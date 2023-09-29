from sqlalchemy import Column, String, Integer, DECIMAL
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Conta(Base):
    __tablename__ = 'conta'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String(60), nullable=False)
    saldo = Column('saldo', DECIMAL(9, 2), default=0)

    def __str__(self):
        return f"{self.id}, {self.nome}, {self.saldo}"
    