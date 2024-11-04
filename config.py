import os
from dotenv import load_dotenv
from pathlib import Path
from sqlalchemy import URL

BASE_DIR = Path(__file__).resolve().parent.parent
env_path = load_dotenv(os.path.join(BASE_DIR, '.env'))
load_dotenv(env_path)

class Config:
    """Base config."""
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

class ProdConfig(Config):
    FLASK_ENV = 'production'
    MY_TEST_VAR = os.getenv('TEST')
    SQLALCHEMY_DATABASE_URI = URL.create(
        "mysql+pymysql",
        username="",
        password="",
        host="localhost",
        database="laravel",
    )