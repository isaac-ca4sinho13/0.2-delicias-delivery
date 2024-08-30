import sqlite3 as lite
from datetime import datetime


# Criando conexão
con = lite.connect('DD\projeto_cad_usuario\db.sqlite3')

# Inserir
def inserir_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO app_cad_usuario_usuarios(nome,numero,senha) VALUES (?,?,?)"
        cur.execute(query, i)


# Deletar
def deletar_form(i):
   
    with con:
        cur = con.cursor()
        query = "DELETE FROM app_cad_usuario_usuarios WHERE id_usuario=?"
        cur.execute(query, i)


# Atualizar
def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = "UPDATE  app_cad_usuario_usuarios SET nome=?, numero=?, senha=? WHERE id_usuario=?"
        cur.execute(query, i)


# Listar
def ver_form():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM app_cad_usuario_usuarios")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens


# Ver Item 
def ver_iten(id):
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM  app_cad_usuario_usuarios  WHERE id_usuario=?",(id))
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens

if __name__ == '__main__':
    #info2 = ["Isaac","987301724","123"]
    #inserir_form(info2)
    lista = ['1']
    deletar_form(lista)

    #info3 = ["Isaac","99999999","000",'4']
    #atualizar_form(info3)

    #print(ver_form())

    #print(ver_iten('2'))


