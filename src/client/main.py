from flask import Flask, render_template, request

import json
from src.carsharing.user import UserInfo
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--config', type=str)

args = parser.parse_args()

with open(args.config) as f:
    config = json.load(f)

UPLOAD_FOLDER = config["upload_folder"]
SERVER_ADDRESS = config["server_adress"]

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/signup", methods=["POST", "GET"])
def signup_page():
    if request.method == "POST":
        print(request.form['username'])
        print(request.form['password'])
        # print(request.files)
        for i in request.files.getlist('file'):
            print(i)
        user_info = UserInfo(request.form['username'], request.form['password'], 123)
    return render_template('signup.html')


@app.route("/", methods=["POST", "GET"])
def index_page():
    if request.method == "POST":
        text = request.form["text"]

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9889, debug=False)
