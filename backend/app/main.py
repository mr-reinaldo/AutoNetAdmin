from fastapi import FastAPI

from app.core.settings import settings

app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION,
    root_path=settings.API_PREFIX,
)
