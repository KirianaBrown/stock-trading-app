from . import app, db
from datetime import datetime

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(
    db.Integer,
    primary_key=True
  )
  username = db.Column(
    db.String(64),
    nullable=False,
    unique=True
  )
  password = db.Column(
    db.Text,
    nullable=False
  )
  wallet = db.relationship('Wallet', backref='users', uselist=False)

class Wallet(db.Model):
  __tablename__ = 'wallet'
  id = db.Column(
    db.Integer,
    primary_key=True
  )
  user_id = db.Column(
    db.Integer,
    db.ForeignKey('users.id')
  )
  balance = db.Column(
    db.Float,
    default=0.00,
  )
  transactionDate = db.Column(
    db.DateTime, 
    default=datetime.utcnow
  )
  transactionType = db.Column(
    db.String(60),
    nullable=False
  )
