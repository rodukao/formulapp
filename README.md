Um webapp feito com Python para a criação e disponibilização de sistemas de cadastro.
A ideia é que o usuário possa criar um sistema de cadastro sem entender de códigos.

Como baixar o projeto:
- Clone o projeto para seu ambiente utilizando "git clone https://github.com/rodukao/formulapp.git"
- Instale as dependências necessárias utilizando o comando "pip install -r requirements.txt" (recomendado ativar venv)
- crie um arquivo na raiz do projeto chamado ".env" com uma variável chamada "FLASK_SECRET_KEY" (essa variável deve conter uma chave segura aleatória secreta; Você pode criar essa chave executando o arquivo "gerador_chave_secreta.py")

Progresso:
- Usuário pode se cadastrar utilizando a rota "/cadastrar"
- Listar usuários cadastrados utilizando a rota "usuarios" (para teste e não estará disponível na versão de produção)