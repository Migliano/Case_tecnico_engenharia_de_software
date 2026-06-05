from flask import Flask
from flask_cors import CORS

from .config import Config
from .extensions import db
from .commands import create_tables, drop_tables
from .routes.main import main

def create_app():

    app = Flask(__name__)
    CORS(app)

    app.config.from_object(Config)
    db.init_app(app)

    app.register_blueprint(main)

    app.cli.add_command(create_tables)
    app.cli.add_command(drop_tables)

    return app