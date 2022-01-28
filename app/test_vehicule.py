from Vehicule import Vehicule
from Immatriculation import Immatriculation


def test_vehicule_constructor():
    vehicle = Vehicule("Citroën", "C3", 10900, "noire", Immatriculation("AB-123-CD", "91"))
    assert vehicle.marque == "Citroën"
    assert vehicle.modele == "C3"
    assert vehicle.prix == 10900
    assert vehicle.couleur == "noire"
    assert str(vehicle.immatriculation) == str(Immatriculation("AB-123-CD", "91"))


def test_vehicule_tostring():
    vehicle = Vehicule("Citroën", "C3", 10900, "noire", Immatriculation("AB-123-CD", "91"))
    assert str(vehicle) == "Citroën C3 noire / Prix: 10900€ / Immatriculation: AB-123-CD 91"


def test_vehicule_is_valid():
    vehicle = Vehicule("Citroën", "C3", 10900, "noire", Immatriculation("AB-123-CD", "91"))
    assert vehicle.is_valid() is True
    vehicle = Vehicule("Citroën", "C3", 10900, "noire", Immatriculation("AB-12A-CD", "54"))
    assert vehicle.is_valid() is False
