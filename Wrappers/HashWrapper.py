from ADT_Christoph.HashTable.HashTable import HashTable
from Enums import HashTableType
from OutputGenerator import printHashTable


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
        self.__ADT.type = HashTableType.Type2

    def create(self):
        return self.__ADT.createHashTable()

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
        self.__ADT.type = HashTableType.Type3

    def create(self):
        return self.__ADT.createHashTable()

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

