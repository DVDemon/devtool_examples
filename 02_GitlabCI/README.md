# 02 — GitLab CI/CD

> Непрерывная интеграция и доставка (CI/CD) с использованием GitLab. Автоматизация сборки, тестирования и развёртывания приложений через пайплайны GitLab CI.

## 📖 Лекция

Лекция охватывает следующие темы:

- **Основы CI/CD** — концепции непрерывной интеграции, доставки и развёртывания
- **GitLab CI/CD архитектура** — GitLab Runner, пайплайны, stages, jobs
- **Конфигурация `.gitlab-ci.yml`** — синтаксис, ключевые секции (`stages`, `script`, `only/except`, `tags`, `variables`, `artifacts`)
- **GitLab Runner** — установка, регистрация, типы executor'ов (Docker, Shell, Kubernetes)
- **Docker-in-Docker (dind)** — сборка Docker-образов внутри CI/CD
- **Эволюция пайплайнов** — от простой проверки до полноценного CI/CD с тестами и деплоем
- **Переменные окружения и артефакты** — передача данных между jobs

**Материалы:**
- 📄 [`lection.pdf`](lection.pdf) — слайды лекции

## 📂 Структура примеров

```
02_GitlabCI/
├── lection.pdf
└── examples/
    └── 01_gitlab_project/             # Проект для изучения GitLab CI/CD
        ├── .gitlab-ci.yml             # Финальная конфигурация пайплайна
        ├── app.py                     # Python-приложение
        ├── test.py                    # Unit-тесты
        ├── Dockerfile                 # Docker-образ приложения
        ├── get_runner.sh              # Скрипт запуска GitLab Runner
        ├── file1.txt / file2.txt      # Тестовые файлы для job_cat
        ├── config/
        │   └── config.toml            # Конфигурация Runner
        └── templates/                 # Эволюция .gitlab-ci.yml
            ├── .gitlab-ci.yml.00      # Базовая проверка конкатенации
            ├── .gitlab-ci.yml.01      # Добавление stages
            ├── .gitlab-ci.yml.02      # Добавление тестов
            ├── .gitlab-ci.yml.03      # Добавление Docker-сборки
            └── .gitlab-ci.yml.04      # Полный пайплайн с деплоем
```

## 🧩 Примеры

### 01 — GitLab CI Project

Учебный проект, демонстрирующий полный цикл GitLab CI/CD: от простой проверки конкатенации файлов до многостадийного пайплайна с синтаксической проверкой, unit-тестами и сборкой Docker-образа. В каталоге `templates/` представлена эволюция `.gitlab-ci.yml` от простейшей конфигурации до production-ready пайплайна.

**Ключевые файлы:**
- [`.gitlab-ci.yml`](examples/01_gitlab_project/.gitlab-ci.yml) — финальная конфигурация пайплайна
- [`templates/`](examples/01_gitlab_project/templates/) — 5 шагов эволюции CI/CD конфигурации (от 00 до 04)
- [`get_runner.sh`](examples/01_gitlab_project/get_runner.sh) — скрипт для запуска собственного GitLab Runner

[→ Подробнее](examples/01_gitlab_project/README.md)

---

[← К корневому README](../README.md)
