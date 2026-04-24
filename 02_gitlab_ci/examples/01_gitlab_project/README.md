# GitLab CI Example

Пример проекта для изучения работы с GitLab CI/CD.

## Описание

Этот репозиторий демонстрирует базовые возможности GitLab CI/CD:
- Настройка пайплайна через `.gitlab-ci.yml`
- Запуск тестов в CI/CD
- Сборка Docker-образов
- Использование собственных GitLab Runner
- Работа с артефактами

## Структура проекта

```
.
├── app.py              # Простое Python-приложение
├── test.py             # Тесты для app.py
├── Dockerfile          # Docker-образ для приложения
├── .gitlab-ci.yml      # Конфигурация GitLab CI/CD
├── get_runner.sh       # Скрипт для запуска GitLab Runner
├── file1.txt           # Тестовый файл 1
├── file2.txt           # Тестовый файл 2
└── config/             # Конфигурация GitLab Runner
    └── config.toml
```

## Компоненты

### app.py
Простое Python-приложение, которое выводит "Hello, World!" в консоль.

### test.py
Набор unit-тестов для проверки корректности работы `app.py`. Использует стандартную библиотеку `unittest`.

### Dockerfile
Минимальный Docker-образ на базе `python:3.12-slim` для запуска приложения.

### .gitlab-ci.yml
Конфигурация пайплайна GitLab CI/CD, включающая:
- Проверку конкатенации файлов
- Запуск тестов
- Сборку и публикацию Docker-образов (при необходимости)

## Настройка GitLab Runner

### Локальный запуск Runner

Для запуска GitLab Runner в Docker-контейнере используйте скрипт `get_runner.sh`:

```bash
chmod +x get_runner.sh
./get_runner.sh
```

Скрипт запускает GitLab Runner с:
- Монтированием конфигурации из `./config`
- Доступом к Docker daemon хоста
- Привилегированным режимом для работы с Docker

### Регистрация Runner

Если Runner еще не зарегистрирован, выполните:

```bash
docker run --rm -it --name gitlab-runner \
  -v ./config:/etc/gitlab-runner \
  gitlab/gitlab-runner:latest register \
  --url https://gitlab.mai.ru \
  --token YOUR_REGISTRATION_TOKEN \
  --executor docker \
  --docker-image docker:latest \
  --tag-list "my_runner"
```

### Конфигурация Runner

Конфигурация хранится в `config/config.toml`. Убедитесь, что:
- Указан правильный executor (docker, shell и т.д.)
- Настроены теги для runner (например, `my_runner`)
- Указаны необходимые Docker-образы

## Использование

### Локальный запуск приложения

```bash
python app.py
```

### Запуск тестов

```bash
python test.py
```

### Сборка Docker-образа

```bash
docker build -t app .
docker run app
```

### Запуск пайплайна

Пайплайн автоматически запускается при:
- Push в ветку `main`
- Создании/обновлении Merge Request

Для ручного запуска используйте интерфейс GitLab: **CI/CD → Pipelines → Run pipeline**

## Примеры задач в пайплайне

### job_cat
Проверяет, что конкатенация `file1.txt` и `file2.txt` равна "Hello world". Если проверка не проходит, пайплайн завершается с ошибкой.

## Переменные окружения

Для работы некоторых jobs могут потребоваться переменные окружения в настройках GitLab CI/CD:

- `DOCKER_USERNAME` - логин Docker Hub
- `DOCKER_PASSWORD` - пароль или токен Docker Hub

Настройка: **Settings → CI/CD → Variables**

## Требования

- GitLab (локальный или облачный)
- GitLab Runner (локальный или shared)
- Docker (для работы с Docker executor)
- Python 3.x (для локального запуска)

## Дополнительные ресурсы

- [Документация GitLab CI/CD](https://docs.gitlab.com/ee/ci/)
- [GitLab Runner Documentation](https://docs.gitlab.com/runner/)
- [Docker Documentation](https://docs.docker.com/)

## Лицензия

Этот проект создан в образовательных целях.

