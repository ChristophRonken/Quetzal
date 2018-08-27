from ADT_Christoph.HashTable.HashTable import HashTable
from Enums import HashTableType
from OutputGenerators.HashOG import printHashTable


class HLinWrapper:

    def __init__(self):
        self.__ADT = HashTable()
        self.__ADT.type = HashTableType.Linear

    def create(self):
        return self.__ADT.createHashTable()

    def isEmpty(self):
        return self.__ADT.isEmpty()

    def insert(self, searchkey, newItem):
        return self.__ADT.insert(searchkey, newItem)

    def delete(self, searchkey):
        return self.__ADT.delete(searchkey)

    def destroy(self):
        return self.__ADT.destroyHashTable()

    def retrieve(self, searchkey):
        if self.__ADT.retrieve(searchkey)[0]:
            return self.__ADT.retrieve(searchkey)[1]
        return False

    def print(self):
        return printHashTable(self.__ADT)


class HQuadWrapper:

    def __init__(self):
        self.__ADT = HashTable()
        self.__ADT.type = HashTableType.Quadratic

    def create(self):
        return self.__ADT.createHashTable()

    def isEmpty(self):
        return self.__ADT.isEmpty()

    def insert(self, searchkey, newItem):
        return self.__ADT.insert(searchkey, newItem)

    def delete(self, searchkey):
        return self.__ADT.delete(searchkey)

    def destroy(self):
        return self.__ADT.destroyHashTable()

    def retrieve(self, searchkey):
        if self.__ADT.retrieve(searchkey)[0]:
            return self.__ADT.retrieve(searchkey)[1]
        return False

    def print(self):
        return printHashTable(self.__ADT)


class HSepWrapper:

    def __init__(self):
        self.__ADT = HashTable()
        self.__ADT.type = HashTableType.Seperate

    def create(self):
        return self.__ADT.createHashTable()

    def isEmpty(self):
        return self.__ADT.isEmpty()

    def insert(self, searchkey, newItem):
        return self.__ADT.insert(searchkey, newItem)

    def delete(self, searchkey):
        return self.__ADT.delete(searchkey)

    def destroy(self):
        return self.__ADT.destroyHashTable()

    def retrieve(self, searchkey):
        if self.__ADT.retrieve(searchkey)[0]:
            return self.__ADT.retrieve(searchkey)[1]
        return False

    def print(self):
        return printHashTable(self.__ADT)

