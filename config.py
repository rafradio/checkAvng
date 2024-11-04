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
        drivername="mysql+pymysql",
        username=os.getenv('my_USER_DB'),
        password=os.getenv('my_PASSWORD_DB'),
        host=os.getenv('HOST'),
        database=os.getenv('DATABASE'),
    )