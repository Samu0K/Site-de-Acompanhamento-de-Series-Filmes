import sqlite3

def criar_banco_de_dados():
    conn = sqlite3.connect('banco_de_dados_de_usuario.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            apelido TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            data_nascimento TEXT NOT NULL,
            senha TEXT NOT NULL
        )
           
    ''')
    conn.commit()
    conn.close()
    print("Banco de dados criado com sucesso!")

if __name__ == "__main__":
    criar_banco_de_dados()