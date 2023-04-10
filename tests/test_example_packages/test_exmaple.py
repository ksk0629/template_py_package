import pytest
from src.example_package.example import add_one

@pytest.fixture
def example_fixture():
    print()
    print("The function havinfg ficture signature will run before each test.")
    return None


@pytest.mark.add_number
def test_with_positive_number(example_fixture):
    positive_number = 1
    result = add_one(positive_number)
    assert result == positive_number + 1


@pytest.mark.add_number
def test_with_negative_number(example_fixture):
    negative_number = -1
    result = add_one(negative_number)
    assert result == negative_number + 1
    

@pytest.mark.add_number
def test_with_zero(example_fixture):
    zero = 0
    result = add_one(zero)
    assert result == zero + 1
