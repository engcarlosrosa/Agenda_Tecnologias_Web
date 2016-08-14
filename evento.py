
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
 
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

@app.route('/create', methods=['GET', 'POST'])
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
   return '''
    	<form action="" method="post">
        	<p>Evento: <input type=text name=Evento>
        	<p>Data: <input type=text name=Data>
        	<p>Horário do Início: <input type=text name=Horario_do_Inicio>
        	<p>Horário do Término: <input type=text name=Horario_do_Termino>
        	<p>Endereço: <input type=text name=Endereco>
        	<p>Descrição: <input type=text name=Descricao>
        	<p>Pessoas associadas: <input type=text name=Pessoas_associadas>
        	<p>Alarme: <input type=text name=Alarme>
        	<p><input type=submit value=Criar>
    	</form>
	'''


db.create_all()
 
if __name__ == "__main__":
	app.run()