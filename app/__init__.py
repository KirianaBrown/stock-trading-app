# App constructor where we init our new app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate
from flask_assets import Environment, Bundle
from .util.assets import bundles

app = Flask(__name__)

assets = Environment(app)
assets.register(bundles)

if app.config['ENV'] == 'production':
  app.config.from_object('config.ProductionConfig')
else:
  app.config.from_object('config.DevelopmentConfig')
  print('Config: Development')

# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@localhost:5432/stock_trader"

# init db
db = SQLAlchemy(app)
migrate = Migrate(app, db)

db.init_app(app)

# import views
from app import views

def create_app():
    db.init_app(app)
