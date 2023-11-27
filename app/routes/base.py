from fastapi import APIRouter, Depends
from sqlalchemy import select

from app.config import Settings, get_settings
from app.db import async_session
from app.models.base import Home
from app.schemas.base import HomeSchema

router: APIRouter = APIRouter(tags=["base"])


@router.get("/")
async def root(settings: Settings = Depends(get_settings)):
    return settings.model_dump()


@router.get("/info")
async def get_info():
    query = select(Home)
    async with async_session() as session:
        result = await session.execute(query)
        result = result.scalars().all()
    return {"data": result}


@router.post("/info")
async def add_info(home_schema: HomeSchema):
    home = Home(info=home_schema.info)
    async with async_session() as session:
        session.add(home)
        await session.flush()
        await session.commit()
    return {"id": home.id}
