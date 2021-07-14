from flask.helpers import url_for
from app import app
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

    # 2. get user wallet balance
    wallet = 1000;

    # 3. get latest price
    data = getQuote(stock)
    price = data['latestPrice']

    # 4. calc total $ required for purchase
    total = float(quantity) * float(price)

    # 5. compare wallet balance and total $ of purchase
    if wallet < total:
      print('not enough funds to purchase')

    remainder = (wallet - total)

    # 6. render results to ui for user confirmation
    return render_template('/confirmation.html', action='buy', symbol=stock, name=data['name'], total=total, price=price, remainder=remainder)

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

    return render_template('/confirmation.html', action='sell', symbol=stock, name=data['name'], total=total, price=price, remainder=remainder)


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
    name = req.get('name')
    return f'confirmation from a buy form with a name value of {name}'  
  elif action == 'sell':
    return f'confirmation to sell a stock'
  else:
    return 'confirmation has been hit without a link'

