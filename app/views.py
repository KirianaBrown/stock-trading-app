import os
import random

from flask.helpers import url_for
from app import app
from flask import Flask, redirect, render_template, request, session, flash, abort, Markup
from flask_session import Session
# Werkzeug security
from werkzeug.security import check_password_hash, generate_password_hash
from .models import db, User
# Helper Functions
from .helpers import check_registration_valid, getListGainers, getListMostActive, getListLosers, formatDollar, formatPercentage, getCryto,getCompanyDetails, getQuote


from dotenv import load_dotenv
load_dotenv()

# Custom filter
app.jinja_env.filters["formatDollar"] = formatDollar
app.jinja_env.filters["formatPercentage"] = formatPercentage

#Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

@app.route("/")
def index():
  session.clear()
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

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
  if request.method == 'GET':
  
    # 1. get most active
    if not session.get('listMostActive'):
      session['listMostActive'] = getListMostActive()
    
    mostActive = session['listMostActive']

    if not session.get('trending'):
      session['trending'] = mostActive[:5]

    trending = session['trending']

    # 2. get spotlight
    if not session.get('spotlightCompany'):
      session['spotlightCompany'] = mostActive[random.randint(0, 9)]

    spotlight = session['spotlightCompany']
    print(spotlight['symbol'])  

    #2b get spotlight company details
    if not session.get('spotlightCompanyDetails'):
      session['spotlightCompanyDetails'] = getCompanyDetails(spotlight['symbol'])

    spotlightCompanyDetails = session['spotlightCompanyDetails']
    
    # 3. get bitcoin
    if not session.get('bitcoin'):
      session['bitcoin'] = getCryto('btcusd') 
    bitcoin = float(session['bitcoin']['price'])

    # 4. get cardona
    if not session.get('litecoin'):
      session['litecoin'] = getCryto('ltcusd') 
    litecoin = float(session['litecoin']['price'])

    # 5. get etherirum
    if not session.get('eth'):
      session['eth'] = getCryto('ethusd')  
    eth = float(session['eth']['price'])

    # 6. get portfolio

    return render_template('/dashboard-copy.html', bitcoin=bitcoin, litecoin=litecoin, eth=eth, trending=trending, spotlight=spotlight, spotlightCompanyDetails=spotlightCompanyDetails)

@app.route('/explore')
def explore():
  # 1. Get most active
  if not session.get('listMostActive'):
    session['listMostActive'] = getListMostActive()
    print('no listMostActive stored in session')
  else:
    print('listMostActive was already stored in the session')
  
  mostActive = session['listMostActive']

  # 2. get spotlight
  if not session.get('spotlightCompany'):
    session['spotlightCompany'] = mostActive[random.randint(0, 9)]

  spotlight = session['spotlightCompany']

  #2b get spotlight company details
  if not session.get('spotlightCompanyDetails'):
    session['spotlightCompanyDetails'] = getCompanyDetails(spotlight['symbol'])

  spotlightCompanyDetails = session['spotlightCompanyDetails']

  # 2. gainers
  if not session.get('listGainers'):
    session['listGainers'] = getListGainers()
    print('no list gainers in session // set now')
  else:
    print('list gainers already in session')

  gainers = session['listGainers']

  # 3. losers
  if not session.get('listLosers'):
    session['listLosers'] = getListLosers()
    print('no list losers in current session // saved now')
  else:
    print('list losers already stored in session')

  losers = session['listLosers']


  print('------------------------------')
  print(f'Active: {mostActive}')
  print(f'spotlight: {spotlight}')
  print(f'spotlightCompanyDetails: {spotlightCompanyDetails}')
  print(f'Gainers: {gainers}')
  print(f'Losers: {losers}')
  print('------------------------------')


  return render_template('/explore.html', mostActive=mostActive, spotlight=spotlight, spotlightCompanyDetails=spotlightCompanyDetails, gainers=gainers, losers=losers)

@app.route('/quote', methods=['GET', 'POST'])
def quote():

  if request.method == 'GET':

     # 1. Get most active
    if not session.get('listMostActive'):
      session['listMostActive'] = getListMostActive()
      print('no listMostActive stored in session')
    else:
      print('listMostActive was already stored in the session')
  
    mostActive = session['listMostActive']

    # 2. get spotlight
    if not session.get('spotlightCompany'):
      session['spotlightCompany'] = mostActive[random.randint(0, 9)]

    spotlight = session['spotlightCompany']

    #2b get spotlight company details
    if not session.get('spotlightCompanyDetails'):
      session['spotlightCompanyDetails'] = getCompanyDetails(spotlight['symbol'])

    spotlightCompanyDetails = session['spotlightCompanyDetails']

    spotlightQuote = getQuote(spotlight['symbol'])
    print(spotlightQuote)
    
    return render_template('/quote.html', spotlight=spotlight, spotlightCompanyDetails=spotlightCompanyDetails, spotlightQuote=spotlightQuote)

@app.route('/portfolio', methods=['GET', 'POST'])
def portfolio():
  if request.method == 'GET':
    return render_template('/portfolio.html')

@app.route('/account', methods=['GET', 'POST'])
def account():
  if request.method == 'GET':
    return render_template('/account.html')


@app.route('/logout')
def logout():
  session.clear()
  return redirect('/')


  