import os

class Config():

    SECRET_KEY = 'dkjfhskfhdskfhjk'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'database/usuarios.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

