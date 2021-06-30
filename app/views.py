import os
from app import app

from dotenv import load_dotenv
load_dotenv()

@app.route("/")
def index():
  return f'hello world - testing link'