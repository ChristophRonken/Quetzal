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

    def insert(self, searchkey, newItem):
        self.ADT.push(newItem)
        return

    def delete(self, searchkey):
        self.ADT.pop()
        return

    def print(self):
        printStack(self.ADT)
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

    def retrieve(self, searchkey):
        return self.ADT.searchkeyRetrieve(searchkey)

    def print(self):
        printDLC(self.ADT)
        return


class CLCWrapper:
    def __init__(self):
        self.ADT = CircularChain()

    def create(self):
        self.ADT.createChain()
        return

    def insert(self, searchkey, newItem):
        self.ADT.addNode(newItem, searchkey)
        return

    def delete(self, searchkey):
        self.ADT.delete(searchkey)
        return

    def print(self):
        printCLC(self.ADT)
        return


class QueueWrapper:
    def __init__(self):
        self.ADT = Queue()

    def create(self):
        self.ADT.createQueue()
        return

    def insert(self, searchkey, newItem):
        self.ADT.enQueue(newItem)
        return

    def delete(self, searchkey):
        self.ADT.deQueue()
        return

    def print(self):
        printQueue(self.ADT)
        return


class BSTWrapper:

    def __init__(self):
        self.ADT = BinarySearchTree()

    def create(self):
        self.ADT.createSearchTree()
        return

    def insert(self, searchkey, newItem):
        self.ADT.insert(searchkey, newItem)
        return

    def delete(self, searchkey):
        self.ADT.delete(searchkey)
        return

    def print(self):
        printBST(self.ADT)
        return


class HashWrapper:

    def __init__(self):
        self.ADT = HashTable()

    def create(self):
        self.ADT.createHashTable()
        return

    def insert(self, searchkey, newItem):
        self.ADT.insert(searchkey, newItem)
        return

    def delete(self, searchkey):
        self.ADT.delete(searchkey)
        return

    def print(self):
        printHashTable(self.ADT)
        return
