from simple_calculator import add
from simple_calculator import multiply
import pytest 

#adding zeros
def test_add():
    result = add(0, 0)
    assert result == 0

#adding negatives 
def test_add():
    result = add(-1, -1)
    assert result == -2 

#adding positives 
def test_add():
    result = add(4, 5)
    assert result == 9

#adding multiple numbers 
def test_add():
    result = add(1, 2, 3, 4)
    assert result == 10
    
 #multiplying two numbers
def test_multiply():
    result = multiply(1, 2)
    assert result == 2 

#multiplying multiple numbers
def test_multiply():
    result = multiply(1, 2, 3, 4) 
    assert result == 24  