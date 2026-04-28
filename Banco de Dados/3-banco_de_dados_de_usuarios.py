import sqlite3
import flask
import request
import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("Home/casdastro/tela_de_cadastro.css", methods= ['POST'])

def rota():
    dados_usuario = request.json()
    adicionar_usuario(dados_usuario['nome'], dados_usuario['apelido'], dados_usuario['email'], dados_usuario['data_nascimento'], dados_usuario['senha'] )
    return jsonify({"status": "Cadastrado com sucesso"})


def adicionar_usuario(nome, apelido, email, data_nascimento, senha):
    conexao = sqlite3.connect('banco_de_dados.db')
    cursor = conexao.cursor()
    cursor.execute("""INSERT INTO (nome, apelido, email, data_nascimento, senha) VALUES (?, ?, ?, ?, ?)""", (nome, apelido, email, data_nascimento, senha))
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Cadastro feito com sucesso!")


if __name__ == "__main__":
    titulo = input("Digite o seu nome: ")
    genero = input("Digite o gênero da série: ")
    ano = int(input("Digite o ano de lançamento da série: "))
    temporadas = input("Digite o número de temporadas da série: ")
    episodios = input("Digite o número de episódios da série: ")
    adicionar_usuario(titulo, genero, ano, temporadas, episodios)
    
def listar_usuario():
    conexao = sqlite3.connect('banco_de_dados.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM series')
    series = cursor.fetchall()

    print("\n--- Minha Lista de Séries ---")
    for s in series:
        print(f"ID: {s[0]} | Título: {s[1]} | Status: {s[5]} (T{s[3]}E{s[4]})")
              
    conexao.close()

print(listar_usuario())
