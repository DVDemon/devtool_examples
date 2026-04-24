# Примеры 2–4 — Docker Compose и `.env`

**Номера в каталоге:** [примеры 2–4](../README.md) — SQLite, PostgreSQL, шаблон [`.env.example`](.env.example).

Два варианта:

| Файл | База данных | Назначение |
|------|-------------|------------|
| `docker-compose.sqlite.yml` | SQLite (внутри volume) | Обучение, локальные эксперименты |
| `docker-compose.postgres.yml` | PostgreSQL 16 | Ближе к продакшену |

Отдельно для **RAG + pgvector** (n8n на **SQLite**, Postgres для векторов, контейнер **Ollama** для локальных эмбеддингов): каталог [`../rag-pipeline/`](../rag-pipeline/README.md) — там свой `docker-compose.yml` и `.env.example`.

## Подготовка

1. Скопируйте `.env.example` в `.env`:

   ```bash
   cp .env.example .env
   ```

2. В `.env` задайте **`N8N_ENCRYPTION_KEY`** — длинная случайная строка (не меняйте между перезапусками, иначе расшифруются не все credentials).

3. При использовании Postgres варианта задайте надёжные `POSTGRES_PASSWORD` и `DB_POSTGRESDB_PASSWORD` (можно одинаковые для локалки).

## Запуск (SQLite)

На macOS/Linux часто доступна команда **`docker compose`** (плагин) или **`docker-compose`** (отдельный бинарник) — используйте ту, что установлена у вас (`docker compose version` / `docker-compose version`).

```bash
docker-compose -f docker-compose.sqlite.yml --env-file .env up -d
docker-compose -f docker-compose.sqlite.yml logs -f n8n
```

## Запуск (PostgreSQL)

```bash
docker-compose -f docker-compose.postgres.yml --env-file .env up -d
docker-compose -f docker-compose.postgres.yml logs -f n8n
```

Интерфейс: `http://localhost:5678` (если не меняли порт).

## Переменные

- **`WEBHOOK_URL`** — базовый URL, по которому клиенты достукиваются до вебхуков. Для локали: `http://localhost:5678/`. За reverse proxy укажите публичный `https://ваш-домен/`.
- **`N8N_HOST` / `N8N_PROTOCOL`** — при необходимости согласовать с внешним URL.

Подробнее: [документация n8n по переменным окружения](https://docs.n8n.io/hosting/configuration/environment-variables/).
