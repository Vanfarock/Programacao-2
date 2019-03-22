from flask import Flask, render_template, request

class Pessoa:
	def __init__(self, nome, data_nascimento, cpf):
		self.nome = nome
		self.data_nascimento = data_nascimento
		self.cpf = cpf

def formatar_data(data):
	data = data[8:10] + "/" + data[5:7] + "/" + data[0:4]
	return data

app = Flask(__name__)

pessoas = []

@app.route("/")
def inicio():
	return render_template("index.html")

@app.route("/listar_pessoas")
def listar_pessoas():
	return render_template("lista_pessoas.html", info = pessoas)

@app.route("/form_alterar_pessoa")
def form_alterar_pessoa():
	return render_template("form_alterar_pessoa.html")

@app.route("/form_deletar_pessoa")
def form_deletar_pessoa():
	return render_template("form_deletar_pessoa.html")

@app.route("/form_inserir_pessoa")
def form_inserir_pessoa():
	return render_template("form_inserir_pessoa.html")

@app.route("/cadastrar_pessoa")
def cadastrar_pessoa():
	nome = request.args.get("nome")
	data = request.args.get("data")
	cpf = request.args.get("cpf")
	data = formatar_data(data)
	pessoas.append(Pessoa(nome, data, cpf))
	return render_template("exibir_mensagem.html", pessoa=(nome, data, cpf))

app.run(debug=True, host="0.0.0.0")
