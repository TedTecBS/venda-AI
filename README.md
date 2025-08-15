# venda-AI

## Running with Docker Compose

1. Copy `.env.example` to `.env` and fill in the required values:
   ```bash
   cp .env.example .env
   ```
2. Build and start all services:
   ```bash
   docker compose up --build
   ```
3. Open the web client in your browser at [http://localhost:5173](http://localhost:5173).

## Health Checks

Each service provides a `/health` endpoint that returns `{"status": "ok"}`. Docker Compose is configured to call these endpoints to verify container health.