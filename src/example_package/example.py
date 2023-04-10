from src.example_package.example_class import ExampleClass

def add_one(number: int) -> int:
    return number + 1


def add_one_with_example_class(number: int) -> int:
    example_class = ExampleClass(number)
    example_class.number = add_one(example_class.number)
    return example_class.number
