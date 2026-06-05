from .extensions import db

class Usuario(db.Model):
    __tablename__ = 'cadastro_usuarios'

    id = db.Column(db.Integer, primary_key = True, autoincrement =True)
    nome = db.Column(db.String, nullable = False)
    login = db.Column (db.String, nullable = False, unique=True)
    cpf = db.Column (db.String, nullable = False) #tem que ser string por conta dos 00 no começo
    email = db.Column (db.String, nullable = False)
    data_nascimento = db.Column (db.String, nullable = False) #fazendo igual a tabela de limites, por date deve dar muito trabalho
    cep = db.Column (db.String, nullable = True) #tem que ser string por conta dos 00 no começo, deixei true por causa da massa inicial
    endereco = db.Column (db.String, nullable = True) #deixei true por causa da massa inicial

    def __repr__(self):
        return f"<Usuario {self.nome}>"


#def limpar_banco(): #por enquanto, pra deletar o banco. remofer if__name__ também se for tirar daqui
#    Base.metadata.drop_all(engine)
#    Base.metadata.create_all(engine)
#    print("banco limpo e recriado")

#if __name__ == '__main__': 
#    limpar_banco() #depois remover, é so pra esvaziar o banco
