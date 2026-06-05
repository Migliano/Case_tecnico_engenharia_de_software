import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from login_generator import gerar_login

def test_login_tem_7_caracteres():
    login = gerar_login('Ana Clara Souza')
    assert len(login) == 7

def test_login_sem_espacos():
    login = gerar_login('Ana Clara Souza')
    assert ' ' not in login

def test_login_minusculo():
    login = gerar_login('Ana Clara Souza')
    assert login == login.lower()

def test_login_sem_duplicatas(): #vai continuar dando erroa ate eu criar o banco, nao vou criar banco falso
    login1 = gerar_login('Maria Silva Santos')
    login2 = gerar_login('Maria Silva Soares')
    assert login1 != login2 