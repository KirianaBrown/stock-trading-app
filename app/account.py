from app import app
from .models import db
from flask.helpers import url_for
from flask import Flask, redirect, render_template, request, session, flash

@app.route('/wallet/<string:action>', methods=['GET', 'POST'])
def wallet(action):
  if request.method == 'POST':
    # 1. get amount from form
    req = request.form
    amount = req.get('amount')

    if not amount:
      return 'No amount provided'

    if action == 'topup':
      return f'topup selected with an amount of {amount}'
    
    if action == 'withdrawal':
      return f'withdrawal selected with an amount of {amount}'

    # 2. get wallet for current user

    # 3. Add value to the wallet

    # 4. Log transaction date (render account page)
    # return render_template('/account.html')

  return 'top up the wallet'


@app.route('/password', methods=['GET', 'POST'])
def password():
  return 'change password'


@app.route('/delete', methods=['GET', 'POST'])
def delete():
  return 'Delete account'