from typing import Generator

from sqlalchemy.exc import PendingRollbackError
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from core.config import settings

engine = create_async_engine(
    settings.DATABASE_URI,
)

async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

Base = declarative_base()


async def get_db() -> Generator:
    db = async_session()
    try:
        yield db
        await db.commit()
    except PendingRollbackError:
        await db.rollback()
    finally:
        await db.close()
