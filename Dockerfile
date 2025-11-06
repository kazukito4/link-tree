#-----------------------------Build Stage-----------------------------------------
FROM python:3.12-bookworm AS builder

# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && \
    apt-get install -y --no-install-recommends --no-install-suggests \
        curl \
        ca-certificates \
        build-essential && \
    rm -rf /var/lib/apt/lists/*

# Download the latest installer, Run the installer then remove it
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

COPY ./pyproject.toml .

# Install any needed packages specified in requirements.txt
RUN uv sync

#-----------------------------Production Stage-----------------------------------------
FROM python:3.12-slim-bookworm AS production

RUN useradd --create-home appuser
USER appuser

WORKDIR /app

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

COPY /src src
COPY --from=builder /app/.venv .venv

# Make port 8000 available to the world outside this container
EXPOSE 8000

CMD [ "uv","run", "src/main.py"]