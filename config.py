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

  # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
  SQLALCHEMY_DATABASE_URI = "postgresql://yidgkedsjcbodl:6ece5a22b752a4b6d03f58a63a482aac7c8f17af3984636863fbf99b014b3510@ec2-18-214-195-34.compute-1.amazonaws.com:5432/ddutm86ijpvmv4"

class ProductionConfig(Config):
  pass

class DevelopmentConfig(Config):
  DEBUG: True
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SESSION_COOKIE_SECURE = False
  TEMPLATES_AUTO_RELOAD = True
  SECRET_KEY: os.environ.get("SECRET_KEY")
  SESSION_PERMANENT = False
  API_KEY=os.environ.get('API_KEY')
