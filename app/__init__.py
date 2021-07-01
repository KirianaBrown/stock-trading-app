# App constructor where we init our new app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment, Bundle
from .util.assets import bundles

app = Flask(__name__)

if app.config['ENV'] == 'production':
  app.config.from_object('config.ProductionConfig')
else:
  app.config.from_object('config.DevelopmentConfig')
  print('Config: Development')

db = SQLAlchemy(app)

assets = Environment(app)
assets.register(bundles)

from app import views

def create_app():
    db.init_app(app)