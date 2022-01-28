from Immatriculation import Immatriculation


class Vehicule:
    def __init__(self, marque, modele, prix, couleur, immatriculation):
        self.__marque: str = marque
        self.__modele: str = modele
        self.__prix: float = prix
        self.__couleur: str = couleur
        self.__immatriculation: Immatriculation = immatriculation

    @property
    def marque(self):
        return self.__marque

    @property
    def modele(self):
        return self.__modele

    @property
    def prix(self):
        return self.__prix

    @property
    def couleur(self):
        return self.__couleur

    @property
    def immatriculation(self):
        return self.__immatriculation
