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


def test_compute_dni():
    
    DNI ="78484464"
    test = Controlador(DNI)
    assert "78484464T" == test.createDni()


def test_compute_dni2():
    
    DNI ="72376173"
    test = Controlador(DNI)
    assert "72376173A" == test.createDni()


def test_compute_dni3():
    
    DNI ="01817200"
    test = Controlador(DNI)
    assert "01817200Q" == test.createDni()

