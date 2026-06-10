from src.calculator import add, subtract
def test_add_positive_numbers():
    
    assert add(2, 3) == 5
    
    assert add(-1, 1) == 0
    
    assert add(5, 0) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5
    assert add(-1, -1) == -2
    assert add(-5, 0) == -5

def test_subtract_positive_numbers():

    assert subtract(5, 3) == 2

    assert subtract(20, 15) == 5

    assert subtract(5, 0) == 5


def test_subtract_negative_numbers():

    assert subtract(-5, -3) == -2

    assert subtract(-10, -5) == -5

    assert subtract(-5, 5) == -10