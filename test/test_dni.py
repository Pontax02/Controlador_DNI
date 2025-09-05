import pytest
from controlador import Controlador


def test_dni():
    
    DNI ="09872653"
    test = Controlador(DNI)
    assert True== test.checkNumbersDni()