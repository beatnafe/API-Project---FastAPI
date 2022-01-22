from pydantic import BaseSettings

# Use pydantic to read modifications to the configuration from environment variables


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str

    class Config:
        env_file = '.env'


settings = Settings()
