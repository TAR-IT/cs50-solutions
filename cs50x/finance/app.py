import os

from cs50 import SQL
from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    # Get the user's portfolio data
    user_id = session["user_id"]
    portfolio_data = db.execute(
        "SELECT symbol, name, SUM(shares) as shares, price FROM purchases WHERE user_id = :user_id GROUP BY symbol HAVING shares > 0",
        user_id=user_id,
    )

    # Get the user's cash balance
    cash_balance = db.execute(
        "SELECT cash FROM users WHERE id = :user_id", user_id=user_id
    )[0]["cash"]

    # Calculate the total value of each stock holding
    for stock in portfolio_data:
        stock["total_value"] = stock["shares"] * stock["price"]

    # Calculate the grand total (sum of stocks' total value plus cash)
    grand_total = cash_balance + sum(stock["total_value"] for stock in portfolio_data)

    # Render the index page with the user's portfolio data
    return render_template(
        "index.html",
        stocks=portfolio_data,
        cash_balance=cash_balance,
        grand_total=grand_total,
    )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        # Get stock symbol and number of shares from the form
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Validate user input
        if not symbol or not shares.isdigit() or int(shares) <= 0:
            return apology("Invalid input")

        # Look up the stock quote using the lookup function
        quote_data = lookup(symbol)

        # Check if the stock symbol is valid
        if quote_data is None:
            return apology("Invalid stock symbol")

        # Calculate the total cost of the purchase
        total_cost = quote_data["price"] * int(shares)

        # Get the user's cash balance from the database
        user_cash = db.execute(
            "SELECT cash FROM users WHERE id = :user_id", user_id=session["user_id"]
        )[0]["cash"]

        # Check if the user can afford the purchase
        if total_cost > user_cash:
            return apology("Insufficient funds")

        # Update the user's cash balance
        new_cash_balance = user_cash - total_cost
        db.execute(
            "UPDATE users SET cash = :new_cash_balance WHERE id = :user_id",
            new_cash_balance=new_cash_balance,
            user_id=session["user_id"],
        )

        # Insert the purchase into the database
        db.execute(
            "INSERT INTO purchases (user_id, symbol, shares, price) VALUES (:user_id, :symbol, :shares, :price)",
            user_id=session["user_id"],
            symbol=symbol,
            shares=int(shares),
            price=quote_data["price"],
        )

        # Redirect to the home page
        return redirect("/")

    # Render the stock buying form for GET requests
    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    # Get the user's transaction history
    user_id = session["user_id"]
    transactions = db.execute(
        "SELECT CASE WHEN shares < 0 THEN 'Sell' ELSE 'Buy' END as type, symbol, ABS(shares) as shares, price, timestamp FROM purchases WHERE user_id = :user_id ORDER BY timestamp DESC",
        user_id=user_id,
    )

    # Render the transaction history page
    return render_template("history.html", transactions=transactions)


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
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
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
    if request.method == "POST":
        # Get stock symbol from the form
        symbol = request.form.get("symbol")

        # Validate stock symbol
        if not symbol:
            return apology("Invalid stock symbol")

        # Look up the stock quote using the lookup function
        quote_data = lookup(symbol)

        # Check if the stock symbol is valid
        if quote_data is None:
            return apology("Invalid stock symbol")

        # Render a template to display the stock quote
        return render_template("quoted.html", quote=quote_data)

    # Render the stock quoting form for GET requests
    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Get user input from the registration form
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Validate user input
        if not username or not password or password != confirmation:
            return apology("Invalid input")

        # Check for duplicate username
        existing_user = db.execute(
            "SELECT * FROM users WHERE username = :username", username=username
        )
        if existing_user:
            return apology("Username already exists, please choose another one")

        # Hash the password before storing it in the database
        hashed_password = generate_password_hash(password)

        # Insert the new user into the database
        db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)",
            username,
            hashed_password,
        )

        # Redirect to the home page or login page
        return redirect("/")

    # Render the registration form for GET requests
    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "POST":
        # Get stock symbol and number of shares from the form
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Validate user input
        if not symbol or not shares.isdigit() or int(shares) <= 0:
            return apology("Invalid input")

        # Look up the stock quote using the lookup function
        quote_data = lookup(symbol)

        # Check if the stock symbol is valid
        if quote_data is None:
            return apology("Invalid stock symbol")

        # Get the user's current holdings of the selected stock
        user_id = session["user_id"]
        user_holdings = db.execute(
            "SELECT SUM(shares) as total_shares FROM purchases WHERE user_id = :user_id AND symbol = :symbol GROUP BY symbol",
            user_id=user_id,
            symbol=symbol,
        )

        # Check if the user owns enough shares to sell
        if user_holdings and int(shares) <= user_holdings[0]["total_shares"]:
            # Calculate the total value of the sale
            total_sale_value = quote_data["price"] * int(shares)

            # Update the user's cash balance
            db.execute(
                "UPDATE users SET cash = cash + :total_sale_value WHERE id = :user_id",
                total_sale_value=total_sale_value,
                user_id=user_id,
            )

            # Insert the sale into the database with a negative shares value
            db.execute(
                "INSERT INTO purchases (user_id, symbol, shares, price) VALUES (:user_id, :symbol, :shares, :price)",
                user_id=user_id,
                symbol=symbol,
                shares=-int(shares),
                price=quote_data["price"],
            )

            # Redirect to the home page
            return redirect("/")
        else:
            return apology("Insufficient shares to sell")

    # Get the user's available stocks for selling
    user_id = session["user_id"]
    user_stocks = db.execute(
        "SELECT symbol FROM purchases WHERE user_id = :user_id GROUP BY symbol HAVING SUM(shares) > 0",
        user_id=user_id,
    )

    # Render the stock selling form for GET requests
    return render_template("sell.html", stocks=user_stocks)


@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    if request.method == "POST":
        # Get the amount of cash to add from the form
        amount = request.form.get("amount")

        # Validate user input
        if not amount or float(amount) <= 0:
            return apology("Invalid input")

        # Update the user's cash balance
        user_id = session["user_id"]
        db.execute(
            "UPDATE users SET cash = cash + :amount WHERE id = :user_id",
            amount=float(amount),
            user_id=user_id,
        )

        # Redirect to the home page
        return redirect("/")

    # Render the add cash form for GET requests
    return render_template("add_cash.html")
