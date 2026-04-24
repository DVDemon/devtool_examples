# DevTools Examples

> Учебный репозиторий с примерами и материалами лекций по современным инструментам разработки (DevTools). Курс охватывает контейнеризацию сред разработки, CI/CD и автоматизацию бизнес-процессов.

## 📚 Модули курса

| № | Раздел | Тема | Материалы |
|---|--------|------|-----------|
| 01 | [`01_devcontainers/`](01_devcontainers/) | **DevContainers и DevPod** — изолированные среды разработки в Docker | [README](01_devcontainers/README.md) · [lection.pdf](01_devcontainers/lection.pdf) |
| 02 | [`02_GitlabCI/`](02_GitlabCI/) | **GitLab CI/CD** — непрерывная интеграция и доставка | [README](02_GitlabCI/README.md) · [lection.pdf](02_GitlabCI/lection.pdf) |
| 03 | [`03_n8n/`](03_n8n/) | **n8n** — автоматизация бизнес-процессов и RAG | [README](03_n8n/README.md) · [lection.pdf](03_n8n/lection.pdf) · [cheatsheet](03_n8n/n8n_cheatsheet.jpg) |

## 🎯 Цели курса

- Понять проблему воспроизводимости сред разработки и освоить DevContainer как стандарт её решения
- Научиться настраивать пайплайны CI/CD в GitLab: от простых проверок до полноценной сборки и деплоя
- Освоить платформу n8n для визуальной автоматизации, включая RAG-пайплайны с LLM и векторными базами данных

## 🧰 Требования

Для работы с примерами необходимо:

- **Docker** и **Docker Compose** — для всех примеров с контейнерами
- **VS Code** с расширением **Dev Containers** (`ms-vscode-remote.remote-containers`) — для примеров DevContainer
- **GitLab** (локальный или облачный) и **GitLab Runner** — для примеров CI/CD
- **Python 3.x** — для некоторых скриптов и приложений

## 📂 Структура репозитория

```
devtool_examples/
├── 01_devcontainers/          # DevContainers и DevPod
│   ├── lection.pdf
│   ├── README.md
│   └── examples/
├── 02_GitlabCI/               # GitLab CI/CD
│   ├── lection.pdf
│   ├── README.md
│   └── examples/
├── 03_n8n/                    # n8n автоматизация
│   ├── lection.pdf
│   ├── n8n_cheatsheet.jpg
│   ├── README.md
│   └── examples/
├── README.md                  # Данный файл
└── LICENSE                    # Apache License 2.0
```

## 📖 Как пользоваться

1. Выберите интересующий модуль из таблицы выше
2. Откройте соответствующий `README.md` для обзора темы и списка примеров
3. Переходите в конкретный пример для детальных инструкций
4. Для примеров с DevContainer: откройте директорию в VS Code и выберите "Reopen in Container"

## 📄 Лицензия

Распространяется под лицензией **Apache License 2.0**. Подробнее см. [`LICENSE`](LICENSE).
