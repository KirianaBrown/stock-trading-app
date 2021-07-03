import os
from app import app
from flask import Flask, render_template

from dotenv import load_dotenv
load_dotenv()

# Make sure API key is set
# if not os.environ.get("API_KEY"):
#     raise RuntimeError("API_KEY not set")

@app.route("/")
def index():
  database = os.environ.get('DATABASE_URL')
  return f'db: {database}'
