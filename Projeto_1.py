# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databaseagenda.db'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	Evento = db.Column(db.String(80), unique=True)
	Data = db.Column(db.String(40), unique=True)
	Horario_do_Inicio = db.Column(db.String(40), unique=True)
	Horario_do_Termino = db.Column(db.String(40), unique=True)
	Endereco = db.Column(db.String(40), unique=True)
	Descricao = db.Column(db.String(200), unique=True)
	Pessoas_associadas = db.Column(db.String(200), unique=True)
	Alarme = db.Column(db.String(40), unique=True)

	def __init__(self, Evento, Data, Horario_do_Inicio, Horario_do_Termino, Endereco, Descricao, Pessoas_associadas, Alarme):
    	   self.Evento = Evento
    	   self.Data = Data
    	   self.Horario_do_Inicio = Horario_do_Inicio
    	   self.Horario_do_Termino = Horario_do_Termino
    	   self.Endereco = Endereco
    	   self.Descricao = Descricao
    	   self.Pessoas_associadas = Pessoas_associadas
    	   self.Alarme = Alarme

@app.route("/", methods=['GET' , 'POST'])
def product():
    productId = request.args.get('Dia')
    return add_user()


def add_user():
   if request.method == 'POST':
    	Evento = request.form["Evento"]
    	Data = request.form["Data"]
    	Horario_do_Inicio = request.form["Horario_do_Inicio"]
    	Horario_do_Termino = request.form["Horario_do_Termino"]
    	Endereco = request.form["Endereco"]
    	Descricao = request.form["Descricao"]
    	Pessoas_associadas = request.form["Pessoas_associadas"]
    	Alarme = request.form["Alarme"]
    	user = User(Evento=Evento, Data=Data, Horario_do_Inicio=Horario_do_Inicio, Horario_do_Termino=Horario_do_Termino, Endereco=Endereco, Descricao=Descricao, Pessoas_associadas=Pessoas_associadas, Alarme=Alarme)
    	db.session.add(user)
    	db.session.commit()
    	return " dado inserido"
   return render_template("evento.html")

@app.route('/list')
def list_user():
	users = User.query.all()
	return render_template('list.html',users=users)
	
db.create_all()

if __name__ == "__main__":
	app.run()