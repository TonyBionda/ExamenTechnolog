from Immatriculation import Immatriculation


def test_immatriculation_constructor():
    immat = Immatriculation("AB-123-CD", "13")
    assert immat.numero_immat == "AB-123-CD"
    assert immat.numero_departement == "13"


def test_immatriculation_tostring():
    immat = Immatriculation("AB-123-CD", "13")
    assert str(immat) == "AB-123-CD 13"


def test_immatriculation_isvalid():
    immat = Immatriculation("AB-123-CD", "75")
    assert immat.is_valid()
    immat = Immatriculation("AZ-123-CD3", "13")
    assert not immat.is_valid()
