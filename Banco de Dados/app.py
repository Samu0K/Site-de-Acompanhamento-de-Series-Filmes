import sqlite3

def adicionar_series(titulo, genero, ano, temporadas, episodios):
    conexao = sqlite3.connect('banco_de_dados.db')
    cursor = conexao.cursor()
    cursor.execute("""INSERT INTO series (titulo, genero, ano, temporadas, episodios) VALUES (?, ?, ?, ?, ?)""", (titulo, genero, ano, temporadas, episodios))
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Série adicionada com sucesso!")


if __name__ == "__main__":
    titulo = input("Digite o título da série: ")
    genero = input("Digite o gênero da série: ")
    ano = int(input("Digite o ano de lançamento da série: "))
    temporadas = input("Digite o número de temporadas da série: ")
    episodios = input("Digite o número de episódios da série: ")
    adicionar_series(titulo, genero, ano, temporadas, episodios)

def listar_series():
    conexao = sqlite3.connect('banco_de_dados.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM series')
    series = cursor.fetchall()

    print("\n--- Minha Lista de Séries ---")
    for s in series:
        print(f"ID: {s[0]} | Título: {s[1]} | Status: {s[5]} (T{s[3]}E{s[4]})")
              
    conexao.close()


