python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-ingest.txt
# workflow «RAG 01» в n8n должен быть активирован (webhook зарегистрирован)
python imporrt_rag.py --dry-run   # проверить число чанков
python imporrt_rag.py