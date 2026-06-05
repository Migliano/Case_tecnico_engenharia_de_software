from flask import Flask
from flask_cors import CORS

from .config import Config
from .extensions import db
from .commands import create_tables, drop_tables
from .routes.main import main

def create_app(): #monta e desenvolve o app. Facilita criar versões diferentes do app (dev, prod, test) sem duplicar codigo
    #padrão application factory


    app = Flask(__name__)
    CORS(app) #por isso tava bloqueando políticas de segurança no console

    app.config.from_object(Config)
    db.init_app(app)

    app.register_blueprint(main) #aqui inicia e chama as blueprint.
#é p jeito de organizar as rotas em arquivos separados
#"liga" as rotas do main.py no app

    app.cli.add_command(create_tables)
    app.cli.add_command(drop_tables)

    return app