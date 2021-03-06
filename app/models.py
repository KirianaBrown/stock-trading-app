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
  portfolio = db.relationship('Portfolio', backref='users')
  portfolioTransactions = db.relationship('PortfolioTransactions', backref='users')

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
  walletTransactions = db.relationship('WalletTransactions', backref='wallet')


class WalletTransactions(db.Model):
  __tablename__ = 'walletTransactions'
  id = db.Column(
    db.Integer,
    primary_key=True
  )
  wallet_id = db.Column(
    db.Integer,
    db.ForeignKey('wallet.id')
  )
  transactionDate = db.Column(
    db.DateTime, 
    default=datetime.utcnow
  )
  transactionType = db.Column(
    db.String(60),
    nullable=False
  )
  amount = db.Column(
    db.Float
  )

# portfolio
class Portfolio(db.Model):
  __tablename__ = "portfolio"
  id = db.Column(
    db.Integer,
    primary_key = True
  )
  user_id = db.Column(
    db.Integer,
    db.ForeignKey('users.id')
  )
  symbol = db.Column(
    db.String(60),
    nullable = False
  )
  name = db.Column(
    db.String(60),
    default = 'NONE'
  )
  quantity = db.Column(
    db.Integer
  )

# portfoliotransactions
# symbol date price quantity type('buy/sell')
class PortfolioTransactions(db.Model):
  __tablename__ = "portfolioTransactions"
  id = db.Column(
    db.Integer,
    primary_key = True
  )
  user_id = db.Column(
    db.Integer,
    db.ForeignKey('users.id')
  )
  symbol = db.Column(
    db.String(60),
    nullable = False
  )
  name = db.Column(
    db.String(60),
    default = 'NONE'
  )
  quantity = db.Column(
    db.Integer(),
    nullable = False
  )
  unitPrice = db.Column(
    db.Float(),
    nullable = False
  )
  transactionDate = db.Column(
    db.DateTime, 
    default=datetime.utcnow
  )
  transactionType = db.Column(
    db.String(60)
  ) 