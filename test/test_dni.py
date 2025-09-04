import pytest
from src.controlador import Controlador


def test_dni():
    
    DNI ="09872653"
    test = Controlador(DNI)
    assert "09872653H" == test.getDNI()