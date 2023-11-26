import uuid
from pydantic import BaseModel

class Home(BaseModel):
    id: uuid.UUID
    info: str