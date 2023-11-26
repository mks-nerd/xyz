from fastapi import APIRouter, Depends
from sqlalchemy import select

from app.config import Settings, get_settings
from app.db import async_session
from app.models import base as base_mdoels
from app.schemas import base as base_schemas

router: APIRouter = APIRouter(tags=["base"])


@router.get("/")
async def root(settings: Settings = Depends(get_settings)):
    return settings.model_dump()


@router.get("/info")
async def get_info():
    query = select(base_mdoels.Home)
    async with async_session() as session:
        result = await session.execute(query)
        result = result.scalars().all()
    return {"home": result}


@router.post("/info")
async def add_info(home: base_schemas.Home):
    home = base_mdoels.Home(info="this is test")
    async with async_session() as session:
        session.add(home)
        await session.flush()
        await session.commit()
    return {"home": home.id}
