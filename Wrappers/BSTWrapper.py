from ADT_Christoph.BinarySearchTree.BinarySearchTree import BinarySearchTree
from OutputGenerators.BSTOG import printBST


class BSTWrapper:

    def __init__(self):
        self.__ADT = BinarySearchTree()

    def create(self):
        return self.__ADT.createSearchTree()

    def insert(self, searchkey, newItem):
        return self.__ADT.insert(searchkey, newItem)

    def delete(self, searchkey):
        return self.__ADT.delete(searchkey)

    def retrieve(self, searchkey):
        if self.__ADT.retrieve(searchkey)[0]:
            return self.__ADT.retrieve(searchkey)[1]
        return False

    def print(self):
        return printBST(self.__ADT)

