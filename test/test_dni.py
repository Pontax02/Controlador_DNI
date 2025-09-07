import pytest
from src.controlador import Controlador


def test_numbers_dni():
    
    DNI ="62007419V"
    test = Controlador(DNI)
    assert True== test.checkNumbersDni()

def test_letter_dni():
    
    DNI ="77510958S"
    test = Controlador(DNI)
    assert True== test.checkValidLetter()

def test_fake_numbers_dni():
    
    DNI ="62-R7419V"
    test = Controlador(DNI)
    assert False == test.checkNumbersDni()

def test_fake_letter_dni():
    
    DNI ="775109583"
    test = Controlador(DNI)
    assert False == test.checkValidLetter()