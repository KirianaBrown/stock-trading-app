# App constructor where we init our new app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

if app.config['ENV'] == 'production':
  app.config.from_object('config.ProductionConfig')
else:
  app.config.from_object('config.DevelopmentConfig')
  print('Config: Development')

db = SQLAlchemy(app)

from app import views

def create_app():
    db.init_app(app)