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

  def __init__(self, username, password):
    self.username = username,
    self.password = password,


class Wallet(db.Model):
  __tablename__ = 'wallet'
  id = db.Column(
    db.Integer,
    primary_key=True
  )
  user_id = db.Column(
    db.Integer,
    nullable = False
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

  def __init__(self, user_id, balance, transactionType):
    self.user_id = user_id,
    self.balance = balance,
    self.transactionType = transactionType
