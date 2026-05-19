import sqlite3
import flask
from flask import Flask, request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("./cadastro/tela_de_cadastro", methods= ['POST'])

def rota():
    dados_usuario = request.json
    adicionar_usuario(dados_usuario['nome'], dados_usuario['apelido'], dados_usuario['email'], dados_usuario['data_nascimento'], dados_usuario['senha'] )
    return jsonify({"status": "Cadastrado com sucesso"})


def adicionar_usuario(nome, apelido, email, data_nascimento, senha):
    conexao = sqlite3.connect('banco_de_dados.db')
    cursor = conexao.cursor()
    cursor.execute("""INSERT INTO banco_de_dados_de_usuario.db (nome, apelido, email, data_nascimento, senha) VALUES (?, ?, ?, ?, ?)""", (nome, apelido, email, data_nascimento, senha))
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Cadastro feito com sucesso!")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
    
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
