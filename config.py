import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
  DEBUG: False
  TESTING: False
  SECRET_KEY: os.environ.get("SECRET_KEY")

  # Production Database
  DB_NAME = ''
  DB_USERNAME = ''
  DB_PASSWORD = ''

  SESSION_COOKIE_SECURE = True
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class ProductionConfig(Config):
  pass

class DevelopmentConfig(Config):
  DEBUG: True
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SESSION_COOKIE_SECURE = False
