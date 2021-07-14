from app import app
from .models import db
from flask_session import Session
# Werkzeug security
from werkzeug.security import check_password_hash, generate_password_hash
from flask.helpers import url_for
from flask import Flask, redirect, render_template, request, session, flash

@app.route('/wallet/<string:action>', methods=['GET', 'POST'])
def wallet(action):
  if request.method == 'POST':
    # 1. get amount from form
    req = request.form
    amount = float(req.get('amount'))

    if not amount:
      return 'No amount provided'

    # 2. get wallet for current user
    wallet = 1000

    if action == 'topup':
      # add value to the wallet
      balance = wallet + amount
      # render the account page (GET) which will add the transaction and flash('success message')
      return f'topup selected with an amount of {amount} to leave a new wallet balance of {balance}'
    
    if action == 'withdrawal':
      # validate withdrawal value does not exceed wallet
      if amount < wallet:
        # update balance to show withdrawal
        balance = wallet - amount
        # render account page(GET) which will add transaction and flash success message
        return f'withdrawal selected with an amount of {amount} from wallet {wallet} leaving a balance of {balance}'
      else:
        return f'Unable to withdrawal value of {amount} due to it exceeding current wallet balance of {wallet}'

  return redirect('/account')


@app.route('/password', methods=['GET', 'POST'])
def password():
  if request.method == 'POST':
    return 'password wants to be changed'
  else:
    return redirect('/account')

    


@app.route('/delete', methods=['GET', 'POST'])
def delete():
  return 'Delete account'