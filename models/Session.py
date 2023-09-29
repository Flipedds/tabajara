from sqlalchemy import create_engine, select, delete
from sqlalchemy.orm import Session
from models.Conta import Conta

class Session_sql:
    def __init__(self):
        self.engine = create_engine("mysql+mysqlconnector://root:root@127.0.0.1:3306/dbtabajara", echo=False)
        self.session = Session(self.engine)

    def nova_conta(self, conta: Conta):
        try:
            self.session.add(conta)
            self.session.commit()
            self.session.close()
            return "Conta adicionada !"
        except Exception as err:
            return err

    def todas_as_contas(self):
        statement = select(Conta)
        contas = self.session.scalars(statement).all()

        return contas

    def remover_conta(self, id):
        if not isinstance(id, int):
            return "Não é um id válido"
        try:
            stmt = delete(Conta).where(Conta.id == id)
            self.session.execute(stmt)
            self.session.commit()
            self.session.close()
            return f"conta {id} deletada com sucesso !"
        except Exception as err:
            return err

    def selecionar_conta(self, id):
        if not isinstance(id, int):
            return "Não é um id válido"
        try:
            statement = select(Conta).where(Conta.id == id)
            conta = None
            for item in self.session.scalars(statement):
                conta = item
            return conta

        except Exception as err:
            return err

    def atualizar_conta(self, id, nome, saldo):
        if not isinstance(id, int):
            return "Não é um id válido"
        try:
            conta_para_atualizar = self.session.query(Conta).filter_by(id=id).first()
            conta_para_atualizar.nome = nome
            conta_para_atualizar.saldo = saldo
            self.session.commit()
            self.session.close()
            return f"conta {id} atualizada com sucesso !"
        except Exception as err:
            return err
