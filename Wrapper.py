from ADT_Christoph.Stack.Stack import Stack
from ADT_Christoph.DoublyLinkedChain.DoublyLinkedChain import DoublyLinkedChain
from ADT_Christoph.HashTable.HashTable import HashTable
from ADT_Christoph.BinarySearchTree.BinarySearchTree import BinarySearchTree
from ADT_Cedric.Queue import Queue
from ADT_Cedric.CircularChain import CircularChain
from OutputGenerator import printStack, printQueue
import copy


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
        ADTCopy = copy.deepcopy(self.ADT)
        printStack(ADTCopy)
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


class CLCWrapper:
    pass


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
        ADTCopy = copy.deepcopy(self.ADT)
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
        self.ADT.inOrder()
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
        self.ADT.print()
        return
