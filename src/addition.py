# app.py
# This is a test commit
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0

def sub(a, b):
    return a - b

def test_sub():
    assert sub(2, 1) == 1
    assert sub(1, -1) == 2

def mul(a, b):
    return a * b

def test_mul():
    assert mul(2, 1) == 2
    assert mul(1, -1) == -1

def div(a, b):
    return a / b

def test_div():
    assert div(4, 2) == 2
    assert div(9, 3) == 3
    assert div(-6, 2) == -3

