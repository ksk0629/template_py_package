import pytest
from src.example_package.example import add_one

@pytest.fixture
def example_fixture():
    print()
    print("The function havinfg ficture signature will run before each test.")
    return None


@pytest.mark.add_number
@pytest.mark.parametrize("number, output",[(1, 2), (2, 3), (3, 4), (5, 6)])
def test_with_positive_numbers(example_fixture, number, output):
    result = add_one(number)
    assert result == output


@pytest.mark.add_number
@pytest.mark.parametrize("number, output",[(-4, -3), (-3, -2), (-2, -1), (-1, 0)])
def test_with_negative_number(example_fixture, number, output):
    result = add_one(number)
    assert result == output
    

@pytest.mark.add_number
def test_with_zero(example_fixture):
    zero = 0
    result = add_one(zero)
    assert result == zero + 1
