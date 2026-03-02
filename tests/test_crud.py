# tests/test_crud.py
import crud
import pytest

def test_create():
    # Llama a la función del otro archivo y verifica que devuelva True
    assert crud.create() == True

def test_read():
    assert crud.read() == True

def test_update():
    assert crud.update() == True

def test_delete():
    assert crud.delete() == True