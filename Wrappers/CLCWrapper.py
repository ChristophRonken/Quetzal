from ADT_Cedric.CircularChain import CircularChain
from OutputGenerator import printCLC


class CLCWrapper:
    def __init__(self):
        self.__ADT = CircularChain()

    def create(self):
        return self.__ADT.createChain()

    def destroy(self):
        return self.__ADT.destroyChain()

    def isEmpty(self):
        return self.__ADT.isEmpty()

    def insert(self, searchkey, newItem):
        return self.__ADT.addNode(newItem, searchkey)

    def delete(self, searchkey):
        return self.__ADT.delete(searchkey)

    def retrieve(self, searchkey):
        return self.__ADT.retrieve(searchkey)

    def print(self):
        return printCLC(self.__ADT)
