import sys
import os

# Esto le dice a GitHub: "Sube un nivel y busca ahí el archivo crud.py"
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crud import create, read, update, delete

def test_create():
    assert create() == True

def test_read():
    assert read() == True