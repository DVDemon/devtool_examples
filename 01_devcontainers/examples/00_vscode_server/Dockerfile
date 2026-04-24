FROM codercom/code-server:4.20.0

# Установка дополнительных системных зависимостей
USER root
RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    gcc \
    g++ \
    cmake \
    make \
    clangd \
    openjdk-17-jdk \
    maven \
    gradle \
    libc6-dev \
    libffi-dev \
    libssl-dev \
    zlib1g-dev \
    libsqlite3-dev \
    libreadline-dev \
    libncurses5-dev \
    libgdbm-dev \
    libbz2-dev \
    liblzma-dev \
    libuuid1 \
    curl \
    wget \
    openssh-client \
    ca-certificates \
    libkrb5-dev \
    libgssapi-krb5-2 \
    && rm -rf /var/lib/apt/lists/*

# Установка Python пакетов
RUN pip3 install --upgrade pip --break-system-packages && \
    pip3 install pylint black isort --break-system-packages

# Создание пользователя для приложения
RUN useradd -m -s /bin/bash appuser && \
    mkdir -p /home/appuser/.vscode-server/extensions && \
    chown -R appuser:appuser /home/appuser

# Создание рабочих директорий и пустого шаблона Git
RUN mkdir -p /app/repositories /app/workspace /app/logs /tmp/empty-git-template && \
    chown -R appuser:appuser /app /tmp/empty-git-template

WORKDIR /app

# Копирование исходного кода
COPY . .

# Установка прав доступа
RUN chown -R appuser:appuser /app

# Переключение на пользователя appuser
USER appuser

# Настройка Git для работы с репозиториями
RUN git config --global --add safe.directory '*'

# Открытие портов
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080 || exit 1

# Установка расширений VS Code
USER coder

# Установка расширений из маркетплейса
RUN code-server --install-extension ms-vscode.cpptools-themes && \
    code-server --install-extension llvm-vs-code-extensions.vscode-clangd && \
    code-server --install-extension ckolkman.vscode-postgres && \
    code-server --install-extension ms-python.python && \
    code-server --install-extension redhat.java && \
    code-server --install-extension vscjava.vscode-java-debug && \
    code-server --install-extension vscjava.vscode-java-test && \
    code-server --install-extension vscjava.vscode-maven

# Запуск code-server
CMD ["code-server", "--bind-addr", "0.0.0.0:8080", "--auth", "none", "/app/workspace"]
