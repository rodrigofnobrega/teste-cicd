"""
Módulo principal da aplicação FastAPI.
Define o endpoint raiz que retorna um "Hello World".
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """
    Retorna uma saudação simples no formato JSON.
    """
    return {"Hello": "World"}
