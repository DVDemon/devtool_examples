# VS Code Server в Docker

Этот проект предоставляет VS Code Server, запущенный в Docker контейнере с предустановленными расширениями и настройками.

## Возможности

- 🚀 **VS Code Server** - полная функциональность VS Code в браузере
- 🐍 **Python** - с расширениями и инструментами разработки
- ☕ **Java 17** - с Maven, Gradle и расширениями для разработки
- 🔧 **C++** - с Clangd и темами
- 🗄️ **PostgreSQL** - поддержка базы данных
- 📁 **Персистентные настройки** - все настройки сохраняются на хосте

## Установленные расширения

### Из маркетплейса:
- `ms-vscode.cpptools-themes` - темы для C++
- `llvm-vs-code-extensions.vscode-clangd` - поддержка Clangd
- `ckolkman.vscode-postgres` - поддержка PostgreSQL
- `ms-python.python` - поддержка Python
- `redhat.java` - основное Java расширение
- `vscjava.vscode-java-debug` - отладчик для Java
- `vscjava.vscode-java-test` - тестирование Java
- `vscjava.vscode-maven` - поддержка Maven

### Локальное расширение:
- `vcomit.c4-varp` - из файла c4-varp-1.0.0.vsix

## Структура проекта

```
00_vscode_server/
├── docker-compose.yml          # Конфигурация Docker Compose
├── Dockerfile                  # Образ с VS Code Server
├── README.md                   # Документация проекта
└── workspace/                  # Рабочая область (персистентная)
```

## Запуск

1. **Запуск контейнера:**
   ```bash
   docker-compose up -d
   ```

2. **Открытие VS Code Server:**
   - Откройте браузер и перейдите по адресу: http://localhost:8080
   - VS Code Server автоматически откроет папку `/app/workspace`

3. **Остановка:**
   ```bash
   docker-compose down
   ```

## Персистентные данные

Все важные данные сохраняются на хостовой машине:

- **`workspace/`** - ваши проекты и файлы (монтируется в `/app/workspace`)

## Управление контейнером

```bash
# Просмотр статуса
docker-compose ps

# Просмотр логов
docker-compose logs

# Перезапуск
docker-compose restart

# Пересборка образа
docker-compose up --build -d
```

## Разработка

Для разработки используйте папку `workspace/` - все файлы в ней будут доступны в VS Code Server и сохранятся на хостовой машине.

## Поддержка

При возникновении проблем проверьте логи:
```bash
docker-compose logs vscode-server
```

## Технические детали

- **Базовый образ**: `codercom/code-server:4.20.0`
- **Порт**: 8080
- **Пользователь**: `coder` (для code-server), `appuser` (для приложений)
- **Рабочая директория**: `/app/workspace`
- **Аутентификация**: отключена (для локальной разработки)

