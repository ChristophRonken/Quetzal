from ADT_Christoph.Stack.Stack import Stack
from ADT_Christoph.DoublyLinkedChain.DoublyLinkedChain import DoublyLinkedChain
from ADT_Christoph.HashTable.HashTable import HashTable, HashTableType
from ADT_Christoph.BinarySearchTree.BinarySearchTree import BinarySearchTree
from ADT_Cedric.Queue import Queue
from ADT_Cedric.CircularChain import CircularChain
from OutputGenerator import printStack, printQueue, printHashTable, printBST, printDLC, printCLC


class StackWrapper:

    def __init__(self):
        self.__ADT = Stack()
        return

    def create(self):
        return

    def isEmpty(self):
        return self.__ADT.isEmpty()

    def insert(self, searchkey, newItem):
        return self.__ADT.push(newItem)

    def delete(self, searchkey):
        return self.__ADT.pop()

    def retrieve(self, searchkey):
        return self.__ADT.getTop()

    def print(self):
        return printStack(self.__ADT)


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

    def retrieve(self, searchkey):
        return self.__ADT.searchkeyRetrieve(searchkey)

    def print(self):
        return printDLC(self.__ADT)


class CLCWrapper:
    def __init__(self):
        self.__ADT = CircularChain()

    def create(self):
        return self.__ADT.createChain()

    def insert(self, searchkey, newItem):
        return self.__ADT.addNode(newItem, searchkey)

    def delete(self, searchkey):
        return self.__ADT.delete(searchkey)

    def print(self):
        return printCLC(self.__ADT)


class QueueWrapper:
    def __init__(self):
        self.__ADT = Queue()

    def create(self):
        return self.__ADT.createQueue()

    def isEmpty(self):
        return self.__ADT.isEmpty()

    def insert(self, searchkey, newItem):
        return self.__ADT.enQueue(newItem)

    def delete(self, searchkey):
        return self.__ADT.deQueue()

    def retrieve(self, searchkey):
        return self.__ADT.getFront()

    def print(self):
        return printQueue(self.__ADT)


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
        return self.__ADT.retrieve(searchkey)

    def print(self):
        return printBST(self.__ADT)


class HLinWrapper:

    def __init__(self):
        self.__ADT = HashTable()
        self.__ADT.type = HashTableType.Type1

    def create(self):
        return self.__ADT.createHashTable()

    def insert(self, searchkey, newItem):
        return self.__ADT.insert(searchkey, newItem)

    def delete(self, searchkey):
        return self.__ADT.delete(searchkey)

    def retrieve(self, searchkey):
        return self.__ADT.retrieve(searchkey)

    def print(self):
        return printHashTable(self.__ADT)


class HQuadWrapper:

    def __init__(self):
        self.__ADT = HashTable()
        self.__ADT.type = HashTableType.Type2

    def create(self):
        return self.__ADT.createHashTable()

    def insert(self, searchkey, newItem):
        return self.__ADT.insert(searchkey, newItem)

    def delete(self, searchkey):
        return self.__ADT.delete(searchkey)

    def retrieve(self, searchkey):
        return self.__ADT.retrieve(searchkey)

    def print(self):
        return printHashTable(self.__ADT)


class HSepWrapper:

    def __init__(self):
        self.__ADT = HashTable()
        self.__ADT.type = HashTableType.Type3

    def create(self):
        return self.__ADT.createHashTable()

    def insert(self, searchkey, newItem):
        return self.__ADT.insert(searchkey, newItem)

    def delete(self, searchkey):
        return self.__ADT.delete(searchkey)

    def retrieve(self, searchkey):
        return self.__ADT.retrieve(searchkey)

    def print(self):
        return printHashTable(self.__ADT)

