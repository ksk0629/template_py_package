import pytest
from src.example_package.example_class import ExampleClass


class TestExampleClassClass():
    def setup_method(self, method):
        print(f"TEST START: method {method.__name__}")

    def teardown_method(self, method):
        print(f"TEST END: method {method.__name__}")
    
    @pytest.mark.example_class
    @pytest.mark.parametrize("whole_number",[1, -1, 2, -2, 0])
    def test_integer(self, whole_number):
        example_class = ExampleClass(whole_number)
        assert example_class.number == whole_number


    @pytest.mark.example_class
    @pytest.mark.parametrize("float_number",[0.1, -0.1, 0.2, -0.2, float(0.0)])
    def test_with_floats(self, float_number):
        with pytest.raises(TypeError):
            ExampleClass(float_number)
