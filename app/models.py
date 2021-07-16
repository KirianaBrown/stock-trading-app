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
  wallet = db.relationship('Wallet', backref='user', lazy=True)

  def __init__(self, username, password, wallet):
    self.username = username,
    self.password = password,
    self.wallet = wallet,


class Wallet(db.Model):
  __tablename__ = 'wallet'
  id = db.Column(
    db.Integer,
    primary_key=True
  )
  user_id = db.Column(
    db.Integer,
    db.ForeignKey('user.id'),
    nullable = False
  )
  balance = db.Column(
    db.Float
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
