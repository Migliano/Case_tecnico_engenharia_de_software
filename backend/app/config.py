import os

class Config():

    SECRET_KEY = 'dkjfhskfhdskfhjk' #chave aleatória hardcoded só pra desenvolvimento. Em produção seria necessario uma variável de ambiente dedicada pra nao ficar exposto no codigo
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'database/usuarios.db')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False #desligar sistema de notificação interno do sqlalchemy. Não usei, deixei false

