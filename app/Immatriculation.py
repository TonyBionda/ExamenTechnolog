import re


class Immatriculation:
    def __init__(self, numero_immat, numero_departement):
        self.__numero_immat: str = numero_immat
        self.__numero_departement: str = numero_departement

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
        # Les deux derniers numéro doivent former 75, 77, 78, 91, 92, 93, 94, ou 95
        if re.match("^[A-Z]{2}-[0-9]{3}-[A-Z]{2} [0-9]{2}$", self.__str__()) \
                and self.__numero_departement in ["75", "77", "78", "91", "92", "93", "94", "95"]:
            return True
        return False
