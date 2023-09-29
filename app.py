from models.Session import Session_sql
from models.Conta import Conta

session = Session_sql()

MENU = """
Sistema Bancário Tabajara
----------------------------
1 - MOSTRAR TODAS AS CONTAS
2 - NOVA CONTA
3 - REMOVER CONTA
4 - PESQUISAR CONTA
5 - ALTERAR CONTA
6 - SAIR
----------------------------
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
            print(session.nova_conta(conta))
        case 3:
            id = input("Qual conta deseja deletar?")
            print(session.remover_conta(id))
        case 4:
            id = input("Qual conta deseja pesquisar?")
            print(session.selecionar_conta(id))
        case 5:
            id = input("Qual conta deseja atualizar?")
            nome = input("Digite o novo nome: ")
            saldo = float(input("Digite o novo saldo: "))
            print(session.atualizar_conta(id, nome, saldo))
        case 6:
            break
        case _:
            pass
