from flask import Flask, render_template
import requests
import os.path

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
    save_path = r"static/images"
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, save_path)
    url = "https://api.nasa.gov/planetary/apod"
    key = "?api_key=dtJInnbvOKDr3u16EZe9C6c2XOguzyWXduZgcMe9"
    request = requests.get(url + key)
    if request.status_code == 200:
        dados = request.json()
        hdimage = dados['hdurl']
        # TODO title = dados['title']
        date = dados['date']

    # Salvando a imagem
    request_img = requests.get(hdimage)
    name_of_file = date
    complete_path = os.path.join(path, name_of_file + '.jpg')

    with open(complete_path, "wb") as file:
        file.write(request_img.content)
    file.close()
    return render_template("lad.html")


@app.route("/felipos")
def felipos():
    return render_template("felipos.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)
