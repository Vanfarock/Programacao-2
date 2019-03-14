from flask import Flask, render_template
import mysql.connector

class Database():
	def __init__(self):
		__host = "localhost"
		__user = "root"
		__password = "root"
		__db = "Pessoas"

		self.con = mysql.connector.connect( host = __host, user = __user, passwd = __password, database = __db)
		self.cursor = self.con.cursor()

		self.cursor.execute("CREATE TABLE IF NOT EXISTS pessoas (nome varchar(255) not null, data_nascimento date not null, cpf varchar(11) primary key)")

	def mostrar_pessoas(self):
		self.cursor.execute("SELECT * FROM pessoas")
		results = self.cursor.fetchall()
		print( results )
		return results

def padronizar_pessoas(pessoas):
	novas_pessoas = []
	for pessoa in pessoas:
		data = str(pessoa[1])
		data_formatada = data[8:10] + "/" + data[5:7] + "/" + data[0:4]
		novas_pessoas.append((pessoa[0], data_formatada, pessoa[2]))
	return novas_pessoas

db = Database()

app = Flask(__name__)

@app.route("/")
def inicio():
	return render_template("index.html")

@app.route("/lista_pessoas")
def lista_pessoas():
	pessoas = db.mostrar_pessoas()
	pessoas = padronizar_pessoas(pessoas)
	#data_nascimento = pessoas[0][1]
	#pessoas[0][1] = padronizar_data_nascimento(data_nascimento)
	return render_template("lista_pessoas.html", data = pessoas, content_type = "application/json")

@app.route("/form_alterar_pessoa")
def form_alterar_pessoa():
	return render_template("form_alterar_pessoa.html")	

@app.route("/form_deletar_pessoa")
def form_deletar_pessoa():
	return render_template("form_deletar_pessoa.html")

@app.route("/form_inserir_pessoa")
def form_inserir_pessoa():
	return render_template("form_inserir_pessoa.html")

app.run(debug=True, host="0.0.0.0")