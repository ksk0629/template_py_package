import pytest
from src.example_package.example import add_one


def test_with_positive_number():
    positive_number = 1
    result = add_one(positive_number)
    assert result == positive_number + 1


def test_with_negative_number():
    negative_number = -1
    result = add_one(negative_number)
    assert result == negative_number + 1
    

def test_with_zero():
    zero = 0
    result = add_one(zero)
    assert result == zero + 1
