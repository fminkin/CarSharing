from flask import Flask, render_template, request, redirect, url_for, g, flash, session


from src.carsharing import UserInfo, Account
from src.server.server import Server
import argparse
import json

app = Flask(__name__)
app.secret_key = 'some secret key'

@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        user_info = UserInfo(request.form['username'], request.form['password'], None)
        server.signup_user_handle(user_info)
        session['username'] = user_info.username
        return redirect('/index')
    return render_template('signup.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        account = Account(request.form['username'], request.form['password'])
        if server.check_account_handle(account):
            session['username'] = account.username
            print(session['username'])
            return redirect('/index')
        else:
            flash("Wrong password and/or username")
    return render_template('login.html')


@app.route("/messages", methods=["POST", "GET"])
def messages():
    if g.account is None:
        return redirect('/login')
    return render_template('messages.html', messages=server.get_messages_handle(g.account.username))


@app.before_request
def load_account():
    if "username" in session and session["username"]:
        account = Account(session["username"])
    else:
        account = None

    g.account = account


@app.route("/index", methods=["POST", "GET"])
@app.route("/", methods=["POST", "GET"])
def index_page():
    return render_template('index.html')


if __name__ == "__main__":
    from src.carsharing.review.reviewer import Reviewer
    import pickle
    with open('../external/db/files/reviewers', 'wb') as f:
        pickle.dump({"alice": Reviewer(), "bob": Reviewer()}, f)

    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default="config/config.json")
    parser.add_argument('--dbconfig', type=str, default="config/dbconfig.json")
    parser.add_argument('--zones-config', type=str, default="config/zones-config.json")

    args = parser.parse_args()
    server = Server(args)

    with open(args.config) as f:
        config = json.load(f)

    UPLOAD_FOLDER = config["upload_folder"]
    SERVER_ADDRESS = config["server_adress"]
    SERVER_PORT = config["server_port"]
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run(host=SERVER_ADDRESS, port=SERVER_PORT, debug=True)
