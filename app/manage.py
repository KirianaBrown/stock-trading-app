from flask_migrate import Migrate, MigrateCommand
from app import app, db

migrate = Migrate(app, db)
