"""App configuration."""
from os import environ, path

import redis
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    """Set Flask configuration variables from .env file."""

    # General Config
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")
    SECRET_KEY = environ.get("SECRET_KEY") or 'gsdfes423e'

    # Flask-Session
    REDIS_URI = environ.get("SESSION_REDIS") or 'redis://127.0.0.1:6379'
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.from_url(REDIS_URI)

    # Flask-Assets
    LESS_BIN = environ.get("LESS_BIN") or '/usr/bin/lessc'
    ASSETS_DEBUG = False
    LESS_RUN_IN_DEBUG = False

    # Static Assets
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    COMPRESSOR_DEBUG = True

    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI") or 'mysql+pymysql://admin:admin@localhost:3306/db_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
