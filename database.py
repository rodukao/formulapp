import sqlite3

from flask import flash

# Email validator
from email_validator import validate_email, EmailNotValidError

# Criptografia de senha
import bcrypt

# CRIA TABELA SE NÃO EXISTIR
def cria_tabela_usuarios():
    try:
        with sqlite3.connect('banco.db') as conn:
            cursor = conn.cursor()

            # Criando tabela
            # as 3 aspas são para criar strings de múltiplas linhas facilitando a leitura
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios_site(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    senha TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE
                )
            ''')
    
    except Exception as e:
        print(f"Ocorreu um erro ao criar a tabela: {e}")

# INSERE USUÁRIOS
def insere_usuario(nome, senha, email):
    # checa se campos estão todos preenchidos
    if valida_campos(nome, senha, email):
        
        # Criptografa a senha antes de inseri-la no banco
        senha_criptografada = bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        
        try:
            with sqlite3.connect('banco.db') as conn:
                cursor = conn.cursor()
            
                # executa query e informa resultado
                cursor.execute('INSERT INTO usuarios_site(nome, senha, email) VALUES (?, ?, ?)', (nome, senha_criptografada, email))
                conn.commit()  
                flash(f"Usuário {nome} inserido com sucesso.", "success")

        except sqlite3.IntegrityError:
            flash(f"O email {email} já está registrado.", "error")

        except Exception as e:
            flash(f"Ocorreu um erro ao inserir usuário: {e}", "error")
    
    else:
        flash("Erro na validação dos campos.", "error")


# VALIDA CAMPOS
def valida_campos(nome, senha, email):
    # Retorna False se os campos estiverem vazios
    if not nome or not senha or not email:
        return "Todos os campos precisam estar preenchidos."
    else:
        
        # Valida email usando a dependência email-validator
        try:
            emailinfo = validate_email(email, check_deliverability=False)
            email = emailinfo.normalized
            return True
        
        except EmailNotValidError as e:
            print(str(e))
            return False

# LISTA USUÁRIOS
def lista_usuarios():
    try:
        with sqlite3.connect('banco.db') as conn:
            cursor = conn.cursor()
            
            # executa query
            cursor.execute('SELECT * FROM usuarios_site')
            return cursor.fetchall()

    except Exception as e:
        print(f"Ocorreu um erro ao listar os usuários: {e}")
        return []