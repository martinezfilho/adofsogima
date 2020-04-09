from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/marzyu")
def marzyu():
    return render_template("marzyu.html")


@app.route("/hitek")
def hitek():
    return render_template("hitek.html")


@app.route("/lad")
def lad():
    return render_template("lad.html")


@app.route("/felipos")
def felipos():
    return render_template("felipos.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)
