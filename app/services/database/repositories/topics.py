from typing import Any, Optional

from app.models.sql import TopicModel

from .base import BaseRepository


class TopicsRepository(BaseRepository):
    """
    Repository for topic database operations.
    """

    async def get_by_id(self, topic_id: int) -> Optional[TopicModel]:
        """
        Get topic by primary key ID.
        """
        return await self._get(TopicModel, TopicModel.id == topic_id)

    async def get_by_telegram_id(self, telegram_id: int) -> Optional[TopicModel]:
        """
        Get topic by unique Telegram ID.
        """
        return await self._get(TopicModel, TopicModel.telegram_id == telegram_id)

    async def update(self, topic_id: int, **kwargs: Any) -> Optional[TopicModel]:
        """
        Update topic fields by primary key ID.
        Accepts any TopicModel fields as kwargs.
        """
        return await self._update(
            model=TopicModel,
            conditions=[TopicModel.id == topic_id],
            load_result=False,
            **kwargs,
        )

    async def delete(self, topic_id: int) -> bool:
        """
        Delete topic by primary key ID.
        """
        return await self._delete(TopicModel, TopicModel.id == topic_id)
