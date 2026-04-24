# 01 — DevContainers и DevPod

> Изолированные среды разработки в Docker контейнерах. DevContainer — стандарт конфигурации воспроизводимых сред разработки, поддерживаемый VS Code, DevPod, GitHub Codespaces и другими инструментами.

## 📖 Лекция

Лекция охватывает следующие темы:

- **Проблема воспроизводимости окружений** — почему "на моей машине работает" больше не проблема
- **DevContainer (Development Container)** — стандарт [`devcontainer.json`](https://containers.dev/), образы, features, жизненный цикл контейнера
- **VS Code Server** — полноценный редактор в браузере через [`code-server`](https://github.com/coder/code-server)
- **DevPod** — open-source альтернатива для управления dev-средами на любом бэкенде (Docker, SSH, Kubernetes)
- **Docker Compose + DevContainer** — многосервисные среды (приложение + БД + кэш)
- **DevContainer Features** — переиспользуемые компоненты (Docker-in-Docker, Node.js, Java и т.д.)

**Материалы:**
- 📄 [`lection.pdf`](lection.pdf) — слайды лекции

## 📂 Структура примеров

```
01_devcontainers/
├── lection.pdf
└── examples/
    ├── README.md                       # Общий README для всех примеров
    ├── 00_vscode_server/               # VS Code Server в Docker
    │   ├── Dockerfile
    │   ├── docker-compose.yml
    │   └── workspace/
    ├── 01_first_devcontainer/          # Базовый DevContainer
    │   └── .devcontainer/
    │       └── devcontainer.json
    └── 02_compose_devcontainer/        # DevContainer + Docker Compose
        ├── .devcontainer/
        │   └── devcontainer.json
        ├── docker-compose.yml
        ├── app.py
        └── run.sh
```

## 🧩 Примеры

### 00 — VS Code Server в Docker

Полнофункциональный VS Code Server, запущенный в Docker контейнере с предустановленными расширениями для Python, Java 17, C++ и PostgreSQL. Доступен через браузер.

[→ Подробнее](examples/00_vscode_server/README.md)

### 01 — Первый DevContainer

Простейший пример использования DevContainer с Python 3.12. Демонстрирует базовую настройку изолированной среды разработки через `devcontainer.json`.

[→ Подробнее](examples/01_first_devcontainer/README.md)

### 02 — DevContainer с Docker Compose

Пример DevContainer с Docker Compose для многосервисной среды разработки. Включает FastAPI приложение и PostgreSQL базу данных.

[→ Подробнее](examples/02_compose_devcontainer/README.md)

---

[← К корневому README](../README.md)
