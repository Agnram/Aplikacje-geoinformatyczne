import pytest
from cw4.actual_source_code.for_testing import add, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)

@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5),
    (20, 5, 4),
    (30, -3, -10),
    (-20, 5, -4)
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected