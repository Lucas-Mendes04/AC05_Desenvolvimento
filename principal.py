from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:12345@localhost/cadjogadores'
db = SQLAlchemy(app)


class cadjogadores(db.Model):
    __tablename__ = 'jogadores'
    _id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome = db.Column(db.String(50))
    idade = db.Column(db.Integer())
    posicao = db.Column(db.String(30))
    altura = db.Column(db.Float(5))
    peso = db.Column(db.Float(5))
    def __init__(self, nome, idade, posicao, altura, peso):
        self.nome = nome
        self.idade = idade
        self.posicao = posicao
        self.altura = altura
        self.peso = peso

db.create_all()

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

@app.route("/cadastrar", methods=['GET','POST'])
def cadastrar():
    if request.method =="POST":
        nome = (request.form.get("nome"))
        idade = (request.form.get("idade"))
        posicao = (request.form.get("posicao"))
        altura = (request.form.get("altura"))
        peso = (request.form.get("peso"))
        if nome:
            f = cadjogadores(nome,idade,posicao,altura,peso)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for("cadastro"))

if __name__ == "__main__":
    app.run(debug=True)