#Aqui serão apenas atalhos para limpar o banco e cria-lo caso necessário

import click
import pandas as pd
import os

from flask.cli import with_appcontext
from .extensions import db
from .models import Usuario

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()

#removi o usuario generico, nao precisa mais. so inserir a massa

    caminhoTXT = os.path.join(os.path.dirname(__file__), '..', 'massa_dados.txt')
    df = pd.read_table(caminhoTXT, sep='|')

    for index, row in df.iterrows():
        usuario = Usuario(
            nome = row["nome"],
            cpf = row["documento"],
            email = row["email"],
            data_nascimento = row["dataNascimento"],
            login = row["login"],
            cep = "",
            endereco = ""
        )
        db.session.add(usuario)
        db.session.commit()

    click.echo("Usuários massa inseridos!")


@click.command(name='drop_tables')
@with_appcontext
def drop_tables(): 
    db.drop_all()
    db.session.commit()
    
    click.echo("Banco limpo")

