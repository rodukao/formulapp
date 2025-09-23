# IMPORTS

# Banco de dados sqlite
import sqlite3

# CRIA TABELA SE NÃO EXISTIR
conn = sqlite3.connect('banco.db')
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

# fecha conexão
conn.close()

# INSERE USUÁRIOS
def insere_usuario(nome, senha, email):    
    # conecta no banco e gera o cursor
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    
    # cria o dicionário usuário
    usuario = {
        "nome": nome,
        "senha": senha,
        "email": email
    }
    
    # executa e salva a query
    cursor.execute('''
        INSERT INTO usuarios_site(nome, senha, email) VALUES (?, ?, ?)
    ''', (nome, senha, email))
    conn.commit()
    
    print(f"Usuário {nome} inserido com sucesso.")
    # fecha conexão
    conn.close()

# LISTA USUÁRIOS
def lista_usuarios():
    # conecta no banco e gera cursor
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    
    # executa query
    cursor.execute('SELECT * FROM usuarios_site')
    resultado = cursor.fetchall()
    for linha in resultado:
        print(linha)
        
    # fecha conexão
    conn.close()

insere_usuario("Rodrigo", "123456", "rodukao@gmail.com")
insere_usuario("Danny", "432432", "dannyzimmermann@yahoo.com.br")
lista_usuarios()