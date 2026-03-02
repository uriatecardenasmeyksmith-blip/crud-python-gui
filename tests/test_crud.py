import sys
import os
# Esto le dice a Python que busque en la carpeta de arriba
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crud import create, read, update, delete

def test_create():
    assert create() == True
