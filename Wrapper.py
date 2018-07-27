from ADT_Christoph.Stack.Stack import Stack
from ADT_Christoph.DoublyLinkedChain.DoublyLinkedChain import DoublyLinkedChain
from ADT_Christoph.HashTable.HashTable import HashTable
from ADT_Christoph.BinarySearchTree.BinarySearchTree import BinarySearchTree
from ADT_Cedric.Queue import Queue
from ADT_Cedric.CircularChain import CircularChain
from OutputGenerator import printStack, printQueue, printHashTable, printBST, printDLC, printCLC


class StackWrapper:

    def __init__(self):
        self.ADT = Stack()
        return

    def create(self):
        return

    def isEmpty(self):
        return self.ADT.isEmpty()

    def insert(self, searchkey, newItem):
        return self.ADT.push(newItem)

    def delete(self, searchkey):
        return self.ADT.pop()

    def retrieve(self):
        return self.ADT.getTop()

    def print(self):
        return printStack(self.ADT)


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

    def retrieve(self, searchkey=None):
        return self.ADT.searchkeyRetrieve(searchkey)

    def print(self):
        return printDLC(self.ADT)


class CLCWrapper:
    def __init__(self):
        self.ADT = CircularChain()

    def create(self):
        return self.ADT.createChain()

    def insert(self, searchkey, newItem):
        return self.ADT.addNode(newItem, searchkey)

    def delete(self, searchkey):
        return self.ADT.delete(searchkey)

    def print(self):
        return printCLC(self.ADT)


class QueueWrapper:
    def __init__(self):
        self.ADT = Queue()

    def create(self):
        return self.ADT.createQueue()

    def isEmpty(self):
        return self.ADT.isEmpty()

    def insert(self, searchkey, newItem):
        return self.ADT.enQueue(newItem)

    def delete(self, searchkey):
        return self.ADT.deQueue()

    def retrieve(self):
        return self.ADT.getFront()

    def print(self):
        return printQueue(self.ADT)


class BSTWrapper:

    def __init__(self):
        self.ADT = BinarySearchTree()

    def create(self):
        return self.ADT.createSearchTree()

    def insert(self, searchkey, newItem):
        return self.ADT.insert(searchkey, newItem)

    def delete(self, searchkey):
        return self.ADT.delete(searchkey)

    def print(self):
        return printBST(self.ADT)


class HashWrapper:

    def __init__(self):
        self.ADT = HashTable()

    def create(self):
        return self.ADT.createHashTable()

    def insert(self, searchkey, newItem):
        return self.ADT.insert(searchkey, newItem)

    def delete(self, searchkey):
        return self.ADT.delete(searchkey)

    def print(self):
        return printHashTable(self.ADT)
