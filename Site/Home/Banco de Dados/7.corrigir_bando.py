import sqlite3

conn = sqlite3.connect("banco_de_dados_de_usuario.bd")
conn.execute("""CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    data_nascimento DATE NULL,
    senha TEXT NOT NULL
)""")

conn.commit()
conn.close()

print("Banco de dados criado com sucesso!")

conn = sqlite3.connect("banco_de_dados.db")

conn.execute("DROP TABLE IF EXISTS usuarios")
conn.commit()
conn.close()

print("Banco de dados corrigido!")