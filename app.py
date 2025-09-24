# IMPORTS
from flask import Flask, render_template, request, redirect, url_for
import os
from dotenv import load_dotenv

# Banco de dados sqlite
from database import cria_tabela_usuarios, insere_usuario, lista_usuarios

app = Flask(__name__)
load_dotenv()
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

# CHAMA FUNÇÕES
cria_tabela_usuarios()

@app.route("/")
def index():
    return render_template('cadastro.html')

@app.route("/cadastrar", methods=['POST'])
def cadastrar_usuario():
    nome = request.form['nome']
    senha = request.form['senha']
    email = request.form['email']

    insere_usuario(nome, senha, email)
    return redirect(url_for('listar_usuarios'))

@app.route("/usuarios")
def listar_usuarios():
    usuarios = lista_usuarios()
    return render_template('lista_usuarios.html', usuarios = usuarios)

if __name__ == "__main__":
    app.run(debug = True)