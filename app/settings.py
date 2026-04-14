from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    ENDPOINT: str
    BROKER: str
    TOPIC: str
    # MODE: str

    # class Config:
    #     env_file="../.env"

settings = Settings()