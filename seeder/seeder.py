from pymongo import MongoClient


class MongoSeeder:

    def __init__(self):
        host = 'mongodb'
        client = MongoClient(host=f'{host}')
        self.__db = client.registre

    @property
    def db(self):
        return self.__db

    def seed(self):
        # On clear la collection à chaque fois. On peut bien évidemment choisir de ne pas le faire.
        self.db.vehicules.drop()

        # On ajoute des données valides
        array = []
        vehicle1 = {
            "marque": "Citroën",
            "modele": "C3",
            "prix": 12000,
            "couleur": "grise",
            "immatriculation": {
                "numero_immat": "AB-123-CD",
                "numero_departement": "91"
            }
        }
        vehicle2 = {
            "marque": "Peugeot",
            "modele": "208",
            "prix": 2000,
            "couleur": "noire",
            "immatriculation": {
                "numero_immat": "YR-762-CT",
                "numero_departement": "75"
            }
        }
        array.append(vehicle1)
        array.append(vehicle2)

        self.db.vehicules.insert_many(array)
        cursor = self.db.personnes.find()
        for vehicle in cursor:
            print(vehicle)


print("Remplissage de la base de données...")
MongoSeeder().seed()

client = MongoClient(host="mongodb")
db = client.registre
print("Fait.")
