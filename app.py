from models.Session import Session_sql
from models.Conta import Conta

# engine = create_engine("mysql+mysqlconnector://root:root@127.0.0.1:3306/dbtabajara", echo=True)
# Base.metadata.create_all(engine)

session = Session_sql()

MENU = """
1 - MOSTRAR TODAS AS CONTAS
2 - NOVA CONTA
3 - REMOVER CONTA
4 - PESQUISAR CONTA
5 - SAIR
"""

loop = True

while loop:
    escolha = int(input(MENU))
    match escolha:
        case 1:
            contas = session.todas_as_contas()
            for conta in contas:
                print(conta)
        case 2:
            nome = input("Digite o nome: ")
            saldo = float(input("Digite o saldo: "))
            conta = Conta(nome=nome, saldo=saldo)
            session.nova_conta(conta)
        case 3:
            id = input("Qual conta deseja deletar?")
            print(session.remover_conta(id))
        case 4:
            id = input("Qual conta deseja pesquisar?")
            print(session.selecionar_conta(id))
        case 5:
            break
        case _:
            pass
