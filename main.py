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

@app.get("/plants")
def read_root():
    """
    Retorna o nome de uma planta.
    """
    return {"Planta": "Samambaia"}

