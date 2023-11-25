from fastapi import APIRouter, Depends

from app.config import Settings, get_settings

router: APIRouter = APIRouter(tags=["base"])


@router.get("/")
async def root(settings: Settings = Depends(get_settings)):
    return settings.model_dump()
