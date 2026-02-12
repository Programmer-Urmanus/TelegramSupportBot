from sqlalchemy import BigInteger, Boolean, String
from sqlalchemy.orm import Mapped, mapped_column
from .base import BaseModel
from app.models.dto import TopicDto


class TopicModel(BaseModel):
    """
    Topic database model.
    """

    __tablename__ = "topics"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)

    initial_message_id: Mapped[int] = mapped_column(BigInteger, nullable=False)

    name: Mapped[str] = mapped_column(String, nullable=False)
    is_translating_enabled: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False
    )

    def dto(self) -> TopicDto:
        """
        Convert ORM model to domain DTO.
        """
        return TopicDto.model_validate(self)
