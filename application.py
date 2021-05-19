import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    if request.method == "GET":
        # Get the stocks for the user
        rows = db.execute("SELECT symbol,quantity FROM portfolio WHERE user_id = ? AND quantity > 0", session["user_id"])
        # [{'symbol':'NFLX', 'quantity':7}]
        symbol_rows = db.execute("SELECT symbol FROM portfolio WHERE user_id = ?", session["user_id"])

        DATA = []
        SYMBOLS = []
        # [{'name': 'netflix', 'price': 554, 'symbol': 'NFLX'}]

        # TODO: get the symbols name and price from lookup
        for symbol in symbol_rows:
            # get the name and price
            value = lookup(symbol['symbol'])
            DATA.append(value)
            SYMBOLS.append(symbol['symbol'])

        # Get the quantity of each symbol and add to names dic
        for sym in range(len(SYMBOLS)):
            portfolio_data = db.execute("SELECT quantity FROM portfolio WHERE symbol = ? ", SYMBOLS[sym])
            DATA[sym]["quantity"] = portfolio_data[0]['quantity']

        # [{'name': 'netflix', 'price': 554, 'symbol': 'NFLX', 'quantity': 10}]

        total_cost_value = 0

        # Calc Value (no_stocks * price)
        for item in range(len(DATA)):
            qty = (DATA[item]['quantity'])
            cost = (DATA[item]['price'])
            value = qty * cost
            total_cost_value += value
            # DATA[item]['value'] = round(value,2)
            DATA[item]['value'] = value

        # Remove those with quantity = 0
        for i in range(len(DATA)):
            if int(DATA[i]['quantity']) == 0:
                del DATA[i]
                break

        # Get cash value of user
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])

        cash_value = (cash[0]["cash"])
        total_net_value = cash_value + total_cost_value

        return render_template("index.html", rows=DATA, cash=cash_value, total_net_value=total_net_value)
    else:
        return apology("Oops missing link", 404)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    """
        1. get display /buy.html (if valid symbol)
        2. post get the symbol and share qty (if valid ie positive)
        3. get the symbol from lookup to get the share price
        4. get the account balance from user
        5. if account balance is > that share # * share price then
        add that value to a new table in finance and deduct the
        value from their account balance
    """
    if request.method == "GET":
        return render_template("buy.html")
    else:
        # 1. Get values from form
        symbol = request.form.get("symbol")
        no_shares = request.form.get("shares")

        # 2. Err check to ensure values inputted.
        if not symbol:
            return apology("Require symbol", 400)
        elif not no_shares:
            return apology("Number of shares to purchase required", 400)
        elif no_shares.isnumeric() == False:
            return apology("Please input a valid number")
        elif int(no_shares) <= 0:
            return apology("Number of shares must be a positive", 400)
        elif not float(no_shares).is_integer():
            return apology("Number of shares must be a whole positive", 400)

        no_shares = int(no_shares)

        # 3. Get current share price
        current_share_data = lookup(symbol)
        if not current_share_data:
            return apology("OOPS sorry we are unable to process that request", 400)

        current_share_price = current_share_data['price']
        # print(current_share_price)

        # 4. total price of shares
        total_price_of_shares = round(float(no_shares) * current_share_price, 2)
        total_price_of_shares = float(no_shares) * current_share_price

        # . TODO: get current users account balance
        rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])

        cash_value = (rows[0]["cash"])

        # . TODO: insert new purchase into table
        if cash_value > total_price_of_shares:
            # Insert into transactions
            db.execute("INSERT INTO transactions (quantity, symbol, user_id, price, date) VALUES(?,?,?,?, current_timestamp)",
                       no_shares, symbol, session["user_id"], total_price_of_shares)

            # Insert into add to portfolio
            # 1. get symbol if sym then update else insert
            symbol_exists = db.execute("SELECT symbol FROM portfolio WHERE user_id  = ? AND symbol = ?",
                                       session["user_id"], symbol)

            if len(symbol_exists) == 0:
                # ie none therefore insert new into table
                db.execute("INSERT INTO portfolio (user_id, symbol, quantity) VALUES (?,?,?)",
                           session["user_id"], symbol, no_shares)
            else:
                # update quantity of that symbol
                qty = db.execute("SELECT quantity FROM portfolio WHERE symbol = ?", symbol)

                qty_value = float(qty[0]['quantity']) + float(no_shares)

                db.execute("UPDATE portfolio SET quantity = ? WHERE symbol = ? AND user_id = ?",
                           qty_value, symbol, session["user_id"])

            # Update current users account balance
            updated_cash = cash_value - total_price_of_shares
            db.execute("UPDATE users SET cash = ? WHERE id = ?", updated_cash, session["user_id"])

            # Redirect to / - to render users account details
            flash('Successfully Purchased Stock')
            return redirect("/")
        else:
            return apology("OOPS you have insufficient funds to make this purchase")

    return apology("TODO")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    rows = db.execute("SELECT * FROM transactions WHERE user_id = ?", session['user_id'])
    # print(history)
    return render_template('history.html', rows=rows)
    # return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    else:
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Please request quote", 400)
        else:
            response = lookup(symbol)
            if not response:
                return apology("Error processing your request", 400)
            else:
                return render_template("quoted.html", data=response)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == 'GET':
        return render_template("register.html")
    else:
        # POST get data from form and validate
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # ERROR CHECKING
        # Validate individual inputs return statements
        if not username:
            return apology("Username is required", 400)
        elif not password:
            return apology("Password is required", 400)
        elif not confirmation:
            return apology("Please confirm password", 400)
        elif password != confirmation:
            return apology("Oops check your password confirmation", 400)

        if username:
            # CHECK IF VALID IE NOT ALREADY IN DB
            valid_username = db.execute("SELECT * FROM users WHERE username = ?", username)

        if len(valid_username) != 0:
            return apology("Username already exists", 400)

        # Generate a hashed password based the fn
        hashpassword = generate_password_hash(password)
        print(hashpassword)

        # insert into finance users table username & hash
        db.execute("INSERT INTO users (username, hash) VALUES(?,?)", username, hashpassword)

        # redirect to login
        return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == 'GET':
        # get the list of stocks for the user and pass them in
        STOCKS = db.execute("SELECT symbol FROM portfolio WHERE user_id = ?", session["user_id"])

        return render_template("sell.html", stocks=STOCKS)
    else:
        symbol = request.form.get('symbol')
        no_to_sell = int(request.form.get('shares'))
        qty_owned = db.execute('SELECT quantity FROM portfolio WHERE user_id = ? AND symbol = ?', session['user_id'], symbol)

        if not symbol or not no_to_sell:
            return apology("Please select a share and input a quantity to sell", 400)
        elif qty_owned[0]['quantity'] < no_to_sell:
            return apology("Not enough shares to sell", 400)
        else:
            # 1. get lookup price
            stock_details = lookup(symbol)

            # 2. add value to cash
            cash = db.execute('SELECT cash FROM users WHERE id = ?', session['user_id'])
            sell_value = no_to_sell * stock_details['price']
            update_value = cash[0]['cash'] + sell_value

            db.execute('UPDATE users SET cash = ? WHERE id = ?', update_value, session['user_id'])

            # 3. add new transaction
            qty = -no_to_sell
            db.execute("INSERT INTO transactions (quantity, symbol, user_id, price, date) VALUES(?,?,?,?, current_timestamp)",
                       qty, symbol, session["user_id"], sell_value)

            # 4. rm portfolio value
            qty_value = qty_owned[0]['quantity'] - no_to_sell

            db.execute('UPDATE portfolio SET quantity = ? WHERE symbol = ? AND user_id = ?', qty_value, symbol, session['user_id'])

            # 5. render index
            flash('Successfully Sold')
            return redirect("/")

    return apology("Error")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
