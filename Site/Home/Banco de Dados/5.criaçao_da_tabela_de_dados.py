import sqlite3

# 1. Corrigir banco_de_dados_de_usuario.db — criar tabela de usuários
conn = sqlite3.connect('banco_de_dados_de_usuario.db')
conn.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        apelido TEXT UNIQUE,
        data_nascimento TEXT,
        email TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL,
        data_cadastro TEXT DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()
conn.close()

# 2. Corrigir banco_de_dados.db — remover a tabela usuarios mal criada
conn = sqlite3.connect('banco_de_dados.db')
conn.execute('DROP TABLE IF EXISTS usuarios')
conn.commit()
conn.close()

print("Bancos corrigidos!")