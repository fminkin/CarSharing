from flask import Flask, render_template, request, redirect, url_for, g, flash, session


from src.carsharing import UserInfo, Account
from src.carsharing.utils.coordinate import Coordinate
from src.server.server import Server
from src.carsharing.ride.ride import get_charge_rate
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
            print("XXX")
            flash("Wrong password and/or username")
    return render_template('login.html')


@app.route("/messages", methods=["POST", "GET"])
def messages():
    if g.account is None:
        return redirect('/login')
    return render_template('messages.html', messages=server.get_messages_handle(g.account.username))

@app.route("/log_out")
def log_out():
    session["username"] = ""
    return redirect('/index')


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


@app.route("/check_autos", methods=["POST", "GET"])
def check_availible_autos():
    print(g.account)
    if g.account is None:
        return redirect('/login')
    else:
        if request.method == "POST":
            server.check_availible_autos_handle(
                g.account.username, Coordinate(int(request.form["x"]), int(request.form["y"])))
            return render_template("check_messages.html")
        else:
            return render_template("check_autos_form.html")


@app.route("/reserve_auto", methods=["POST", "GET"])
def reserve_auto():
    if g.account is None:
        return redirect('/login')
    else:
        if request.method == "POST":
            server.reserve_auto_handle(g.account.username, request.form["plate"],
                                       get_charge_rate(int(request.form["charge_rate"])))
            return render_template("check_messages.html")
        else:
            return render_template("reserve_auto.html")


@app.route("/start_ride", methods=["POST", "GET"])
def start_ride():
    if g.account is None:
        return redirect('/login')
    else:
        if request.method == "POST":
            server.start_ride_action_handle(g.account.username, [])
            return render_template("check_messages.html")
        else:
            return render_template("start_ride.html")


@app.route("/finish_ride", methods=["POST", "GET"])
def finish_ride():
    if g.account is None:
        return redirect('/login')
    else:
        if request.method == "POST":
            server.finish_ride_action_handle(g.account.username)
            return render_template("check_messages.html")
        else:
            return render_template("finish_ride.html")


if __name__ == "__main__":
    # from src.external.db.db_mock import Reviewer, Automobile
    # from src.carsharing.auto.automobile import EVehicleClass
    # import pickle
    # with open('../external/db/files/reviewers', 'wb') as f:
    #     pickle.dump([None, None], f)
    # with open('../external/db/files/cars', 'wb') as f:
    #     pickle.dump([["Lada", 4, "AA777A777", EVehicleClass.ECONOM],
    #                  ["BMW", 2, "BB666B50", EVehicleClass.COMFORT]], f)

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
