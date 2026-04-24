# Первый DevContainer

Простейший пример использования DevContainer с Python 3.12. Этот пример демонстрирует базовую настройку изолированной среды разработки.

## Что такое DevContainer?

DevContainer (Development Container) - это способ создания воспроизводимых сред разработки в Docker контейнерах. Это позволяет:

- 🐳 **Изоляция** - каждый проект имеет свою среду разработки
- 🔄 **Воспроизводимость** - одинаковое окружение на любой машине
- 🚀 **Быстрый старт** - не нужно настраивать инструменты вручную
- 👥 **Совместимость** - команда работает в одинаковых условиях

## Структура проекта

```
01_first_devcontainer/
└── .devcontainer/
    └── devcontainer.json       # Конфигурация DevContainer
```

## Конфигурация

Проект использует базовый образ Microsoft для Python разработки:

- **Образ**: `mcr.microsoft.com/devcontainers/python:1-3.12-bullseye`
- **Python версия**: 3.12
- **Базовая ОС**: Debian Bullseye

## Использование

### В VS Code

1. **Установите расширение**:
   - Откройте VS Code
   - Установите расширение "Dev Containers" (ms-vscode-remote.remote-containers)

2. **Откройте проект**:
   ```bash
   cd 01_first_devcontainer
   code .
   ```

3. **Запустите в контейнере**:
   - VS Code предложит открыть проект в контейнере
   - Нажмите "Reopen in Container" или используйте команду:
     - `F1` → "Dev Containers: Reopen in Container"

4. **Дождитесь сборки**:
   - VS Code соберет и запустит контейнер
   - Это может занять несколько минут при первом запуске

### В DevPod

1. **Инициализируйте DevPod**:
   ```bash
   devpod up
   ```

2. **Откройте в браузере**:
   - DevPod предоставит URL для доступа к среде разработки

## Что внутри контейнера?

После запуска контейнера вы получите:

- ✅ Python 3.12 с pip
- ✅ Git
- ✅ Стандартные инструменты разработки
- ✅ Настроенное окружение для Python разработки

## Проверка работы

После запуска контейнера проверьте установку Python:

```bash
python3 --version
# Должно показать: Python 3.12.x

pip3 --version
# Должно показать версию pip
```

## Создание Python проекта

1. Создайте файл `main.py`:
   ```python
   print("Hello from DevContainer!")
   ```

2. Запустите:
   ```bash
   python3 main.py
   ```

## Установка зависимостей

Для установки Python пакетов используйте pip:

```bash
pip3 install --user package-name
```

Или создайте `requirements.txt` и используйте:

```bash
pip3 install --user -r requirements.txt
```

> **Примечание**: Используйте флаг `--user` для установки пакетов в пользовательскую директорию, чтобы не требовались права root.

## Настройка контейнера

Вы можете настроить контейнер, отредактировав `.devcontainer/devcontainer.json`:

- **Добавить порты**: раскомментируйте `forwardPorts`
- **Установить зависимости**: раскомментируйте `postCreateCommand`
- **Добавить расширения VS Code**: используйте `customizations`
- **Добавить Features**: используйте `features`

### Пример расширенной конфигурации

```json
{
  "name": "Python 3",
  "image": "mcr.microsoft.com/devcontainers/python:1-3.12-bullseye",
  
  "forwardPorts": [8000, 5000],
  
  "postCreateCommand": "pip3 install --user -r requirements.txt",
  
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance"
      ]
    }
  }
}
```

## Управление контейнером

### Остановка

В VS Code:
- `F1` → "Dev Containers: Reopen Folder Locally"

В DevPod:
```bash
devpod stop
```

### Удаление

В VS Code:
- `F1` → "Dev Containers: Rebuild Container"

В DevPod:
```bash
devpod delete
```

## Следующие шаги

После освоения этого примера переходите к:
- `02_compose_devcontainer/` - более сложный пример с Docker Compose
- Добавление собственных инструментов и расширений
- Настройка персистентных данных

## Полезные ссылки

- [DevContainer спецификация](https://containers.dev/)
- [DevContainer Features](https://containers.dev/features)
- [Python DevContainer шаблоны](https://github.com/devcontainers/templates/tree/main/src/python)
- [VS Code Remote Containers](https://code.visualstudio.com/docs/remote/containers)
- [DevPod документация](https://devpod.sh/)

