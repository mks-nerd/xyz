from typing import Final

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

from app.config import Settings, get_db_url, get_settings


class Base(MappedAsDataclass, DeclarativeBase):
    pass


# settings: Settings = get_settings()
DB_URL: Final[str] = get_db_url()
engine = create_async_engine(DB_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)
