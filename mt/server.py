from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"service": "mt"}


@app.get("/health")
async def health():
    return {"status": "ok"}
