from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date


from fast_zero import crud, schemas_atividades, database

router = APIRouter(prefix='/atividades', tags=['Atividades'])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

@router.post('/', response_model=schemas_atividades.Output_Atividade)
def create(atividade: schemas_atividades.CriarAtividade, db: Session = Depends(get_db)):
    return crud.criar_atividade(db, atividade)

@router.get('/', response_model=List[schemas_atividades.Output_Atividade])
def list_activities(
    db: Session = Depends(get_db),
    username: Optional[str] = None,
    nome_atividade: Optional[str] = None,
    data_inicial: Optional[date] = Query(None),
    data_final: Optional[date] = Query(None)
):
    if data_inicial and not data_final:
        raise HTTPException(
            status_code=400,
            detail="Se data1 for fornecida, data2 também deve ser."
        )

    if data_inicial and data_final and data_final < data_inicial:
        raise HTTPException(
            status_code=400,
            detail="data_final deve ser maior ou igual a data_inicial."
        )
    atividades = crud.pegar_atividades(db, username, nome_atividade, data_inicial, data_final)

    if not atividades:
        raise HTTPException(
            status_code=404,
            detail="Nenhuma atividade encontrada com os filtros fornecidos."
        )

    return atividades

@router.patch('/{id_atividade}', response_model=schemas_atividades.Output_Atividade, description="Atualiza apenas os campos enviados")
def update(id_atividade: int, atividade: schemas_atividades.AtualizarAtividade, db: Session = Depends(get_db)):
    atualizada = crud.atualizar_atividade(db, id_atividade, atividade)
    if not atualizada:
        raise HTTPException(status_code=404, detail='Atividade não foi encontrada!')
    return atualizada

@router.delete('/{id_atividade}')
def delete(id_atividade: int, db: Session = Depends(get_db)):
    deletada = crud.deletar_atividade(db, id_atividade)
    if not deletada:
        raise HTTPException(status_code=404, detail='Atividade não foi encontrada!')
    return {'message': 'Deletada'}

@router.get('/somatorio/{username}', response_model=schemas_atividades.SomatoriaAtividades)
def summary(username: str, db: Session = Depends(get_db)):
    resultado = crud.pegar_somatoria(db, username)

    if not resultado:
        raise HTTPException(
            status_code=404,
            detail='Usuário não encontrado ou sem atividades registradas.'
        )
    return resultado
