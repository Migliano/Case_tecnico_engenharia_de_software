from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///cadastro.db', echo=True)  #igual base alfred, tirar o echo em produção!

class Usuario(Base):
    __tablename__ = 'cadastro_usuarios'

    id = Column(Integer, primary_key = True, autoincrement =True)
    nome = Column(String, nullable = False)
    login = Column (String, nullable = False, unique=True)
    cpf = Column (String, nullable = False) #tem que ser string por conta dos 00 no começo
    email = Column (String, nullable = False)
    data_nascimento = Column (String, nullable = False) #fazendo igual a tabela de limites, por date deve dar muito trabalho
    cep = Column (String, nullable = False) #tem que ser string por conta dos 00 no começo
    endereco = Column (String, nullable = False)

Base.metadata.create_all(engine) #pegua a base e cria a tabela de fato
Session = sessionmaker(bind=engine)
