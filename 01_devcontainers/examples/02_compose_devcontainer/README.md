# DevContainer с Docker Compose

Пример использования DevContainer с Docker Compose для создания многосервисной среды разработки. Демонстрирует работу с FastAPI приложением и PostgreSQL базой данных.

## Отличия от простого DevContainer

В отличие от `01_first_devcontainer`, этот пример использует **Docker Compose** для управления несколькими сервисами:

- 🐍 **Python 3.12** - основная среда разработки
- 🚀 **FastAPI** - веб-фреймворк с автоматической документацией
- 🗄️ **PostgreSQL 15** - база данных для разработки
- 🔗 **Сетевое взаимодействие** - сервисы работают вместе
- 📦 **Персистентные данные** - данные БД сохраняются в volume

## Структура проекта

```
02_compose_devcontainer/
├── .devcontainer/
│   └── devcontainer.json       # Конфигурация DevContainer с docker-compose
├── docker-compose.yml          # Определение сервисов
└── app.py                      # FastAPI приложение
```

## Конфигурация

### docker-compose.yml

Определяет два сервиса:

1. **`app`** - основной контейнер разработки с Python 3.12
2. **`db`** - PostgreSQL 15 база данных

Сервисы настроены для совместной работы:
- `app` зависит от `db` через `depends_on`
- Сервисы находятся в одной Docker сети и могут обращаться друг к другу по имени
- `app` подключается к БД по имени сервиса `db` (Docker Compose автоматически создает DNS)
- Переменные окружения настроены для подключения к PostgreSQL
- Данные БД сохраняются в Docker volume `postgres-data`

### devcontainer.json

Использует `dockerComposeFile` вместо `image`:

```json
{
  "dockerComposeFile": "docker-compose.yml",
  "service": "app",
  "workspaceFolder": "/workspaces/${localWorkspaceFolderBasename}"
}
```

**Ключевые параметры:**
- `dockerComposeFile` - путь к файлу docker-compose.yml
- `service` - какой сервис использовать как основной контейнер разработки
- `workspaceFolder` - рабочая директория в контейнере
- `forwardPorts` - проброс портов (5432 для PostgreSQL)
- `postCreateCommand` - установка зависимостей после создания
- `customizations` - расширения VS Code

## Использование

### В VS Code

1. **Установите расширение**:
   - "Dev Containers" (ms-vscode-remote.remote-containers)

2. **Откройте проект**:
   ```bash
   cd 02_compose_devcontainer
   code .
   ```

3. **Запустите в контейнере**:
   - `F1` → "Dev Containers: Reopen in Container"
   - VS Code запустит все сервисы из docker-compose.yml

4. **Дождитесь запуска**:
   - Создастся контейнер `app` с Python
   - Запустится контейнер `db` с PostgreSQL
   - Установятся зависимости из `postCreateCommand`

### В DevPod

```bash
cd 02_compose_devcontainer
devpod up
```

## Проверка работы

### Python

```bash
python3 --version
# Python 3.12.x

pip3 list | grep psycopg2
# psycopg2-binary должен быть установлен
```

### PostgreSQL

```bash
# Проверка подключения (используйте имя сервиса 'db' вместо localhost)
psql -h db -U postgres -d devdb -c "SELECT version();"
```

Или используйте расширение VS Code "PostgreSQL" для визуального управления БД.

## FastAPI приложение

Проект включает простое FastAPI приложение (`app.py`) с двумя эндпоинтами для работы с пользователями.

### Запуск приложения

1. **Запустите сервер**:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000 --reload
   ```

2. **Откройте в браузере**:
   - API документация: http://localhost:8000/docs
   - Альтернативная документация: http://localhost:8000/redoc

### API эндпоинты

#### POST /users
Добавление нового пользователя

**Запрос:**
```bash
curl -X POST "http://localhost:8000/users" \
     -H "Content-Type: application/json" \
     -d '{"name": "John Doe", "email": "john@example.com"}'
```

**Ответ:**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

#### GET /users
Получение списка всех пользователей

**Запрос:**
```bash
curl http://localhost:8000/users
```

**Ответ:**
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "email": "jane@example.com"
  }
]
```

### Структура приложения

Приложение использует:
- **FastAPI** - современный веб-фреймворк
- **SQLAlchemy** - ORM для работы с БД
- **Pydantic** - валидация данных (встроен в FastAPI)
- Автоматическое создание таблиц при первом запуске

## Переменные окружения

Следующие переменные окружения доступны в контейнере `app`:

- `POSTGRES_HOST=db` (имя сервиса в docker-compose, Docker автоматически резолвит в IP)
- `POSTGRES_PORT=5432`
- `POSTGRES_USER=postgres`
- `POSTGRES_PASSWORD=postgres`
- `POSTGRES_DB=devdb`

Используйте их в вашем коде для подключения к БД. Обратите внимание, что `POSTGRES_HOST` установлен в `db` (имя сервиса), а не `localhost`, так как сервисы находятся в одной Docker сети.

## Персистентные данные

Данные PostgreSQL сохраняются в Docker volume `postgres-data`. Это означает:

- ✅ Данные сохраняются между перезапусками контейнеров
- ✅ Данные не теряются при пересборке
- ⚠️ Для полного удаления данных используйте `docker-compose down -v`

## Управление сервисами

### Просмотр запущенных контейнеров

```bash
docker-compose ps
```

### Просмотр логов

```bash
# Логи всех сервисов
docker-compose logs

# Логи конкретного сервиса
docker-compose logs db
docker-compose logs app
```

### Остановка сервисов

В VS Code:
- `F1` → "Dev Containers: Reopen Folder Locally"

Или вручную:
```bash
docker-compose down
```

### Перезапуск сервисов

```bash
docker-compose restart
```

## Настройка конфигурации

### Добавление новых сервисов

Отредактируйте `docker-compose.yml` и добавьте новый сервис:

```yaml
services:
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
```

Затем обновите `devcontainer.json`:

```json
{
  "forwardPorts": [5432, 6379]
}
```

### Изменение версий

Измените теги образов в `docker-compose.yml`:

```yaml
services:
  app:
    image: mcr.microsoft.com/devcontainers/python:1-3.11-bullseye
  db:
    image: postgres:14-alpine
```

### Добавление зависимостей

Обновите `postCreateCommand` в `devcontainer.json`:

```json
{
  "postCreateCommand": "pip3 install --user psycopg2-binary redis flask"
}
```

## Преимущества Docker Compose

Использование Docker Compose в DevContainer дает:

1. **Многосервисная архитектура** - легко добавить Redis, RabbitMQ и другие сервисы
2. **Изоляция сервисов** - каждый сервис в своем контейнере
3. **Управление зависимостями** - автоматический запуск зависимых сервисов
4. **Персистентность** - volumes для сохранения данных
5. **Сетевая изоляция** - контроль над сетевым взаимодействием
6. **Масштабируемость** - легко добавить новые сервисы

## Отладка

### Проблемы с подключением к БД

1. Проверьте, что контейнер `db` запущен:
   ```bash
   docker-compose ps
   ```

2. Проверьте логи:
   ```bash
   docker-compose logs db
   ```

3. Проверьте переменные окружения:
   ```bash
   env | grep POSTGRES
   ```

### Проблемы с портами

Если порт 5432 уже занят, измените в `docker-compose.yml`:

```yaml
ports:
  - "5433:5432"  # Используйте другой внешний порт
```

И обновите `POSTGRES_PORT` в переменных окружения.

## Следующие шаги

- Добавьте Redis для кэширования
- Настройте автоматическую миграцию БД при запуске
- Добавьте тестовую БД для запуска тестов
- Настройте hot-reload для разработки

## Полезные ссылки

- [DevContainer с Docker Compose](https://containers.dev/guide/docker-compose)
- [Docker Compose документация](https://docs.docker.com/compose/)
- [PostgreSQL документация](https://www.postgresql.org/docs/)
- [psycopg2 документация](https://www.psycopg.org/docs/)

