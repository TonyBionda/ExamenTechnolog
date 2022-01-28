from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()


@app.get("/")
def read_root():
    return {"Tapez": "/vehicules"}


def database():
    client = MongoClient(host="mongodb")
    db = client.registre
    return db
