print('Criando banco de dados')
# importando o SQLite
import sqlite3 as lite

# Criando conexão
con = lite.connect('dados.db')

# Criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, numero TEXT, senha TEXT)")

print('Criando banco de dados criado com sucesso!')
