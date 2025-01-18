from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import mapper_registry


@mapper_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[UUID] = mapped_column(
        init=False,
        primary_key=True,
        unique=True,
        index=True,
        default_factory=uuid4,
    )
    username: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), onupdate=func.now()
    )

    devices = relationship(
        'Device',
        back_populates='user',
        lazy='joined',
        uselist=True,
        cascade='all, delete-orphan',
    )
