#!/usr/bin/env python3
"""
Заливка PDF из каталога docs в RAG через n8n workflow «RAG 01 — Ingest» (webhook).

Ожидается запущенный стенд из README: POST с телом
{"text": "...", "source": "..."} на /webhook/rag-ingest.

Зависимости: pip install -r requirements-ingest.txt
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


def extract_pdf_text(path: Path) -> str:
    from pypdf import PdfReader

    reader = PdfReader(str(path))
    parts: list[str] = []
    for page in reader.pages:
        t = page.extract_text()
        if t:
            parts.append(t)
    return "\n\n".join(parts).strip()


def chunk_text(text: str, chunk_size: int, overlap: int) -> list[str]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be in [0, chunk_size)")

    text = " ".join(text.split())
    if not text:
        return []

    chunks: list[str] = []
    start = 0
    n = len(text)
    while start < n:
        end = min(start + chunk_size, n)
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end >= n:
            break
        start = end - overlap
        if start <= 0:
            start = end
    return chunks


def post_ingest(url: str, text: str, source: str, timeout: float) -> tuple[int, str]:
    body = json.dumps({"text": text, "source": source}, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
            return resp.status, raw
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace") if e.fp else ""
        return e.code, err_body or str(e)
    except urllib.error.URLError as e:
        return -1, str(e.reason if hasattr(e, "reason") else e)


def main() -> int:
    default_docs = Path(__file__).resolve().parent / "docs"
    default_url = "http://localhost:5678/webhook/rag-ingest"

    p = argparse.ArgumentParser(
        description="Импорт PDF из каталога в RAG (n8n webhook rag-ingest)."
    )
    p.add_argument(
        "--docs-dir",
        type=Path,
        default=default_docs,
        help=f"Каталог с PDF (по умолчанию: {default_docs})",
    )
    p.add_argument(
        "--webhook-url",
        default=default_url,
        help=f"URL webhook (по умолчанию: {default_url})",
    )
    p.add_argument("--chunk-size", type=int, default=1200, help="Целевой размер чанка в символах")
    p.add_argument("--overlap", type=int, default=200, help="Перекрытие соседних чанков")
    p.add_argument("--delay", type=float, default=0.2, help="Пауза между запросами, сек")
    p.add_argument("--timeout", type=float, default=120.0, help="Таймаут HTTP на один чанк")
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Только показать, сколько чанков будет отправлено",
    )
    args = p.parse_args()

    docs_dir: Path = args.docs_dir.resolve()
    if not docs_dir.is_dir():
        print(f"Каталог не найден: {docs_dir}", file=sys.stderr)
        print("Создайте каталог docs и положите туда PDF.", file=sys.stderr)
        return 1

    pdfs = sorted(docs_dir.glob("*.pdf")) + sorted(docs_dir.glob("*.PDF"))
    # убрать дубликаты при case-insensitive ФС
    seen: set[Path] = set()
    unique_pdfs: list[Path] = []
    for f in pdfs:
        key = f.resolve()
        if key not in seen:
            seen.add(key)
            unique_pdfs.append(f)

    if not unique_pdfs:
        print(f"В {docs_dir} нет файлов *.pdf", file=sys.stderr)
        return 1

    plan: list[tuple[Path, int, str, str]] = []
    for pdf_path in unique_pdfs:
        try:
            full = extract_pdf_text(pdf_path)
        except Exception as e:
            print(f"Ошибка чтения {pdf_path.name}: {e}", file=sys.stderr)
            continue
        if not full:
            print(f"Пустой текст: {pdf_path.name} (пропуск)", file=sys.stderr)
            continue
        chunks = chunk_text(full, args.chunk_size, args.overlap)
        rel = pdf_path.name
        for i, ch in enumerate(chunks):
            source = f"{rel}#chunk-{i + 1}-of-{len(chunks)}"
            plan.append((pdf_path, i + 1, source, ch))

    if not plan:
        print("Нечего отправлять (нет текста после извлечения).", file=sys.stderr)
        return 1

    print(f"Файлов: {len(unique_pdfs)}, чанков к отправке: {len(plan)}")
    if args.dry_run:
        return 0

    ok = 0
    for pdf_path, idx_in_file, source, text in plan:
        status, body = post_ingest(args.webhook_url, text, source, args.timeout)
        if status == 200:
            ok += 1
            print(f"OK  {pdf_path.name} [{idx_in_file}] source={source!r}")
        else:
            print(
                f"ERR {pdf_path.name} [{idx_in_file}] HTTP {status} source={source!r}\n  {body[:500]}",
                file=sys.stderr,
            )
        if args.delay > 0:
            time.sleep(args.delay)

    print(f"Готово: успешно {ok}/{len(plan)}")
    return 0 if ok == len(plan) else 2


if __name__ == "__main__":
    raise SystemExit(main())
