from Enums import HashTableType
from Wrappers.DLCWrapper import DLCWrapper
from Wrappers.CLCWrapper import CLCWrapper
from OutputGenerators.HashOG import printHashTable


class Bucket:
    def __init__(self, searchkey=None, newItem=None, deleted=False):
        self.deleted = deleted
        self.searchkey = searchkey
        self.item = newItem

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Bucket):
            return self.deleted is other.deleted and self.item == other.item and self.searchkey == other.searchkey
        return False


class HashTable:

    def __init__(self):
        self.type = None
        self.size = 101
        self.table = [None] * self.size

    def createHashTable(self):
        if self.type != HashTableType.Seperate:
            for i in range(0, len(self.table)):
                self.table[i] = Bucket()
        else:
            for i in range(0, len(self.table)):
                self.table[i] = DLCWrapper()
                self.table[i].create()
        return True

    def destroyHashTable(self):
        if not self.__exists():
            return False

        if self.type != HashTableType.Seperate:
            for i in range(0, len(self.table)):
                if self.type == HashTableType.Seperate and not self.table[i].deleted:
                    if not self.table[i].item:
                        continue
                    while not self.table[i].item.isEmpty():
                        self.table[i].item.removeLast()
                self.table[i].item = None
                self.table[i].searchkey = None
                self.table[i].deleted = False

            for i in range(0, len(self.table)):
                self.table[i] = None
        else:
            for i in range(0, len(self.table)):
                self.table[i].destroy()
                self.table[i] = None
        return not self.__exists()

    def __hash(self, searchkey):
        return searchkey % self.getLength()

    def __exists(self):
        for i in range(0, len(self.table)):
            if not self.table[i]:
                return False
        return True

    def isEmpty(self):
        if not self.__exists():
            return False

        elif self.type != HashTableType.Seperate:
            for i in range(0, len(self.table)):
                if self.table[i].searchkey:
                    return False
            return True

        else:
            for i in range(0, len(self.table)):
                if not self.table[i].isEmpty():
                    return False

            return True

    def isFull(self):
        if not self.__exists():
            return False

        elif self.type != HashTableType.Seperate:
            for i in range(0, len(self.table)):
                if self.table[i].searchkey is None:
                    return False
            return True

        else:
            return False

    def getLength(self):
        return len(self.table)

    def insert(self, searchkey, newItem):
        if not self.__exists():
            return False

        elif self.isFull():
            return False

        index = self.__hash(searchkey)
        if self.type == HashTableType.Linear:
            probeNumber = 0
            while self.table[(index + probeNumber) % self.getLength()] != Bucket() and self.table[(index + probeNumber) % self.getLength()] != Bucket(None, None, True):
                probeNumber += 1
                if probeNumber == self.getLength():
                    return False
            self.table[(index + probeNumber) % self.getLength()].item = newItem
            self.table[(index + probeNumber) % self.getLength()].searchkey = searchkey
            return True

        elif self.type == HashTableType.Quadratic:
            probeNumber = 0
            while self.table[(index + probeNumber ** 2) % self.getLength()] != Bucket() and self.table[(index + probeNumber ** 2) % self.getLength()] != Bucket(None, None, True):
                probeNumber += 1
                if probeNumber == self.getLength():
                    return False
            self.table[(index + probeNumber ** 2) % self.getLength()].item = newItem
            self.table[(index + probeNumber ** 2) % self.getLength()].searchkey = searchkey
            return True

        elif self.type == HashTableType.Seperate:
            return self.table[index].insert(searchkey, newItem)

        return False

    def retrieve(self, searchkey):
        if not self.__exists():
            return False, None
        if self.isEmpty():
            return False, None

        index = self.__hash(searchkey)
        if self.type == HashTableType.Linear:
            probeNumber = 0
            while self.table[(index + probeNumber) % self.getLength()].deleted or self.table[(index + probeNumber) % self.getLength()].item:
                if self.table[(index + probeNumber) % self.getLength()] == Bucket(None, None, True):
                    probeNumber += 1
                    continue

                if self.table[(index + probeNumber) % self.getLength()] == Bucket():
                    probeNumber += 1
                    continue

                if self.table[(index + probeNumber) % self.getLength()].searchkey == searchkey:
                    return True, self.table[(index + probeNumber) % self.getLength()].item

                probeNumber += 1
                if probeNumber == self.getLength():
                    return False, None
            return False, None

        elif self.type == HashTableType.Quadratic:
            probeNumber = 0
            while self.table[(index + probeNumber ** 2) % self.getLength()].item or self.table[(index + probeNumber) % self.getLength()].deleted:
                if self.table[(index + probeNumber ** 2) % self.getLength()] == Bucket(None, None, True):
                    probeNumber += 1
                    continue

                if self.table[(index + probeNumber ** 2) % self.getLength()] == Bucket():
                    probeNumber += 1
                    continue

                if self.table[(index + probeNumber ** 2) % self.getLength()].searchkey == searchkey:
                    return True, self.table[(index + probeNumber ** 2) % self.getLength()].item

                probeNumber += 1
                if probeNumber == self.getLength():
                    return False, None
            return False, None

        elif self.type == HashTableType.Seperate:
            if not self.table[index].retrieve(searchkey) is False:
                return True, self.table[index].retrieve(searchkey)
            return False, None

    def delete(self, searchkey):
        if not self.__exists():
            return False

        if self.isEmpty():
            return False

        index = self.__hash(searchkey)
        if self.type == HashTableType.Linear:
            probeNumber = 0
            while self.table[(index + probeNumber) % self.getLength()].searchkey is not None or self.table[(index + probeNumber) % self.getLength()].deleted:
                if self.table[(index + probeNumber) % self.getLength()] == Bucket(None, None, True):
                    probeNumber += 1
                    continue

                if self.table[(index + probeNumber) % self.getLength()].searchkey == searchkey:
                    self.table[(index + probeNumber) % self.getLength()].searchkey = None
                    self.table[(index + probeNumber) % self.getLength()].deleted = True
                    self.table[(index + probeNumber) % self.getLength()].item = None
                    return True

                probeNumber += 1
                if probeNumber == self.getLength():
                    return False
            return False

        elif self.type == HashTableType.Quadratic:
            probeNumber = 0
            while self.table[(index + probeNumber ** 2) % self.getLength()].searchkey is not None or self.table[
                (index + probeNumber) % self.getLength()].deleted:
                if self.table[(index + probeNumber ** 2) % self.getLength()] == Bucket(None, None, True):
                    probeNumber += 1
                    continue

                if self.table[(index + probeNumber ** 2) % self.getLength()].searchkey == searchkey:
                    self.table[(index + probeNumber ** 2) % self.getLength()].searchkey = None
                    self.table[(index + probeNumber ** 2) % self.getLength()].deleted = True
                    self.table[(index + probeNumber ** 2) % self.getLength()].item = None
                    return True

                probeNumber += 1
                if probeNumber == self.getLength():
                    return False
            return False

        elif self.type == HashTableType.Seperate:
            return self.table[index].delete(searchkey)

    def print(self):
        for i in range(0, len(self.table)):
            if self.table[i] and self.table[i].item and self.type == HashTableType.Seperate:
                self.table[i].print()
            else:
                print(self.table[i].searchkey)
        return True

