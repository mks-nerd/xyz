import uuid

from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Home(Base):
    __tablename__ = "home"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default_factory=uuid.uuid4, init=False
    )
    info: Mapped[str]
