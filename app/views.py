import os
from app import app
from flask import Flask, render_template, request
from .models import db, User

from dotenv import load_dotenv
load_dotenv()

# Make sure API key is set
# if not os.environ.get("API_KEY"):
#     raise RuntimeError("API_KEY not set")

@app.route("/")
def index():
  return render_template('/index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'GET':
    return render_template('/register.html')
  else:
    return 'POST register'
