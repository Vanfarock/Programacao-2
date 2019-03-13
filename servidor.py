from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
	return render_template("index.html")

@app.route("/lista_pessoas")
def lista_pessoas():
	return render_template("lista_pessoas.html")

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