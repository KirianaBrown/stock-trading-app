from . import app, db

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
  wallet = db.Column(
    db.Float
  )

  def __init__(self, username, password, wallet):
    self.username = username,
    self.password = password,
    self.wallet = wallet
