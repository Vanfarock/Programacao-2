from flask import Flask, render_template, request

class Pessoa:
	def __init__(self, nome, endereco, cpf):
		self.nome = nome
		self.endereco = endereco
		self.cpf = cpf

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
	nome = request.args.get("nome")
	endereco = request.args.get("endereco")
	cpf = request.args.get("cpf")
	return render_template("form_alterar_pessoa.html", dados=(nome, endereco, cpf))

@app.route("/excluir_pessoa")
def form_deletar_pessoa():
	cpf = request.args.get("cpf")
	achou = None
	for p in pessoas:
		if p.cpf == cpf:
			achou = p
			break
	if achou != None:
		pessoas.remove(achou)
		return render_template("exibir_mensagem.html", resultado=str(achou.nome) + " foi excluido com sucesso!")

@app.route("/form_inserir_pessoa")
def form_inserir_pessoa():
	return render_template("form_inserir_pessoa.html")

@app.route("/cadastrar_pessoa")
def cadastrar_pessoa():
	nome = request.args.get("nome")
	endereco = request.args.get("endereco")
	cpf = request.args.get("cpf")
	pessoas.append(Pessoa(nome, endereco, cpf))
	msg = "Seu nome é " + str(nome) + ", você mora na " + str(endereco) + " e seu cpf é " + str(cpf)
	return render_template("exibir_mensagem.html", resultado=msg)

app.run(debug=True, host="0.0.0.0")
