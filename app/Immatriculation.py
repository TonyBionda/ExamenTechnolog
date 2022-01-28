import re


class Immatriculation:
    def __init__(self, numero_immat, numero_departement):
        self.__numero_immat = numero_immat
        self.__numero_departement = numero_departement

    @property
    def numero_immat(self):
        return self.__numero_immat

    @property
    def numero_departement(self):
        return self.__numero_departement

    def __str__(self):
        return self.__numero_immat + " " + self.__numero_departement

    def is_valid(self):
        # Example : "NE-212-BA 91" est valide
        if re.match("^[A-Z]{2}-[0-9]{3}-[A-Z]{2} [0-9]{2}$", self.__str__()):
            return True
        return False
