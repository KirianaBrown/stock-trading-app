from app import app
from .models import Portfolio, PortfolioTransactions, db, User, Wallet, WalletTransactions
from flask_session import Session
from flask.helpers import url_for
from flask import Flask, redirect, render_template, request, session, flash
from .helpers import getQuote, login_required

@app.route('/buy', methods=['GET','POST'])
@login_required
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
@login_required
def sell():
  if request.method == 'GET':
    return redirect('/portfolio')
  else:
    # 1. get form data
    req = request.form
    symbol = req.get('symbol')
    quantity = req.get('quantity')

    # 2. get user 
    user = User.query.get_or_404(session['user_id'])

    # 3. get quote
    data = getQuote(symbol)
    price = data['latestPrice']

    # 4. get wallet
    wallet = user.wallet.balance
    total = int(quantity) * float(price)
    
    # 6. calc remainder
    remainder = wallet + total

    return render_template('/confirmation.html', action='sell', symbol=symbol, quantity=quantity, name=data['name'], total=total, price=price, remainder=remainder)


@app.route('/confirmation/<string:action>', methods=['GET', 'POST'])
@login_required
def confirmation(action):
  # take buy/sell/delete action
  user = User.query.get_or_404(session['user_id'])

  if action == 'buy':
    req = request.form

    # 1. get form values
    symbol = req.get('symbol')
    quantity = req.get('quantity')
    price = req.get('price')
    total = req.get('total')

    if not symbol or not quantity or not price or not total:
      flash('There was an error processing this buy, please try again')
      return redirect('/quote')

    # 2. get user
    if not user:
      flash('There was an error accessing your account, please try again later.')
      return redirect('/login')

    # 3. handle wallet transaction
    total = float(total)
    user.wallet.balance -= total
  
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
    # else:
    else:
      portfolios = Portfolio.query.filter_by(user_id = session['user_id']).all()

      symbolExists = False
      itemID = ''

      for item in portfolios:
        if item.symbol == symbol:
          symbolExists = True
          itemID = item.id

      if symbolExists:
        print('Symbol exists - updating quantity')
        # 1. update quantity
        selectedSymbol = Portfolio.query.filter_by(id = itemID).first()
        selectedSymbol.quantity += float(quantity)
        # 2. New transaction
        new_portfolio_transaction = PortfolioTransactions(users=user, symbol=symbol, quantity=quantity, unitPrice=price, transactionType=action)
        # 3. add to db
        db.session.add(new_portfolio_transaction)
      else:
        print('create a new portfolio')
        # 1. create a new portfolio
        new_portfolio = Portfolio(users=user, symbol=symbol, quantity=quantity)
        print('created a new portfolio then')
        db.session.add(new_portfolio)

        # 2. new transaction
        print('create new transaction for buy')
        new_portfolio_transaction = PortfolioTransactions(users=user, symbol=symbol, quantity=quantity, unitPrice=price, transactionType=action)
        print('created new transaction')
        db.session.add(new_portfolio_transaction)

    db.session.commit()

    return redirect('/portfolio') 
  elif action == 'sell':
    # 1. get form details
    req = request.form
    symbol = req.get('symbol')
    quantity = req.get('quantity')
    price = req.get('price')
    name = req.get('name')

    # 2. validate if user owns stock
    print(symbol, quantity, price)

    # 3. if user owns the stock then validate quantity is less than on hand
    if not user.portfolio:
      flash('Error processing this sell, check your details and account and try again')
      return redirect('/sell')

    symbolInPortfolio = False
    portfolioItem = ''

    portfolios = Portfolio.query.filter_by(user_id = user.id).all()

    for item in portfolios:
      if item.symbol == symbol:
        symbolInPortfolio = True
        portfolioItem = item

    # 4. process updating the quantity of the stock 
    if symbolInPortfolio:
      print('symbol in portfolio linked to user')
      if portfolioItem.quantity < float(quantity):
        flash('Error processing this sell, it appears you are trying to sell more shares than you currently own. Please check details and try again.')
        return redirect(request.url)
      else:
        print('able to process bc correct value')
        # 5. record a portfolio transaction
        portfolioItem.quantity -= float(quantity)
        new_portfolio_transaction = PortfolioTransactions(user_id=user.id, symbol=symbol, name=name, quantity=quantity, unitPrice=price, transactionType=action)

        # 6. add total to wallet
        total = int(quantity) * price
        user.wallet.balance += float(total)

        # 7. record a wallet transaction
        wallet_id = user.wallet.id
        new_transaction = WalletTransactions(wallet_id=wallet_id, transactionType=action, amount=total,)

        # 8. commit to db
        db.session.add(new_portfolio_transaction)
        db.session.add(new_transaction)
        db.session.commit()

        flash('Success processing this sell')
        return redirect('/portfolio')

    else:
      flash('Error processing this sell, check your account and try again')
      return redirect('/sell')

  elif action == 'delete':
    # remove db user account
    # render index
    req = request.form
    id = req.get('id')

    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit
    db.session.clear()
    return redirect('/')
  else:
    return redirect(request.url)

