from sqlalchemy.orm import Session
from fast_zero import models, schemas_atividades
from sqlalchemy import func
from datetime import date


def criar_atividade(db: Session, atividade: schemas_atividades.CriarAtividade):
    db_atividade = models.Atividade(**atividade.model_dump())
    db.add(db_atividade)
    db.commit()
    db.refresh(db_atividade)
    return db_atividade


def pegar_atividades(db: Session, username=None, nome_atividade=None, data_inicial= None, data_final = None):
    query = db.query(models.Atividade)
    
    if username:
        query = query.filter(models.Atividade.username == username)
    if nome_atividade:
        query = query.filter(models.Atividade.nome == nome_atividade)
    if data_inicial and data_final:
        query = query.filter(models.Atividade.data.between(data_inicial, data_final))  
    
    return query.all()


def pegar_atividade(db: Session, id_atividade: int):
    return db.query(models.Atividade).filter(models.Atividade.id == id_atividade).first()


def atualizar_atividade(db: Session, id_atividade: int, data_atividade: schemas_atividades.AtualizarAtividade):
    db_atividade = pegar_atividade(db, id_atividade)
    if not db_atividade:
        return None
    for field, value in data_atividade.model_dump(exclude_unset=True).items():
        setattr(db_atividade, field, value)
    db.commit()
    db.refresh(db_atividade)
    return db_atividade

def deletar_atividade(db: Session, id_atividade: int):
    db_atividade = pegar_atividade(db, id_atividade)
    if db_atividade:
        db.delete(db_atividade)
        db.commit()
    return db_atividade

def pegar_somatoria(db: Session, username: str):
    query = db.query(
        func.count(models.Atividade.id),
        func.sum(models.Atividade.duracao),
        func.sum(models.Atividade.calorias),
        func.avg(models.Atividade.duracao),
    ).filter(models.Atividade.username == username)
    
    total, minutos, calorias, duracao = query.one()
    return {
        'total_atividades' : total or 0,
        'total_minutos': minutos or 0,
        'total_calorias': calorias or 0.0,
        'total_duracao': duracao or 0.0
    }
