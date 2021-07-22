# import all the libraries needed
from dbcrud import *
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


# data = Data("My Company", "aslkdjlask dsalkdjas",
#             "123asd", ["asdas", "asdsa", "asdas"])
# data1 = Data("My Company", "aslkdjlask dsalkdjas",
#              "123asd2", ["asdas", "asdsa", "asdas"])
# data2 = Data("My Company", "aslkdjlask dsalkdjas",
#              "123asd2", ["asdas", "asdsa", "asdas"])
data = Data("My Company", "aslkdjlask dsalkdjas", "123asd2")


# print(data.uuid)
# print(data2.uuid)
# insert(data)
# insert(data1)
# insert(data2)
# get_all_data()

# for element in data4.values:
#     print(element)
# print(type(data4.values))

# insert(data)
# all_data = get_all_data()
# # print(get_data_by_id('60f9910287bb259af8f3a78e'))
# # print(all_data)
# for elem in all_data:
#     print(elem['_id'])
# update_data('60f9910287bb259af8f3a78e')
strin = "asd asd asd qwe fdg qwe"
print(len(strin))
