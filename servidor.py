from flask import Flask, render_template
import mysql.connector

# class Database():
# 	def __init__(self):
# 		__host = "localhost"
# 		__user = "root"
# 		__password = "root"
# 		__db = "Pessoas"

# 		self.con = mysql.connector.connect( host = __host, user = __user, passwd = __password, database = __db)
# 		self.cursor = self.con.cursor()

# 		self.cursor.execute("CREATE TABLE IF NOT EXISTS pessoas (nome varchar(255) not null, rua varchar(255) not null, telefone varchar(9) primary key)")

# 	def mostrar_pessoas(self):
# 		self.cursor.execute("SELECT * FROM pessoas")
# 		results = self.cursor.fetchall()
# 		print(results)
# 		return results

# db = Database()

class Pessoa:
	def __init__(self, nome, rua, telefone):
		self.nome = nome
		self.rua = rua
		self.telefone = telefone



app = Flask(__name__)

lista_pessoas = [Pessoa("Luana", "Alex Robe", "991678017")]

@app.route("/")
def inicio():
	return render_template("index.html")

@app.route("/listar_pessoas")
def listar_pessoas():
	return render_template("lista_pessoas.html", info = lista_pessoas)

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