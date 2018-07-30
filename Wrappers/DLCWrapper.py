from ADT_Christoph.DoublyLinkedChain.DoublyLinkedChain import DoublyLinkedChain
from OutputGenerators.DLCOG import printDLC


class DLCWrapper:

    def __init__(self):
        self.ADT = DoublyLinkedChain()

    def create(self):
        return self.ADT.createChain()

    def isEmpty(self):
        return self.ADT.isEmpty()

    def insert(self, searchkey, newItem):
        return self.ADT.add(searchkey, newItem)

    def delete(self, searchkey):
        return self.ADT.remove(searchkey)

    def destroy(self):
        return self.ADT.destroyChain()

    def retrieve(self, searchkey):
        if self.ADT.searchkeyRetrieve(searchkey)[0]:
            return self.ADT.searchkeyRetrieve(searchkey)[1]
        return False

    def print(self):
        return printDLC(self.ADT)
