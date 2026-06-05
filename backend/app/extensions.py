from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#db criado aqui e não no __init__.py pra evitar importação circular: models precisa do db, __init__ precisa dos models, se o db ficasse no __init__ daria loop