# tests/test_calculator.py

from src.calculator import add, subtract

def test_add():
    assert add(3, 4) == 7
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(-1, -1) == 0
