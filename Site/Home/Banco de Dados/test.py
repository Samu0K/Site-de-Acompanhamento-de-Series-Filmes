import sqlite3

def adicionar_series(nome):
    conexao = sqlite3.connect('banco_de_series.db')
    cursor = conexao.cursor()
    cursor.execute("""INSERT INTO series (nome) VALUES (?)""", (nome,))
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Série adicionada com sucesso!")


if __name__ == "__main__":
    nome = input("Digite o título da série: ")
    adicionar_series(nome)

def test():
    conexao = sqlite3.connect('banco_de_dados_de_usuario.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM series')
    series = cursor.fetchall()

    print("\n--- Minha Lista de Séries ---")
    for s in series:
        print(f"ID: {s[0]} | Nome: {s[1]}")
              
    conexao.close()

print(test())