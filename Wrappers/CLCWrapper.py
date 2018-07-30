from ADT_Cedric.CircularChain import CircularChain
from OutputGenerators.CLCOG import printCLC


class CLCWrapper:
    def __init__(self):
        self.ADT = CircularChain()

    def create(self):
        return self.ADT.createChain()

    def destroy(self):
        return self.ADT.destroyChain()

    def isEmpty(self):
        return self.ADT.isEmpty()

    def insert(self, searchkey, newItem):
        return self.ADT.addNode(newItem, searchkey)

    def delete(self, searchkey):
        return self.ADT.delete(searchkey)

    def retrieve(self, searchkey):
        return self.ADT.retrieve(searchkey)

    def print(self):
        return printCLC(self.ADT)
