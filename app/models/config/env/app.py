from pydantic import BaseModel
from app.models.config.env import PostgresConfig, SQLAlchemyConfig, TelegramConfig


class AppConfig(BaseModel):
    """
    Application configuration aggregator.
    Collects and exposes all environment domains
    required by the application.
    """

    postgres: PostgresConfig
    sql_alchemy: SQLAlchemyConfig
    telegram: TelegramConfig

    # TODO: will include common config later
