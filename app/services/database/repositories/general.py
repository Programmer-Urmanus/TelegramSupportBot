from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncSession
from .base import BaseRepository
from .users import UsersRepository
from .topics import TopicsRepository


class Repository(BaseRepository):
    """
    Base repository abstraction.
    Provides access to SQLAlchemt session.
    """

    users: UsersRepository
    topics: TopicsRepository

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session=session)
        self.users = UsersRepository(session=session)
        self.topics = TopicsRepository(session=session)
