from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from fast_zero.database import Base

class Atividade(Base):
    __tablename__ = 'atividades'
    
    id = Column(Integer, primary_key = True, index = True)
    username = Column(String, index = True)
    nome = Column(String)
    duracao = Column(Integer)
    data = Column(Date)
    distancia = Column(Float, nullable = True)
    calorias = Column(Float, nullable = True)
    
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key = True, index = True)
    nome = Column(String, nullable = False)
    email = Column(String, unique = True, index = True, nullable = False)
    senha = Column(String, nullable = False)
    