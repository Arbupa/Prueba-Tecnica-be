# import all the libraries needed
import uuid
import random


class Data:

    def __init__(self, name: str, description: str, symbol: str) -> None:
        # generates uuid randomly
        self.uuid = uuid.uuid4()
        self.name = name
        self.description = description
        self.symbol = symbol
        # here I use list comprehension to create 50 numbers randomly with a max value of 1000
        # and returns the values within a list.
        self.values = [random.randrange(1, 1000, 1) for i in range(50)]
