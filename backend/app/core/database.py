from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    AsyncEngine,
    async_sessionmaker,
)
from app.core.settings import settings
from typing import AsyncGenerator


engine: AsyncEngine = create_async_engine(
    url=settings.DATABASE_URL, echo=settings.ECHO_SQLALCHEMY
)


async_session: AsyncSession = async_sessionmaker(
    engine=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
