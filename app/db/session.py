from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import get_settings

settings = get_settings()
engine = create_async_engine(settings.database_url, echo=True)

async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)



async def get_session() -> AsyncGenerator[AsyncSession, None]:
    session = async_session()
    try:
        yield session
    finally:
        await session.close()
