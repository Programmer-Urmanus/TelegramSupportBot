from typing import Any, Optional

from app.models.sql import UserModel

from .base import BaseRepository


class UsersRepository(BaseRepository):
    """
    Repository for user database operations.
    """

    async def get_by_id(self, user_id: int) -> Optional[UserModel]:
        """
        Get user by primary key ID.
        """
        return await self._get(UserModel, UserModel.id == user_id)

    async def get_by_telegram_id(self, telegram_id: int) -> Optional[UserModel]:
        """
        Get user by unique Telegram ID.
        """
        return await self._get(UserModel, UserModel.telegram_id == telegram_id)

    async def update(self, user_id: int, **kwargs: Any) -> Optional[UserModel]:
        """
        Update user fields by primary key ID.
        Accepts any UserModel fields as kwargs.
        """
        return await self._update(
            model=UserModel,
            conditions=[UserModel.id == user_id],
            load_result=False,
            **kwargs,
        )

    async def delete(self, user_id: int) -> bool:
        """
        Delete user by primary key ID.
        """
        return await self._delete(UserModel, UserModel.id == user_id)
