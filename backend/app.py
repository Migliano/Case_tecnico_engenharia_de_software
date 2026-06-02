from flask import Flask, jsonify, request
from flask_cors import CORS #para o erro de cors no console. remover depois

from login_generator import gerar_login
from database import Usuario, Session
app = Flask(__name__)
CORS(app)

@app.route("/cadastro", methods=['POST'])
def cadastro():
    dados = request.get_json()
    session = Session()

    todos_usuarios = session.query(Usuario).all()

    logins_existentes = []
    for usuario in todos_usuarios:          #criar lista com logins ja existentes para mandar pros generators
        logins_existentes.append(usuario.login)

    """ATENÇÃO: logins_existentes é passado como parâmetro e não variável global pq se fosse global,
    ia buscar os logins só uma vez quando o servidor sobe e ficaria desatualizado conforme novos usuários entram
    assim, cada requisição monta a lista fresh do banco antes de passar pro generator"""
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

    return jsonify({"login": login_final})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False) #esse reloader que tava dando o problema de inferno de recarregar. Checar depois se manter. acho que é so tirar o debug
