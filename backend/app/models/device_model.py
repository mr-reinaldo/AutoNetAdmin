from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import mapper_registry


class DeviceDriver(str, Enum):
    ios: str = 'ios'
    eos: str = 'eos'
    nxos: str = 'nxos'
    iosxr: str = 'iosxr'
    junos: str = 'junos'


class DeviceType(str, Enum):
    router: str = 'router'
    switch: str = 'switch'
    firewall: str = 'firewall'
    load_balancer: str = 'load_balancer'


@mapper_registry.mapped_as_dataclass
class Device:
    __tablename__ = 'devices'

    id: Mapped[UUID] = mapped_column(
        init=False,
        primary_key=True,
        unique=True,
        index=True,
        default_factory=uuid4,
    )
    user_id: Mapped[UUID] = mapped_column(ForeignKey('users.id'))
    hostname: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    username: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    enable_password: Mapped[str] = mapped_column(nullable=False)
    device_type: Mapped[DeviceType] = mapped_column(
        nullable=False, default=DeviceType.router
    )
    ssh_port: Mapped[int] = mapped_column(default=22)
    driver_name: Mapped[DeviceDriver] = mapped_column(
        nullable=False, default=DeviceDriver.ios
    )

    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), onupdate=func.now()
    )
    user = relationship('User', back_populates='devices', lazy='joined', uselist=True)
