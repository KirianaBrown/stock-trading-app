import os
from app import app

from dotenv import load_dotenv
load_dotenv()

@app.route("/")
def index():
  secret = os.environ.get("SECRET")
  return f'hello world {secret}!!!!!!!'