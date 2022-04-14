# import dependencies
from pydantic import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = "../../.env"

    # sftp credentials
    SSH_HOST: str
    SSH_USER: str
    SSH_PRIVATE_KEY_FILE_PATH: str
    SSH_PRIVATE_KEY_FILE_PASSWORD: str
    SSH_DIR: str = "files"

    # database credentials
    DB_HOST: str
    DB_USER: str
    DB_PASSWORD: str
    DB_DATABASE: str
    DB_PORT: int = 5432

    @property
    def sql_connection(self) -> str:
        """str: Synchronous Application connection string."""
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_DATABASE}"  # noqa: 501


settings = Settings()
