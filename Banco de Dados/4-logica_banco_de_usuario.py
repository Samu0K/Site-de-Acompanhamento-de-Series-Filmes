import _sqlite3
import _json

def criar_banco_de_dados():
    conn = _sqlite3.connect('banco_de_dados_de_usuario.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            apelido TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            data_nascimento TEXT NOT NULL,
            senha TEXT NOT NULL UNIQUE,
        )
           
    ''')
    conn.commit()
    conn.close()
    print("Banco de dados criado com sucesso!")

if __name__ == "__main__":
    criar_banco_de_dados()