#Validar dados antes de salvar

import re as re
from validate_docbr import CPF
from datetime import datetime
from email_validator import validate_email


def sanity_checkar_campos(dados): #recebe os dados la do front e manda cada tipo de dado pra função especifica. Ja retorna o ero

    erro = validar_nome(dados.get('nome'))
    if erro:
        return erro
    
    erro = validar_cpf(dados.get('cpf'))
    if erro:
        return erro
    
    erro = validar_email(dados.get('email'))
    if erro:
        return erro
    
    erro = validar_data_nascimento(dados.get('data_nascimento'))
    if erro:
        return erro

    erro = validar_cep(dados.get('cep'))
    if erro:
        return erro

    erro = validar_endereco(dados.get('endereco'))
    if erro:
        return erro
    
    return None #deu tudo certo!

def validar_nome(nome):

    if nome is None: #verifica se é vazio
        return "Nome não pode estar vazio"
    
    if len(nome) > 100: #nome é um campo de texto livre. Precisa de controle de maximo de caracteres
        return "Nome muito longo"
    
    nome_sanitizado = nome.strip() #remover espaçõs em branco inicio e final

    if nome_sanitizado == '': #verifica se terminou vazio depois do strip (pode ser que o nome era uns espaços, ai fez o strip vira none)
        return "Nome não pode estar vazio"

    nome_padrao = re.compile(r'^[a-zA-Z\s]+$') #lib re para checar caracteres especiais. so deixa letras A-Z e espaços

    if not nome_padrao.match(nome_sanitizado): #se nao bateu com o padrao -> invalido
        return "Nome não pode ter caracteres especiais"
    
    return None
    

def validar_cpf(cpf):

    if cpf is None:
        return "CPF não pode estar vazio"
    
    cpf_sanitizado = cpf.strip() #remover espaçõs em branco inicio e final
    

    cpf_validator = CPF()

    if cpf_validator.validate(cpf_sanitizado) is True: #validate() pertence á instancia da lib, ai deixa separado de cpf
        return None
    else: 
        return "CPF invalido"
    

def validar_email(email):
    if email is None:
        return "Email não pode estar vazio"
    
    try:
        validate_email(email, check_deliverability=False) #igual pypi.org. deliverability é pra tentar first time validations
        return None  # válido
    except:
        return "Email inválido"
     
    
def validar_data_nascimento(data_nascimento):
    if data_nascimento is None:
        return "Data de Nascimento não pode estar vazio"
    
    try:
        data_nascimento_sanitizada = datetime.strptime(data_nascimento, "%Y-%m-%d") #tem que normalizar antes de comparara com a data atual, por isso tava dando

        if data_nascimento_sanitizada > datetime.now():
            return "Data de Nascimento não pode ser futura"
        else:
            return None
    
    except ValueError:
        return "Formato de data invalido. Use DD/MM/YYYY"
    

def validar_cep(cep):

    if cep is None: #verifica se é vazio
        return "CEP não pode estar vazio"

    else: 
        cep_sanitizado = cep.replace('-', '')
        cep_sanitizado = cep_sanitizado.replace('.', '')

        cep_padrao = re.compile(r'^\d{8}$') #definir padrão de estrutura do dado

        if not cep_padrao.match(cep_sanitizado): #se nao bateu com o padrao -> invalido
            return "CEP invalido"
        
        return None
    
def validar_endereco(endereco):

    if endereco is None: #verifica se é vazio
        return "Endereço não pode estar vazio"
    
    if len(endereco) > 100: #Endereço é um campo livre. precisa de controle maximo de caracteres
        return "Endereço muito longo"

    else: 
        return None    