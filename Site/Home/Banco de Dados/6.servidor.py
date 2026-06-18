from flask import Flask, request, jsonify, session
from flask_cors import CORS
import sqlite3
import hashlib
import os

app = Flask(__name__)
app.secret_key = "chave_secreta_do_site"
CORS(app, supports_credentials=True)

DB_USUARIOS = "banco_de_dados_de_usuario.db"
DB_SERIES = "banco_de_dados.db"

def get_conn(db_path):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# Rota de cadastro

@app.route("/cadastro", methods=["POST"])
def cadastro():
    dados = request.json
    nome = dados.get("nome", "").strip()
    apelido = dados.get("apelido", "").strip()
    email = dados.get("email", "").strip()
    data_nascimento = dados.get("data_nascimento", "").strip()
    senha = dados.get("senha", "").strip()

    if not nome or not email or not senha:
        return jsonify({"status": "Erro", "mensagem": "Nome, email e senha são obrigatórios."}), 400
    
    if len(senha) < 6:
        return jsonify({"status": "Erro", "mensagem": "A senha deve ter pelo menos 6 caracteres."}), 400
    
    try:
        conn = get_conn(DB_USUARIOS)
        conn.execute("INSERT INTO usuarios (nome, apelido, email, data_nascimento, senha) VALUES (?, ?, ?, ?, ?)",(nome, apelido, email, data_nascimento, hash_senha(senha)))
        conn.commit()
        return jsonify({"status": "Sucesso", "mensagem": "Usuário cadastrado com sucesso."}), 201
    
    except sqlite3.IntegrityError:
        return jsonify({"status": "Erro", "mensagem": "Email ou apelido já estão em uso."}), 409
    except Exception as e:
        print(f"Erro no banco: {e}")
        return jsonify({"status": "Erro", "mensagem": "Erro interno ao salvar no banco."}), 500
    
@app.route("/login", methods=["POST"])
def login():
    dados = request.json
    email = dados.get("email", "").strip()
    senha = dados.get("senha", "").strip()

    conn = get_conn(DB_USUARIOS)
    usuario = conn.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, hash_senha(senha))).fetchone()
    conn.close()

    if usuario:
        session["usuario_id"] = usuario["id"]
        session["usuario_nome"] = usuario["nome"]
        return jsonify({"status": "Sucesso", "mensagem": "Login realizado com sucesso.", "nome": usuario["nome"]}), 200
    else:
        return jsonify({"erro": "Email ou senha inválidos."}), 401
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)