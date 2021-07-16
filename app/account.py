from app import app
from .models import db, User, Wallet, WalletTransactions
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

        # 2. create new transaction
        new_transaction = WalletTransactions(wallet=new_wallet, amount=amount, transactionType='topup')
        db.session.add(new_transaction)
        db.session.commit()

      else:
        user.wallet.balance += float(amount)
        new_transaction = WalletTransactions(wallet=user.wallet, amount=amount, transactionType='topup')
        db.session.add(new_transaction)
        db.session.commit()

        flash('Success! Your wallet has been updated')
   
      return redirect('/account')
    
    if action == 'withdrawal':
      if not user.wallet:
        flash('Unable to locate your wallet at the moment')
        return redirect('/account')

      wallet = user.wallet.balance
      # validate withdrawal value does not exceed wallet
      if amount <= wallet:
        # update balance to show withdrawal
        balance = wallet - float(amount)
        user.wallet.balance = balance

        new_transaction = WalletTransactions(wallet=user.wallet, amount=-amount, transactionType='withdrawl')
        db.session.add(new_transaction)

        db.session.commit()
        return redirect('/account')

      else:
        flash('Unable to withdraw those funds as the amount exceeds your wallet balance')
        return redirect('/account')

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