from flask import Flask, jsonify, request

from login_generator import gerar_login
from database import Usuario, Session
app = Flask(__name__)

@app.route("/cadastro", methods=['POST'])
def cadastro():
    dados = request.get_json()
    session = Session()

    todos_usuarios = session.query(Usuario).all()

    logins_existentes = []
    for usuario in todos_usuarios:          #criar lista com logins ja existentes para mandar pros generators
        logins_existentes.append(usuario.login)

    login_final = gerar_login(dados['nome'], logins_existentes)           #chama função gerar_login la do login_generator. Passa o nome completo (classe nome de "dados") e os logins_existentes (repeti o nome pra nao confundir. talvez faça a mesma coisa para o nomecompleto, vou ver se fica ruim de debugar)
    
    novo_usuario = Usuario(
    nome = dados['nome'],
    cpf = dados['cpf'],
    email = dados['email'],
    data_nascimento = dados['data_nascimento'],
    cep = dados['cep'],
    endereco = dados['endereco'],
    login = login_final
)
    session.add(novo_usuario)
    session.commit()

    print(dados) #remover depois, so pra testar o postman

    return jsonify({"mensagem": "funcionou"})

if __name__ == '__main__':
    app.run(debug=True)


"""{
    "nome": "Ana Beatriz Ferreira",
    "cpf": "123.456.789-00",
    "email": "ana@email.com",
    "data_nascimento": "2001-04-09",
    "cep": "04113-040",
    "endereco": "Paulista"
}"""