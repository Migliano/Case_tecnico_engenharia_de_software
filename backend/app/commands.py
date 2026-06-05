import click
from flask.cli import with_appcontext

from .extensions import db
from .models import Usuario

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()

    generico = Usuario(
        nome = "Usuário Genérico",
        login = "usuario.genérico",
        cpf = "50252073800",
        email = "usuario@genérico.com",
        data_nascimento = "01/01/1900", #data_nascimento tem que ser string por causa da tabela de limites, por date deve dar muito trabalho
        cep = "00000000",
        endereco = "Endereço Genérico"
    )

    db.session.add(generico)
    db.session.commit()

    click.echo("Tabelas criadas com sucesso!")

@click.command(name='drop_tables')
@with_appcontext
def drop_tables(): 
    db.drop_all()
    db.session.commit()
    
    click.echo("Banco limpo")

