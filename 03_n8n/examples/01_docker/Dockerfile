# Минимальное расширение официального образа n8n (Community).
# Сборка: docker build -t my-n8n:local .
# Запуск: см. README.md — обычно достаточно docker run / docker-compose без своего образа.

FROM docker.n8n.io/n8nio/n8n:latest

# Пример: зафиксировать часовой пояс в образе (дублирует env в compose; можно убрать)
ENV TZ=Europe/Moscow

# Раскомментируйте при необходимости кастомных нод:
# USER root
# COPY ./custom-nodes /home/node/.n8n/custom
# USER node
