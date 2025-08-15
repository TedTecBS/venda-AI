from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index():
    return "<h1>Web Client</h1>"


@app.get("/health")
async def health():
    return {"status": "ok"}
