import uuid

from pydantic import BaseModel


class HomeSchema(BaseModel):
    info: str
