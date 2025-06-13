from fastapi import FastAPI
from fast_zero.routers import atividades
from fast_zero.database import Base, engine

app = FastAPI(title='Fitness API')

Base.metadata.create_all(bind=engine)

app.include_router(atividades.router)

@app.get('/')
def root():
    return {'message': 'API Atividades Físicas Online!'}