from fastapi import FastAPI

from app.routes import base

app: FastAPI = FastAPI(version="0.0.1", title="xyz")
app.include_router(base.router)
