from os import getenv
from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    db_url