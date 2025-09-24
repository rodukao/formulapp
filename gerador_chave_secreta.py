# Esse arquivo serve para gerar uma chave secreta para podermos usar no Flask

import secrets

chave = secrets.token_urlsafe(16)
print(chave)