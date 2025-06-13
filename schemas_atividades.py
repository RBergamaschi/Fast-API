from datetime import date
from typing import Optional, List
from pydantic import BaseModel, Field, field_validator


class AtividadeBase(BaseModel):
    nome: str = Field(..., min_length = 1, description=('Nome da atividade'))
    duracao: int = Field(...,gt = 0, description =('Duração da atividade(em minutos)'))
    data: date = Field(..., description = ('Data da atividade (não pode ser no passado)'))
    distancia: Optional[float] = Field(default =None, ge = 0, description = ('Distância da atividade (não negativa)'))
    calorias: Optional[float] = Field(default = None, ge = 0, description = ('Calorias queimadas (não negativa)'))
    username: str
    
    @field_validator('data')
    @classmethod
    def validacao_data(cls, value):
        if value < date.today():
            raise ValueError('A data não pode estar no passado')
        return value
    

class CriarAtividade(AtividadeBase):
    pass


class AtualizarAtividade(BaseModel):
    nome: Optional[str] = Field(default= None, min_length = 1)
    duracao: Optional[int] = Field(default=None, gt=0)
    distancia: Optional[float] = Field(default = None, ge = 0)
    calorias: Optional[float] = Field(default = None, ge = 0)
    
    
class Output_Atividade(AtividadeBase):
    id:int
    
    class Config:
        orm_mode = True
    

class SomatoriaAtividades(BaseModel):
    total_atividades: int
    total_minutos: int
    total_calorias: float
    total_duracao: float