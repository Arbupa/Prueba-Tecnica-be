from dataclass import Data
import pytest


# testing if is instance of the class
def test_instance_class():
    my_class = Data("", "", "")
    assert isinstance(my_class, Data)


# testing if is instance of another class
def test_instance_class2():
    class Fake():
        def __init__(self) -> None:
            pass

    my_class = Fake()
    if not isinstance(my_class, Data):
        assert AssertionError("The object comparised is from another class")
    else:
        return "their equal"
