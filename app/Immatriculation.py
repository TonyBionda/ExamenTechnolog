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
