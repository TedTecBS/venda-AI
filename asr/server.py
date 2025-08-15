from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"service": "asr"}


@app.get("/health")
async def health():
    return {"status": "ok"}
