from ADT_Christoph.DoublyLinkedChain.DoublyLinkedChain import DoublyLinkedChain
from OutputGenerator import printDLC


class DLCWrapper:

    def __init__(self):
        self.__ADT = DoublyLinkedChain()

    def create(self):
        return self.__ADT.createChain()

    def isEmpty(self):
        return self.__ADT.isEmpty()

    def insert(self, searchkey, newItem):
        return self.__ADT.add(searchkey, newItem)

    def delete(self, searchkey):
        return self.__ADT.remove(searchkey)

    def destroy(self):
        return self.__ADT.destroyChain()

    def retrieve(self, searchkey):
        if self.__ADT.searchkeyRetrieve(searchkey)[0]:
            return self.__ADT.searchkeyRetrieve(searchkey)[1]
        return False

    def print(self):
        return printDLC(self.__ADT)
