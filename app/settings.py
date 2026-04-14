from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    ENDPOINT: str
    BROKER: str
    TOPIC: str

settings = Settings()