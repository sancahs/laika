from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = "postgresql://laika:laika123@127.0.0.1:5433/laika"


settings = Settings()
