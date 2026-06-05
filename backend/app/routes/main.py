

from flask import Blueprint, jsonify, request, render_template

from ..models import Usuario
from ..extensions import db
from ..utils.login_generator import gerar_login
from ..utils.sanity_check import sanity_checkar_campos

main = Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route("/cadastro", methods=['POST'])
def cadastro():
    dados = request.get_json() #pega os dados do front
    #session = Session()

    todos_usuarios = Usuario.query.all()

    logins_existentes = []
    for usuario in todos_usuarios:          #criar lista com logins ja existentes para mandar pros generators
        logins_existentes.append(usuario.login)

    #Antes de criar login e receber os dados pro banco, vamos valida-los no backend também
    erro = sanity_checkar_campos(dados)

    if erro:
        return jsonify({"erro": erro}), 400

    """logins_existentes é passado como parâmetro e não variável global pq se fosse global,
    ia buscar os logins só uma vez quando o servidor sobe e ficaria desatualizado conforme novos usuários entram.
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

    db.session.add(novo_usuario)
    db.session.commit()

    return jsonify({"login": login_final})