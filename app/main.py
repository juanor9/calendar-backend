from fastapi import FastAPI
from dotenv import load_dotenv
from app.core.config import get_settings

load_dotenv()
settings = get_settings()

app = FastAPI()


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "database_url": settings.database_url
    }

