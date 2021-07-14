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

    return f'A buy form has been submitted for stock: {stock} for a quantity of {quantity} at a price of {price} with a wallet value of {wallet} leaving a remainder of {remainder}'


@app.route('/confirmation', methods=['GET', 'POST'])
def confirmation():
  # confirm should be able to receive both a sell and a buy action and perform differently depending if sell x if buy do y

  # should be a request by a user to confirm the purchase provided
  # if yes then 

  # 1. add stock transaction to users portfolio

  # 2. adjust wallet appropriately

  # 3. return confirmation and render portfolio to show updated transaction details

  return render_template('/confirmation.html')
