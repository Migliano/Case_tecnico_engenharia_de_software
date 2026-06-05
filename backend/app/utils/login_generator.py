#Gerar logins únicos a partir do nome

def gerar_login(nomeCompleto, logins_existentes):          #função para efetivamente gerar o login: passa pelos generators e compara com o banco, caso ja exista o login, tenta o proximo generator

    opcoes_de_Login = [
        login_generator1(nomeCompleto),
        login_generator2(nomeCompleto),
        login_generator3(nomeCompleto),
        login_generator4(nomeCompleto),
           ] + login_generator5(nomeCompleto)           #neste caso, decidi fazer a 5 retornar uma lista e gerar_login SOMA as 2 listas. Talvez seja mais facil de debugar 1 lista só caso de problema. Outra opção seria fazer a gerar_login interpretar a lista da 5 diferentemente de forma separada: testa as 4 e, caso nao encontre espaço vazio, ir para a 5

    for opcao_de_Login in opcoes_de_Login:

        if opcao_de_Login not in logins_existentes:
            return opcao_de_Login


def normalizar_nome (nome):                 #normalizador para tirar o espaço entre nomes e manter em letras minusculas para todos os generators
    return nome.replace (' ','').lower()


def login_generator1(nomeCompleto):         #generator que pega as 7 primeiras letras do nome normalizado
    nomeLimpo = normalizar_nome(nomeCompleto)
    sete = nomeLimpo[:7]
    return sete.lower()


def login_generator2(nomeCompleto):         #generator que concatena as 4 primeiras letras e 3 ultimas do nome normalizado
    nomeLimpo = normalizar_nome(nomeCompleto)
    prefixo = nomeLimpo[:4]
    sufixo = nomeLimpo[-3:]
    sete = prefixo + sufixo
    return sete.lower()


def login_generator3(nomeCompleto):         #generator que concatena as 5 primeiras letras e 2 ultimas do nome normalizado
    nomeLimpo = normalizar_nome(nomeCompleto)
    prefixo = nomeLimpo[:5]
    sufixo = nomeLimpo[-2:]
    sete = prefixo + sufixo
    return sete.lower()


def login_generator4(nomeCompleto):         #generator que concatena as iniciais do nome com as primeiras letras do nome normalizado
    iniciais = ''

    for parte in nomeCompleto.split():
        iniciais += parte[0]

    resultado = 7 - len(iniciais)

    nomeLimpo = normalizar_nome(nomeCompleto)
    sufixo = nomeLimpo[:resultado]

    sete = iniciais + sufixo
    return sete.lower()

def login_generator5(nomeCompleto):         #generator "coringa", percorre 'janelas' dentro do nome normalizado, afim de diminuir a chance de repetições a quase 0
    nomeLimpo = normalizar_nome(nomeCompleto)
    opcoesGenerator5 = []   

    for i in range(len(nomeLimpo) - 6):

        opcoesGenerator5.append(nomeLimpo[i:i+7])

    return opcoesGenerator5


# roda só se executar "python login_generator.py" direto. serve pra testar os generators na mão sem precisar de banco nem de servidor. se o app.py importar esse arquivo, esse bloco é ignorado, remover depois
if __name__ == '__main__':
    nomeCompleto = 'ANA BEATRIZ FERREIRA' #simulação de nome
    logins_existentes = ['anabeat', 'anabira', 'anabera', 'abfanab', 'nabeatr', 'abeatri', 'beatriz'] #simulação de banco de dados com logins existentes
    login = login_generator4(nomeCompleto)
    gerar = gerar_login(nomeCompleto, logins_existentes)

    print (gerar)
    
