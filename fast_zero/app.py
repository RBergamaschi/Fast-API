from fastapi import FastAPI

app = FastAPI()


@app.get('/')  # end_point 'home' ou 'root'
def read_root():
    return {'message': 'Hello World'}
