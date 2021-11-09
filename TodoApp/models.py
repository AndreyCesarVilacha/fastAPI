from sqlalchemy import Boolean, Column, Integer, String
from database import Base

#criando um model
class Todos(Base):
    #nome da tabela
    __tablename__ = "todos"

    #Criando uma chave primaria
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    Complete = Column(Boolean, default=False)