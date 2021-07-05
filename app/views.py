import os

from flask.helpers import url_for
from app import app
from flask import Flask, redirect, render_template, request, session, flash, abort
from flask_session import Session
# Werkzeug security
from werkzeug.security import check_password_hash, generate_password_hash
from .models import db, User
# Helper Functions
from .helpers import check_registration_valid


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
    # 1. get form data
    username = request.form.get('username')
    password = request.form.get('password')

    flash(check_registration_valid(username, password))
    return redirect(request.url)
