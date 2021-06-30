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

  SQLALCHEMY_DATABASE_URI = ''

class ProductConfig(Config):
  pass

class DevelopmentConfig(Config):
  DEBUG: True
  # Production Database
  DB_NAME = 'gw_portal'
  DB_USERNAME = 'postgres'
  DB_PASSWORD = 'password'

  SESSION_COOKIE_SECURE = False

  SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/gw_portal'