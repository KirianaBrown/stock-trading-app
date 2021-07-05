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
    username = request.form.get('username').lower()
    password = request.form.get('password')
    confirmation = request.form.get('confirmation')

    # 2. init validation & generate a flash message
    flash_message = check_registration_valid(username,password, confirmation)
    if flash_message:
      flash(flash_message)
      return redirect(request.url)

    # 3. Check if username already exists in DB
    if db.session.query(User).filter(User.username == username).count() == 1:
      flash('Oops username is already taken please try again')
      return redirect(request.url)
    
    # 4. hash password
    hash = generate_password_hash(password, salt_length=16)

    # 4. Create new user in the db
    new_user = User(username=username, password=hash)

    try:
      db.session.add(new_user)
      db.session.commit()
      flash('Successfully Registered')
      return redirect('/')
    except:
      flash('Server error adding new user to DB')
      return redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    session.clear()
    return render_template('/login.html')
  else:
    # 1. get form data
    username = request.form.get('username').lower()
    password = request.form.get('password')

    # 2. validate
    flash_message = check_registration_valid(username,password)
    if flash_message:
      flash(flash_message)
      return redirect(request.url)

    # 3. check user from DB
    user = User.query.filter_by(username=username).first()
    if not user:
      flash('Oops please check your username and try again')
      return redirect(request.url)
    
    if not check_password_hash(user.password, password):
      flash('Oops wrong password - please try again')
      return redirect(request.url)
    
    session['user_id'] = user.id
    session['username'] = user.username

    print('successfully logged in - all credentials match!')
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
  return render_template('/dashboard.html')

@app.route('/logout')
def logout():
  session.clear()
  return redirect('/')


  