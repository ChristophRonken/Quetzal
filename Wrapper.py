from ADT_Christoph.Stack.Stack import Stack
from ADT_Christoph.DoublyLinkedChain.DoublyLinkedChain import DoublyLinkedChain


class StackWrapper:

    def __init__(self):
        self.ADT = Stack()

    def create(self):
        return

    def insert(self, newItem):
        self.ADT.push(newItem)
        return

    def delete(self):
        self.ADT.pop()
        return

    def print(self):
        return


class DLCWrapper:

    def __init__(self):
        self.ADT = DoublyLinkedChain()

    def create(self):
        self.ADT.createChain()

    def insert(self, searchkey, newItem):
        self.ADT.add(searchkey, newItem)
        return

    def delete(self, searchkey):
        self.ADT.remove(searchkey)
        return

    def print(self):
        return
