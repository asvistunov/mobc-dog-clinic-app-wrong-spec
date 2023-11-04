from random import randint

from enum import Enum
from fastapi import FastAPI, Request, Path
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel

app = FastAPI()


class DogType(str, Enum):
    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"


class Dog(BaseModel):
    name: str
    pk: int
    kind: DogType


class Timestamp(BaseModel):
    id: int
    timestamp: int


dogs_db = {
    0: Dog(name='Bob', pk=0, kind='terrier'),
    1: Dog(name='Marli', pk=1, kind='bulldog'),
    2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
    3: Dog(name='Rex', pk=3, kind='dalmatian'),
    4: Dog(name='Pongo', pk=4, kind='dalmatian'),
    5: Dog(name='Tillman', pk=5, kind='bulldog'),
    6: Dog(name='Uga', pk=6, kind='bulldog')
}

post_db = [
    Timestamp(id=0, timestamp=12),
    Timestamp(id=1, timestamp=10)
]


# @app.get('/')
# def root():
#     return 'sucess'

# @app.post('/post')
# def post():
#     timestamp = Timestamp(id=len(post_db) + 1, timestamp=randint(1, 100))
#     post_db.append(timestamp)
#     return timestamp

@app.get('/dog')
def list_dogs(kind: DogType):
    return [dog for dog in dogs_db.values() if dog.kind == kind]


@app.post('/dog')
def add_dog(dog: Dog):
    dogs_db[dog.pk] = dog
    return dog

@app.get('/dog/{pk}')
def get_dog_by_pk(pk: str):
    return dogs_db[pk]

@app.patch('/dog/{pk}')
def update_dog_by_pk(pk: int, dog: Dog):
    dogs_db[pk] = dog
    return dog

