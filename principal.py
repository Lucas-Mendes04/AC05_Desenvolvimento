from flask import Flask
from flask import render_template, request, url_for, redirect


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/pontuacao")
def pontuacao():
    return render_template("pontuacao.html")

@app.route("/time")
def times():
    return render_template("time.html")

@app.route("/jogadores")
def jogadores():
    return render_template("jogadores.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

app.run(debug=True)
