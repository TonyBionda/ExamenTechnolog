from typing import Optional
from fastapi import FastAPI
from pymongo import MongoClient
from Vehicule import Vehicule
from Immatriculation import Immatriculation

app = FastAPI()


@app.get("/")
def read_root():
    return {"Tapez": "/vehicules"}


def database():
    client = MongoClient(host="mongodb")
    db = client.registre
    return db


@app.get("/vehicules")
def fetch_vehicules():
    db = database()
    results = db.vehicules.find()
    vehicules = []
    for result in results:
        v = Vehicule(
            result["marque"],
            result["modele"],
            result["prix"],
            result["couleur"],
            Immatriculation(
                result["immatriculation"]["numero_immat"],
                result["immatriculation"]["numero_departement"],
            ),
        )
        vehicules.append(v)
    return vehicules


@app.get("/vehicules/prix")
def fetch_personne_by_prix(eq: Optional[float] = None, gt: Optional[float] = None, lt: Optional[float] = None):
    db = database()
    array = []
    results = None
    if eq is not None:
        results = db.vehicules.find({"prix": eq})
    elif gt is not None and lt is not None:
        results = db.vehicules.find({"prix": {"$gt": gt, "$lt": lt}})
    elif gt is not None:
        results = db.vehicules.find({"prix": {"$gt": gt}})
    elif lt is not None:
        results = db.vehicules.find({"prix": {"$lt": lt}})
    if results is None:
        return {"error": "Pas de résultat"}
    for result in results:
        v = Vehicule(
            result["marque"],
            result["modele"],
            result["prix"],
            result["couleur"],
            Immatriculation(
                result["immatriculation"]["numero_immat"],
                result["immatriculation"]["numero_departement"],
            ),
        )
        array.append(v)
    return array
