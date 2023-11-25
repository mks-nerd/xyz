from fastapi import APIRouter

router: APIRouter = APIRouter(tags=["base"])


@router.get("/")
def root():
    return {"message": True}
