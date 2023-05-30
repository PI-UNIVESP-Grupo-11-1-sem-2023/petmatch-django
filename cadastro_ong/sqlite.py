import sqlite3
from forms import participantes

Nome = participantes.Nome
CPF = participantes.CPF
Telefone = participantes.Telefone
Cep = participantes.Cep
Rua = participantes.Rua
Cidade = participantes.Cidade
Estado = participantes.Estado

banco = sqlite3.connect('db.sqlite3')
cursor = banco.cursor()

cursor.execute("INSERT INTO participantes VALUES ('"+Nome+"','"+CPF+"','"+Telefone+"','"+Cep+"','"+Rua+"','"+Cidade+"','"+Estado+"')")

banco.commit()