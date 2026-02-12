from sqlalchemy import BigInteger, Boolean, String
from sqlalchemy.orm import Mapped, mapped_column
from .base import BaseModel
from app.models.dto import UserDto


class UserModel(BaseModel):
    """
    User database model.
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)

    first_name: Mapped[str] = mapped_column(String(64), nullable=True)
    last_name: Mapped[str] = mapped_column(String(64), nullable=True)
    username: Mapped[str] = mapped_column(String(64), nullable=True)

    locale: Mapped[str] = mapped_column(String(2), nullable=False)
    is_blocked: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    is_bot_blocked: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    def dto(self) -> UserDto:
        """
        Convert ORM model to domain DTO.
        """
        return UserDto.model_validate(self)
