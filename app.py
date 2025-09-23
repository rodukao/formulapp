# IMPORTS

# Banco de dados sqlite
import sqlite3

# CRIA TABELA SE NÃO EXISTIR
def cria_tabela_usuarios():
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

# INSERE USUÁRIOS
def insere_usuario(nome, senha, email):    
    with sqlite3.connect('banco.db') as conn:
        cursor = conn.cursor()
    
        # executa query e informa resultado
        cursor.execute('INSERT INTO usuarios_site(nome, senha, email) VALUES (?, ?, ?)', (nome, senha, email))
        conn.commit()  
        print(f"Usuário {nome} inserido com sucesso.")


# LISTA USUÁRIOS
def lista_usuarios():
    with sqlite3.connect('banco.db') as conn:
        cursor = conn.cursor()
        
        # executa query
        cursor.execute('SELECT * FROM usuarios_site')
        resultado = cursor.fetchall()
        for linha in resultado:
            print(linha)


# CHAMA FUNÇÕES
cria_tabela_usuarios()

insere_usuario("Rodrigo", "123456", "rodukao@gmail.com")
insere_usuario("Danny", "432432", "dannyzimmermann@yahoo.com.br")

lista_usuarios()