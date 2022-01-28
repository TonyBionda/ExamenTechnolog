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

    def __str__(self):
        # Exemple : "Citroën C3 noire / Prix: 10900€ / Immatriculation: AB-123-CD"
        return f"{self.__marque} {self.__modele} {self.__couleur} / Prix: {self.__prix}€ / Immatriculation: " \
               f"{str(self.__immatriculation)}"

    def is_valid(self):
        # Est valide si l'immatriculation est valide,
        # si la couleur est blanche, noire ou grise,
        # et si la marque n'est pas FakeBrand.
        return self.__immatriculation.is_valid() and \
               self.__couleur in ["blanche", "noire", "grise"] and \
               self.__marque != "FakeBrand"
