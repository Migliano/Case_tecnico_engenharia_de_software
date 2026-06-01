import pandas as pd #eu comecei a fazer por open e split mas tive um pouco de dificuldade. Fui pro pandas que tenho mais familiaridade
from database import Usuario, Session

session = Session()

df = pd.read_table('massa_dados.txt', sep = '|')

row = df.iloc[0] #iloc para pegar a primeira linha, pandas ja separa o head

for index, row in df.iterrows():
    usuario = Usuario(
    nome = row["nome"],
    cpf = row["documento"],
    email = row["email"],
    data_nascimento = row["dataNascimento"],
    login = row["login"],
    cep = "",
    endereco = "" #vazio pq o massa veio vazio
    )

    session.add(usuario)
    session.commit() #igual database.py
    print(f"Usuário {row['nome']} inserido com login {row['login']}")





