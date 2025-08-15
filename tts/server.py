from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"service": "tts"}


@app.get("/health")
async def health():
    return {"status": "ok"}
