from app import app
from .models import db, User, Wallet
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
    user = User.query.get_or_404(session['user_id'])
    if not user:
      flash('Unable to update your wallet at the moment - please try again later')
      redirect('/account')

    if action == 'topup':
      # 1. get the wallet balance associated with the user
      if not user.wallet:
        # 1. create new wallet
        new_wallet = Wallet(balance=amount, users=user)
        db.session.add(new_wallet)
        db.session.commit()
        print('Created new wallet to the DB')
      else:
        print(user.wallet)
      
      return redirect('/account')
    
    if action == 'withdrawal':
      wallet = 1000
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
    # 1. get form values
    req = request.form
    current = req.get('current')
    new = req.get('new')
    confirm = req.get('confirm')

    # 2. get current users id 

    # 3. get current users password 
    dbPassword = 'saltme'

    # 4. validate
    if not current == dbPassword:
      # flash error message
      return redirect('/account')
    
    if not new == confirm:
      # flash error message
      return redirect('/account')

    if not len(new) >= 8:
      #flash error message
      return redirect('/account')

    # 5. now validated update (salt the password and update in db)
    return f'password wants to be changed from {current} to new {new} which has been confirmed {confirm}'
  else:
    return redirect('/account')

    
@app.route('/delete', methods=['GET', 'POST'])
def delete():
  return render_template('/confirmation.html', action='delete')