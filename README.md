# Venda AI

## System Overview
Venda AI is a modular speech translation platform. Audio sent to the gateway is transcribed by an Automatic Speech Recognition (ASR) service, translated by a Machine Translation (MT) service, enhanced by a Large Language Model (LLM) and converted back to audio by a Text-to-Speech (TTS) service. A web client demonstrates a real-time voice assistant built from these components.

## Repository Structure
```
.
├── asr/        # Speech-to-text services
├── mt/         # Text translation engines
├── llm/        # Large language model applications
├── tts/        # Speech synthesis services
├── gateway/    # API gateway combining all services
└── web/        # Client application
```

## Environment Setup
Create a `.env` file in the repository root with credentials for the services. Typical variables include:

```
OPENAI_API_KEY=<your_openai_key>
GOOGLE_APPLICATION_CREDENTIALS=/path/to/google-creds.json
TTS_API_KEY=<tts_key>
```

## Docker Compose
All components run locally with Docker Compose.

```
docker compose up --build
```

To stop the stack:

```
docker compose down
```

## Components
### ASR
Handles audio transcription. Plug in your preferred model or provider.

### MT
Translates transcribed text into the target language.

### LLM
Optionally rewrites or augments text before speech synthesis.

### TTS
Generates spoken audio from the final text.

### Gateway
Exposes a unified HTTP API to orchestrate the pipeline.

### Web Client
Front‑end for trying the system in a browser.

## Local Run Instructions
1. Clone the repository and create the `.env` file.
2. Start the stack with `docker compose up --build`.
3. Open the web client at [http://localhost:3000](http://localhost:3000).

## Quick Tests
Use `curl` to exercise individual services through the gateway:

```bash
# Health check
curl http://localhost:8000/health

# Translate text
curl -X POST http://localhost:8000/translate \
     -H 'Content-Type: application/json' \
     -d '{"text":"hello","target_lang":"pt"}'
```

