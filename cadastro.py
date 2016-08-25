# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	Evento = db.Column(db.String(80), unique=True)
	Sobrenome = db.Column(db.String(40), unique=True)
	Email = db.Column(db.String(40), unique=True)
	Login = db.Column(db.String(40), unique=True)
	Senha = db.Column(db.String(40), unique=True)
	Descricao = db.Column(db.String(200), unique=True)
	Pessoas_associadas = db.Column(db.String(200), unique=True)
	Alarme = db.Column(db.String(40), unique=True)

	def __init__(self, Nome, Sobrenome, Email , Login , Senha):
    	   self.Nome = Nome
    	   self.Sobrenome = Sobrenome
    	   self.Email = Email
    	   self.Login = Login
    	   self.Senha = Senha

db.create_all()
    	
@app.route('/create', methods=['GET', 'POST'])
def add_user():
   if request.method == 'POST':
    	Evento = request.form["Evento"]
    	Sobrenome = request.form["Sobrenome"]
    	Email = request.form["Email"]
    	Login = request.form["Login"]
    	Senha = request.form["Senha"]
    	user = User(Evento=Evento, Sobrenome=Sobrenome, Email=Email, Login=Login, Senha=Senha)
    	db.session.add(user)
    	db.session.commit()
    	return " dado inserido"
   return '''



    	<form action="" method="post">
        	<p>Nome: <input type=text name=Evento>
        	<p>Sobrenome: <input type=text name=Sobrenome>
        	<p>Email: <input type=text name=Email>
        	<p>Login: <input type=text name=Login>
        	<p>Senha: <input type=text name=Senha>
        	<p><input type=submit value=Criar>
    	</form>
	'''


if __name__ == "__main__":
	app.run()