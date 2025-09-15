import math
import pytest
import calculator as calc

def testAdd():
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0

def testSubtract():
    assert calc.subtract(10, 5) == 5
    assert calc.subtract(0, 3) == -3

def testMultiply():
    assert calc.multiply(5, 5) == 25
    assert calc.multiply(-2, 5) == -10

def testDivide():
    assert calc.divide(25, 5) == 5
    assert math.isclose(calc.divide(3, 2), 1.5)

def testDivideByZero():
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)