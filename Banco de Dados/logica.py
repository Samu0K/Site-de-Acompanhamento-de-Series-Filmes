import _sqlite3
import _json

def criar_banco_de_dados():
    conn = _sqlite3.connect('banco_de_dados.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()
    print("Banco de dados criado com sucesso!")

if __name__ == "__main__":
    criar_banco_de_dados()
    