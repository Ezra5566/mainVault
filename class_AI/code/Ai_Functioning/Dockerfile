# Dockerfile for the End‑to‑End Data Science Pipeline
# ----------------------------------------------------
# This Docker image packages the complete pipeline:
#   * PostgreSQL client (psycopg2)
#   * PySpark
#   * PyTorch + TorchVision
#   * FastAPI + Uvicorn (model serving)
#   * Streamlit (UI)
#   * All Python dependencies from requirements.txt
#
# Build with:  docker build -t data-pipeline .
# Run with:    docker compose up -d
#
# The container expects environment variables for DB access and social‑API keys
# (see docker-compose.yml and the .env.example file).

# ---------- Base image ----------
FROM python:3.11-slim

# ---------- System dependencies ----------
#   - build-essential for compiling any binary wheels
#   - libpq-dev for PostgreSQL client libraries
#   - ca-certificates & curl for potential secret fetching
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        ca-certificates \
        curl && \
    rm -rf /var/lib/apt/lists/*

# ---------- Create non‑root user ----------
ARG UID=1000
ARG GID=1000
RUN groupadd -g ${GID} appuser && \
    useradd -m -u ${UID} -g ${GID} -s /bin/bash appuser

# ---------- Working directory ----------
WORKDIR /app

# ---------- Python dependencies ----------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---------- Copy source code ----------
COPY . .

# ---------- Permissions ----------
RUN chown -R appuser:appuser /app && \
    chmod -R 755 /app

# ---------- Switch to non‑root user ----------
USER appuser

# ---------- Expose ports ----------
EXPOSE 8000
EXPOSE 8501

# ---------- Default command ----------
# By default, show the Run‑pipeline help message.
# Users can override this in docker‑compose.yml or with `docker compose run`.
CMD ["python", "-m", "run_pipeline", "--help"]