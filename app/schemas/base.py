import uuid

from pydantic import BaseModel


class HomeSchema(BaseModel):
    id: uuid.UUID
    info: str
