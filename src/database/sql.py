"""Relational database setup."""
import sqlalchemy
from utils.settings import settings

engine = sqlalchemy.create_engine(
    settings.sql_connection,
    pool_pre_ping=True,
)
