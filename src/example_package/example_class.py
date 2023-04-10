class ExampleClass():
    def __init__(self, number: int):
        self.number = number
    
    @property
    def number(self) -> int:
        return self.__number
    
    @number.setter
    def number(self, new_number: int):
        if not isinstance(new_number, int):
            msg = f"The type of a given number must be int, but it is {type(new_number)}"
            raise TypeError(msg)
        self.__number = new_number
