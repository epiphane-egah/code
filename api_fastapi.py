from fastapi import FastAPI, status, HTTPException, Query, Path, Body, Request
from fastapi.responses import JSONResponse

from pydantic import BaseModel, Field

import sqlite3
from typing import Optional
from datetime import datetime


api = FastAPI(
    title='Test FastAPI',
    description="Un ensemble de code pour apprendre " \
    "le fonctionnement de FastAPI",
    version="1.0.1",
    redoc_url="/egah",
    openapi_tags=[
        {
            "name": "Accueil",
            "description": "Les fonctions par défaut"
        },
        {
            "name": "Articles",
            "description": "Les fonctions pour manipuler les articles"
        }
    ]
)


class Item(BaseModel):
    """Les informations sur les articles du magasin
    """
    name: str = Field(..., description="nom article")
    price: int = Field(..., gt=0, description="prix")
    description: Optional[str] = Field(
        None,
        max_length=200,
        description="description du produit"
        )


@api.get("/", name="Message d'accueil", tags=["Accueil"])
def home():
    """Page d'accueil
    """
    return {
        "message": "Hello, I am working"
    }


# EXEMPLE DE PATH
@api.get(
        '/get_all_item',
        status_code=status.HTTP_200_OK,
        name="Liste des articles",
        tags=['Articles'])
def get_all():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    query = 'select * from article'
    c.execute(query)
    result = c.fetchall()
    return {
        "data": result
    }


# BODY PARAMETER
@api.post(
        "/create_new_item",
        status_code=status.HTTP_201_CREATED,
        name="Ajouter un nouvel article",
        tags=['Articles'])
def add_new_article(item: Item = Body(...)):  # Body
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    query = "INSERT INTO article (name, description, price) VALUES (?, ?, ?)"
    c.execute(query, (item.name, item.description, item.price))
    conn.commit()
    conn.close()


''' curl -X POST http://127.0.0.1:8000/create_new_item
 -H "Content-Type: application/json"
'-d '{"name": "montre lanier", "price": 45,
"description": "Une montre de qualite"}'
'''


# PATH PARAMETER
@api.get(
        "/articles/{item_id}",
        status_code=status.HTTP_200_OK,
        name="Récupérer un article avec son id",
        tags=['Articles'])
def get_item(item_id: int = Path(...)):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    query = "select * from article where id=?"
    c.execute(query, (item_id, ))
    result = c.fetchone()
    return {
        "data": result
    }
# curl -X GET http://127.0.0.1:8000/articles/1


# QUERY PARAMETER
@api.get(
        "/articles_with_query",
        status_code=status.HTTP_200_OK,
        name="Filtre sur le prix",
        tags=['Articles'])
def get_item_with_query(price_threshold: int = Query(...)):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    query = "select * from article where price >= ?"
    c.execute(query, (price_threshold, ))
    result = c.fetchone()
    if not result:
        raise HTTPException(
            status_code=404,
            detail="Produit introuvable",
        )
    return {
        "data": result
    }
# curl -X GET http://127.0.0.1:8000/articles_with_query?price_threshold=100


# Création de mes propres erreur
class MyException(Exception):
    def __init__(self, name: str, date: str):
        self.name = name
        self.date = date

# comment l'erreur renvoie les données


@api.exception_handler(MyException)
def MyExceptionHandler(request: Request, exception: MyException):
    return JSONResponse(
        status_code=418,
        content={
            "url": str(request.url),
            "name": exception.name,
            "message": "This is an error",
            "date": exception.date
        }
    )


@api.get("/my_custom_excpetion")
def get_my_exception():
    raise MyException(
        name=" my error",
        date=datetime.now().strftime('%y/%m/%d - %H:%M')
    )

# GESTION DES CODES HTTP REPONSES


responses = {
    200: {"description": "OK"},
    404: {"description": "Item not found"},
    302: {"description": "The item was moved"},
    403: {"description": "Not enough privileges"},
}


@api.get('/thing', responses=responses)
def get_thing():
    return {
        'data': 'hello world'
    }