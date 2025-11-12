#-----------------------------Build Stage-----------------------------------------
FROM python:3.12-bookworm AS builder

# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && \
    apt-get install -y --no-install-recommends --no-install-suggests \
        curl \
        ca-certificates \
        build-essential && \
    rm -rf /var/lib/apt/lists/*

# Download do Instalador mais recente, roda ele e aí remove
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Garantir que o binario instalado está no `PATH`
ENV PATH="/root/.local/bin/:$PATH"

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

# copia apenas o que precisa pro uv sync rodar
COPY ./pyproject.toml .

# Instala qualquer pacote no requirements.txt
RUN uv sync

#-----------------------------Production Stage-----------------------------------------
FROM python:3.12-slim-bookworm AS production

RUN useradd --create-home appuser
USER appuser

WORKDIR /app

# Garantir que o binario instalado está no `PATH`
ENV PATH="/app/.venv/bin/:$PATH"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

COPY /src src
COPY --from=builder /app/.venv .venv

# expor a porta 8000
EXPOSE 8000

# copiar o comando do uv do root
COPY --from=builder /root/.local/bin/uv /usr/local/bin/uv
CMD [ "uv","run", "src/main.py"]
