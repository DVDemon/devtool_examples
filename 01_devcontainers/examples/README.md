# Примеры DevContainer и DevPod

Коллекция примеров для работы с DevContainer и DevPod - инструментами для создания изолированных сред разработки в Docker контейнерах.

## Структура проекта

```
devcontainer_examples/
├── 00_vscode_server/              # VS Code Server в Docker контейнере
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── workspace/
├── 01_first_devcontainer/         # Первый пример DevContainer
│   └── .devcontainer/
│       └── devcontainer.json
└── 02_compose_devcontainer/        # DevContainer с Docker Compose + FastAPI
    ├── .devcontainer/
    │   └── devcontainer.json
    ├── docker-compose.yml
    ├── app.py                      # FastAPI приложение
    └── run.sh                      # Скрипт запуска
```

## Примеры

### 00_vscode_server

Полнофункциональный VS Code Server, запущенный в Docker контейнере с предустановленными расширениями и инструментами разработки.

**Возможности:**
- VS Code Server в браузере
- Поддержка Python, Java 17, C++
- PostgreSQL клиент
- Персистентные настройки и рабочая область

**Подробнее:** см. [README.md в директории 00_vscode_server](./00_vscode_server/README.md)

### 01_first_devcontainer

Простейший пример DevContainer с Python 3.12. Демонстрирует базовую настройку изолированной среды разработки.

**Возможности:**
- Базовый DevContainer с Python 3.12
- Готовая среда для Python разработки
- Простая конфигурация для изучения основ

**Подробнее:** см. [README.md в директории 01_first_devcontainer](./01_first_devcontainer/README.md)

### 02_compose_devcontainer

Пример DevContainer с использованием Docker Compose для многосервисной среды разработки. Включает готовое FastAPI приложение с двумя API эндпоинтами для работы с пользователями.

**Возможности:**
- DevContainer с Docker Compose
- Python 3.12 + PostgreSQL 15
- FastAPI приложение (готовое к использованию)
- SQLAlchemy ORM для работы с БД
- Два API эндпоинта: POST /users и GET /users
- Автоматическая документация API (Swagger UI)
- Многосервисная архитектура
- Персистентные данные БД
- Скрипт запуска приложения

**Файлы:**
- `app.py` - компактное FastAPI приложение (55 строк)
- `run.sh` - скрипт для запуска сервера
- `docker-compose.yml` - конфигурация сервисов

**Подробнее:** см. [README.md в директории 02_compose_devcontainer](./02_compose_devcontainer/README.md)

## Требования

- Docker
- Docker Compose (для примеров с compose)

## Быстрый старт

### Для начинающих
Начните с `01_first_devcontainer` - простейший пример для понимания основ DevContainer.

### Для практики
Используйте `02_compose_devcontainer` - готовое FastAPI приложение с базой данных для практической разработки.

### Для работы в браузере
Используйте `00_vscode_server` - полнофункциональный VS Code в браузере.

**Общий алгоритм:**
1. Выберите интересующий пример
2. Перейдите в соответствующую директорию
3. Следуйте инструкциям в README.md примера
4. Для примеров с DevContainer: откройте в VS Code и выберите "Reopen in Container"

## Технологии

Проекты используют следующие технологии:
- **Docker** и **Docker Compose** - контейнеризация
- **DevContainer** - стандарт конфигурации сред разработки
- **Python 3.12** - язык программирования
- **FastAPI** - современный веб-фреймворк
- **SQLAlchemy** - ORM для работы с БД
- **PostgreSQL** - реляционная база данных
- **VS Code Server** - редактор кода в браузере

## Полезные ссылки

- [DevContainer спецификация](https://containers.dev/)
- [DevPod документация](https://devpod.sh/)
- [VS Code Remote Containers](https://code.visualstudio.com/docs/remote/containers)
- [Code Server](https://github.com/coder/code-server)
- [FastAPI документация](https://fastapi.tiangolo.com/)
- [SQLAlchemy документация](https://www.sqlalchemy.org/)

