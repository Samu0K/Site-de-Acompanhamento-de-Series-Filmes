import sqlite3

conn = sqlite3.connect("banco_de_dados_de_usuario.bd")
conn.execute("""CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    apelido TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    data_nascimento TEXT NOT NULL)""")

conn.commit()
conn.close()

print("Banco de dados criado com sucesso!")

conn = sqlite3.connect("banco_de_dados.db")

conn.execute()