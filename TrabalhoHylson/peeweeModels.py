from peewee import *

arq = "lojaJogos.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
	class Meta():
		database = db

class ProdutoraJogos(BaseModel):
	nome = CharField()
	cnpj = CharField(primary_key=True)

class Fornecedor(BaseModel):
	nome = CharField()
	cnpj = CharField(primary_key=True)

class Plataforma(BaseModel):
	nome = CharField()

class Jogo(BaseModel):
	nome = CharField()
	preco = FloatField()
	lancamento = DateField()
	classificacaoIndicativa = IntegerField()
	fornecedor = ForeignKeyField(Fornecedor)
	produtora = ForeignKeyField(ProdutoraJogos)
	plataforma = ForeignKeyField(Plataforma)

class Cliente(BaseModel):
	nome = CharField()
	cpf = CharField(primary_key=True)
	dataNascimento = DateField()

class Funcionario(BaseModel):
	nome = CharField()
	cpf = CharField(primary_key=True)
	dataNascimento = DateField()
	dataVinculoEmpresa = DateField()
	salario = FloatField()

class TicketsDesconto(BaseModel):
	valor = FloatField()

class TipoPerifericos(BaseModel):
	nome = CharField()

class Perifericos(BaseModel):
	nome = CharField()
	preco = FloatField()
	tipo = ForeignKeyField(TipoPerifericos)

class Compra(BaseModel):
	dataHora = DateTimeField()
	cliente = ForeignKeyField(Cliente)
	funcionario = ForeignKeyField(Funcionario)
	jogos = ManyToManyField(Jogo)
	perifericos = ManyToManyField(Perifericos)
	valorBruto = FloatField()
	ticketsDesconto = ManyToManyField(TicketsDesconto)

if __name__ == "__main__":
	db.connect()
	db.create_tables([ProdutoraJogos, Fornecedor, Plataforma, Jogo, Cliente, Funcionario, TicketsDesconto, TipoPerifericos, Perifericos, Compra, Compra.jogos.get_through_model(), Compra.perifericos.get_through_model(), Compra.ticketsDesconto.get_through_model()])

	blizzard = ProdutoraJogos.create(nome="Blizzard", cnpj="1234567890")
	chiodini = Fornecedor.create(nome="Chiodini", cnpj="0987654321")
	computador = Plataforma.create(nome="Computador")
	overwatch = Jogo.create(nome="Overwatch", preco=150, lancamento="2015-11-10", classificacaoIndicativa=12, fornecedor=chiodini, produtora=blizzard, plataforma=computador)
	luana = Cliente.create(nome="Luana Chiodini", cpf="12366789020", dataNascimento="2001-11-08")
	vini = Funcionario.create(nome="Vinicius Martins", cpf="80976517292", dataNascimento="2002-03-07", dataVinculoEmpresa="2019-11-25", salario=1050)
	ticket15Reais = TicketsDesconto.create(valor=15)
	headSet = TipoPerifericos.create(nome="HeadSet")
	headSetRazer = Perifericos.create(nome="Razer Kraken", preco=250, tipo=headSet)
	compra = Compra.create(dataHora="2019-11-25 15:59:47", cliente=luana, funcionario=vini, valorBruto=1200)
	compra.jogos.add(overwatch)
	compra.perifericos.add(headSetRazer)
	compra.ticketsDesconto.add(ticket15Reais)




