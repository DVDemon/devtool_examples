# 03 — n8n: Автоматизация бизнес-процессов

> n8n — платформа с открытым исходным кодом для визуальной автоматизации рабочих процессов (workflow automation). Позволяет соединять любые сервисы через drag-and-drop интерфейс с возможностью написания собственного кода.

## 📖 Лекция

Лекция охватывает следующие темы:

- **Введение в n8n** — архитектура, self-hosted vs cloud, основные концепции (workflow, node, credential, trigger)
- **Развёртывание n8n** — Docker, Docker Compose, SQLite vs PostgreSQL, переменные окружения
- **Основные типы нод** — triggers (Webhook, Schedule, Polling), actions (HTTP Request, Telegram, AI)
- **LangChain интеграция** — AI Agent, Chat Model, Embeddings, Vector Stores
- **RAG (Retrieval-Augmented Generation)** — полный цикл: индексация → векторное хранение → поиск → генерация ответа
- **Локальные эмбеддинги с Ollama** — запуск LLM на локальной машине, интеграция с n8n
- **Telegram боты на n8n** — polling, обработка сообщений, AI-агенты

**Материалы:**
- 📄 [`lection.pdf`](lection.pdf) — слайды лекции
- 🖼️ [`n8n_cheatsheet.jpg`](n8n_cheatsheet.jpg) — шпаргалка по основным нодам и концепциям

## 📂 Структура примеров

```
03_n8n/
├── lection.pdf
├── n8n_cheatsheet.jpg
└── examples/
    ├── 01_docker/                     # Запуск n8n через Docker (без Compose)
    │   ├── Dockerfile
    │   └── README.md
    ├── 02_docker-compose/             # Docker Compose: SQLite и PostgreSQL
    │   ├── docker-compose.sqlite.yml
    │   ├── docker-compose.postgres.yml
    │   ├── .env.example
    │   └── README.md
    └── 03_rag-pipeline/               # Полный RAG пайплайн
        ├── docker-compose.yml
        ├── .env.example
        ├── import_rag.py              # Скрипт загрузки PDF
        ├── requirements-ingest.txt
        ├── init-db/                   # Инициализация pgvector
        ├── docs/                      # Примеры PDF для загрузки
        └── workflows/                 # Экспортированные workflow n8n
```

## 🧩 Примеры

### 01 — Docker: образ n8n

Запуск n8n в Docker контейнере без Docker Compose. Минимальный `Dockerfile` для расширения официального образа. Подходит для быстрого ознакомления.

[→ Подробнее](examples/01_docker/README.md)

### 02 — Docker Compose и `.env`

Два варианта развёртывания n8n: с SQLite (для обучения) и PostgreSQL (ближе к продакшену). Демонстрирует использование `.env` файлов для конфигурации.

[→ Подробнее](examples/02_docker-compose/README.md)

### 03 — RAG pipeline: n8n + pgvector + Ollama + DeepSeek

Полный учебный стенд Retrieval-Augmented Generation: индексация документов в векторное хранилище (pgvector), локальные эмбеддинги через Ollama, Telegram бот с AI Agent на DeepSeek.

[→ Подробнее](examples/03_rag-pipeline/README.md)

---

[← К корневому README](../README.md)
