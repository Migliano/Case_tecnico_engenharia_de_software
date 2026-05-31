from flask import Flask, jsonify, request

from login_generator import gerar_login
from database import Usuario, Session
app = Flask(__name__)

@app.route("/cadastro", methods=['POST'])
def cadastro():
    dados = request.get_json()
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