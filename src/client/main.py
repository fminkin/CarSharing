from flask import Flask, render_template, request

from src.carsharing.user import UserInfo

app = Flask(__name__)


@app.route("/signup", methods=["POST", "GET"])
def signup_page():
    if request.method == "POST":
        user_info = UserInfo()

        print(request.form['email'])
        print(request.form['psw'])
        print(request.form)

    # ImmutableMultiDict([('email', 'huy'), ('psw', '123'), ('psw-repeat', '123')])
    return render_template('signup.html')


@app.route("/", methods=["POST", "GET"])
def index_page():
    if request.method == "POST":
        text = request.form["text"]

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=False)
