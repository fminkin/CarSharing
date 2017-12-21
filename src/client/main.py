from flask import Flask, render_template, request

# from src.carsharing import UserInfo

import json
# from src.server.main import Server

import argparse

app = Flask(__name__)

@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        print(request.form['username'])
        print(request.form['password'])
        print(request.files)
        UserInfo(request.form['username'], request.form['password'], 123)
        # server.signup_user_handle(UserInfo)

    return render_template('signup.html')


@app.route("/", methods=["POST", "GET"])
def index_page():
    if request.method == "POST":
        text = request.form["text"]

    return render_template('index.html')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str)

    args = parser.parse_args()
    # server = Server(args)

    with open(args.config) as f:
        config = json.load(f)

    UPLOAD_FOLDER = config["upload_folder"]
    SERVER_ADDRESS = config["server_adress"]
    SERVER_PORT = config["server_port"]
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run(host=SERVER_ADDRESS, port=SERVER_PORT, debug=True)
