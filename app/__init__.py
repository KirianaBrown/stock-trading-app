# App constructor where we init our new app
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
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

# app.config["SECRET_KEY"] = 'TPmi4aLWRbyVq8zu9v82dWYW1'
app.config.update(SECRET_KEY=os.urandom(24))

# init db
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# init session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# import views
from app import views, actions, account

def create_app():
    db.init_app(app)

