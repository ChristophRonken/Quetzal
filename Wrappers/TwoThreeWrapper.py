from ADT_Cedric.TwoThree import Tree
from OutputGenerators.TwoThreeOG import print23


class TwoThreeWrapper:

    def __init__(self):
        self.__ADT = Tree()
        return

    def create(self):
        self.__ADT.createTree()
        return

    def isEmpty(self):
        return self.__ADT.isEmpty()

    def insert(self, searchkey, newItem):
        return self.__ADT.treeInsert(searchkey, newItem)

    def delete(self, searchkey):
        return self.__ADT.treeDelete(searchkey)

    def destroy(self):
        return self.__ADT.destroyTree()

    def retrieve(self, searchkey):
        if self.__ADT.treeRetrieve(searchkey)[0]:
            return self.__ADT.treeRetrieve(searchkey)[1]
        return False

    def print(self):
        return print23(self.__ADT)
