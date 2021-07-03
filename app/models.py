from . import app, db

class Test(db.Model):
  __tablename__ = 'testing'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), unique=True, nullable=False)
  hash = db.Column(db.Text, nullable=False)
  balance = db.Column(db.Integer)

  def __init__(self, username, hash, balance):
    self.username = username
    self.hash = hash
    self.balance = balance