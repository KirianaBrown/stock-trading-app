from app import app
from .models import Portfolio, PortfolioTransactions, db, User, Wallet, WalletTransactions
from flask_session import Session
from flask.helpers import url_for
from flask import Flask, redirect, render_template, request, session, flash
from .helpers import getQuote

@app.route('/buy', methods=['GET','POST'])
def buy():
  if request.method == 'GET':
    return redirect(request.url)
  else:
    req = request.form
    # 1. get form data
    stock = request.form.get('symbol')
    quantity = request.form.get('quantity')

    if not stock or not quantity:
      flash('Unable to execute buy right now - missing stock and/or quantity. Please try again!')
      redirect('/quote')

    print(f'stock: {stock}')
    print(f'quantity: {quantity}')

    # 2. get user wallet balance
    user = User.query.get_or_404(session['user_id'])
    if not user:
      flash('Unable to execute buy right now, please try again later')
      return redirect(request.url)

    if not user.wallet:
      flash('Missing wallet balance, please top up account before making this buy request.')
      return redirect('/account')

    wallet = user.wallet.balance

    print(f'wallet: {wallet}')

    # 3. get latest price
    data = getQuote(stock)
    price = data['latestPrice']

    print(f'price: {price}')

    # 4. calc total $ required for purchase
    total = float(quantity) * float(price)

    print(f'total: {total}')

    # 5. compare wallet balance and total $ of purchase
    if wallet <= total:
      flash('Missing funds, please top up your account before executing this buy')
      return redirect('/account')

    remainder = (wallet - total)

    # 6. render results to ui for user confirmation
    return render_template('/confirmation.html', action='buy', symbol=stock, quantity=quantity, name=data['name'], total=total, price=price, remainder=remainder)

@app.route('/sell', methods=['POST', 'GET'])
def sell():
  if request.method == 'GET':
    return redirect(request.url)
  else:
    # 1. get form data
    req = request.form
    stock = req.get('symbol')
    quantity = req.get('quantity')

    # 2. get latest price of stock
    print(stock)

    data = getQuote(stock)
    price = data['latestPrice']

    # 3. total
    total = float(price) * float(quantity)

    # 4. get users wallet
    wallet = 1999

    # 5. calc remainder
    remainder = wallet + total

    return render_template('/confirmation.html', action='sell', symbol=stock, quantity=quantity, name=data['name'], total=total, price=price, remainder=remainder)


@app.route('/confirmation/<string:action>', methods=['GET', 'POST'])
def confirmation(action):
   # confirm should be able to receive both a sell and a buy action and perform differently depending if sell x if buy do y

  # should be a request by a user to confirm the purchase provided
  # if yes then 

  # 1. add stock transaction to users portfolio

  # 2. adjust wallet appropriately

  # 3. return confirmation and render portfolio to show updated transaction details
  if action == 'buy':
    req = request.form

    # 1. get form values
    symbol = req.get('symbol')
    quantity = req.get('quantity')
    price = req.get('price')
    total = req.get('total')

    # 2. get user
    user = User.query.get_or_404(session['user_id'])
    print(f'user: {user.username}')

    # 3. handle wallet transaction
    user.wallet.balance -= float(total)
  
    new_transaction = WalletTransactions(wallet=user.wallet, amount=total, transactionType=action)   
    db.session.add(new_transaction)

    # 4. portfolio
    if not user.portfolio:
      print('no portfolio linked to this user')
      # 1. create new portfolio
      new_portfolio = Portfolio(users=user, symbol=symbol, quantity=quantity)
      print('created a new portfolio then')
      db.session.add(new_portfolio)

      # 2. new transaction
      print('create new transaction for buy')
      new_portfolio_transaction = PortfolioTransactions(users=user, symbol=symbol, quantity=quantity, unitPrice=price, transactionType=action)
      print('created new transaction')
      db.session.add(new_portfolio_transaction)

      # 3. commit to db records
      db.session.commit()
    else:
      print('user already has a portfolio linked')

    db.session.commit()

    return 'Success stock has been purchase and added to portfolio'  
  elif action == 'sell':
    return f'confirmation to sell a stock'
  elif action == 'delete':
    # remove db user account
    # render index
    return f'confirmation to delete account'
  else:
    return 'confirmation has been hit without a link'

