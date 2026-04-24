# Пример 1 — Docker: образ n8n

**Номер в каталоге:** [пример 1](../README.md) · запуск без Compose и опциональный `Dockerfile`.

Официальный образ: `docker.n8n.io/n8nio/n8n` (альтернативно `n8nio/n8n` на Docker Hub).

## Быстрый запуск без Compose

Персистентные данные в томе `n8n_data`:

```bash
docker volume create n8n_data

docker run -d --name n8n \
  -p 5678:5678 \
  -e N8N_ENCRYPTION_KEY="замените_на_случайную_строку_не_короче_32_символов" \
  -e WEBHOOK_URL="http://localhost:5678/" \
  -e TZ="Europe/Moscow" \
  -v n8n_data:/home/node/.n8n \
  --restart unless-stopped \
  docker.n8n.io/n8nio/n8n:latest
```

Откройте `http://localhost:5678` и создайте учётную запись владельца.

## Файл `Dockerfile` в этой папке

Минимальный пример наследования официального образа — если понадобится добавить переменные окружения по умолчанию или подготовить образ для CI. Для учебного курса достаточно `docker run` или каталога [`../docker-compose/`](../docker-compose/).

## Остановка и удаление

```bash
docker stop n8n && docker rm n8n
```

Том `n8n_data` сохраняет workflow и credentials до явного удаления: `docker volume rm n8n_data`.
