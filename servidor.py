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

	def mostrar_pessoas(self):
		self.cursor.execute("SELECT * FROM pessoas")
		results = self.cursor.fetchall()
		return results

db = Database()

app = Flask(__name__)

@app.route("/")
def inicio():
	return render_template("index.html")

@app.route("/lista_pessoas")
def lista_pessoas():
	pessoas = db.mostrar_pessoas()
	return render_template("lista_pessoas.html", result = pessoas, content_type = "application/json")

@app.route("/form_alterar_pessoa")
def form_alterar_pessoa():
	return render_template("form_alterar_pessoa.html")	

@app.route("/form_deletar_pessoa")
def form_deletar_pessoa():
	return render_template("form_deletar_pessoa.html")

@app.route("/form_inserir_pessoa")
def form_inserir_pessoa():
	return render_template("form_inserir_pessoa.html")

app.run(debug=True)