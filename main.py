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
def read_plant():
    """
    Retorna o nome de uma planta.
    """
    return {"Planta": "Samambaia"}

@app.get("/arvore")
def read_arvore():
    """
    Retorna o nome de uma arvore.
    """
    return {"Arvore": "Ipê"}

@app.get("/horta")
def check_horta_status():
    """
    Retorna o status da horta.
    """
    return {"status": "online"}
