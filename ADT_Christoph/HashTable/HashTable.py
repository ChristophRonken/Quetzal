from enum import Enum, auto
from ADT_Christoph.DoublyLinkedChain.DoublyLinkedChain import DoublyLinkedChain


class HashTableType(Enum):
    Type1 = auto()
    Type2 = auto()
    Type3 = auto()


class Bucket:
    def __init__(self, searchkey=None, newItem=None, deleted=False):
        self.deleted = deleted
        self.searchkey = searchkey
        self.item = newItem

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Bucket):
            return self.deleted is other.deleted and self.item is other.item and self.searchkey is other.searchkey
        return False


class HashTable:

    def __init__(self):
        self.type = HashTableType.Type3
        self.size = 101
        self.table = [None] * self.size

    def createHashTable(self):
        if self.type != HashTableType.Type3:
            for i in range(0, len(self.table)):
                self.table[i] = Bucket()
        else:
            for i in range(0, len(self.table)):
                self.table[i] = DoublyLinkedChain()
                self.table[i].createChain()
        return True

    def destroyHashTable(self):
        if not self.__exists():
            return False

        if self.type != HashTableType.Type3:
            for i in range(0, len(self.table)):
                if self.type == HashTableType.Type3 and not self.table[i].deleted:
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
                self.table[i].destroyChain()
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

        elif self.type != HashTableType.Type3:
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

        elif self.type != HashTableType.Type3:
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
        if self.type == HashTableType.Type1:
            probeNumber = 0
            while self.table[(index + probeNumber) % self.getLength()] != Bucket() and self.table[(index + probeNumber) % self.getLength()] != Bucket(None, True):
                probeNumber += 1
                if probeNumber == self.getLength():
                    return False
            self.table[(index + probeNumber) % self.getLength()].item = newItem
            self.table[(index + probeNumber) % self.getLength()].searchkey = searchkey
            return True

        elif self.type == HashTableType.Type2:
            probeNumber = 0
            while self.table[(index + probeNumber ** 2) % self.getLength()] != Bucket() and self.table[(index + probeNumber ** 2) % self.getLength()] != Bucket(None, True):
                probeNumber += 1
                if probeNumber == self.getLength():
                    return False
            self.table[(index + probeNumber ** 2) % self.getLength()].item = newItem
            self.table[(index + probeNumber ** 2) % self.getLength()].searchkey = searchkey
            return True

        elif self.type == HashTableType.Type3:
            self.table[index].add(searchkey, newItem)
            return True

        return False

    def retrieve(self, searchkey):
        if not self.__exists():
            return False
        if self.isEmpty():
            return False

        index = self.__hash(searchkey)
        if self.type == HashTableType.Type1:
            probeNumber = 0
            while self.table[(index + probeNumber) % self.getLength()].deleted or self.table[(index + probeNumber) % self.getLength()].item:
                if self.table[(index + probeNumber) % self.getLength()] == Bucket(None, True):
                    probeNumber += 1
                    continue

                if self.table[(index + probeNumber) % self.getLength()] == Bucket():
                    probeNumber += 1
                    continue

                if self.table[(index + probeNumber) % self.getLength()].searchkey == searchkey:
                    return self.table[(index + probeNumber) % self.getLength()].item

                probeNumber += 1
                if probeNumber == self.getLength():
                    return False
            return False

        elif self.type == HashTableType.Type2:
            probeNumber = 0
            while self.table[(index + probeNumber ** 2) % self.getLength()].item or self.table[(index + probeNumber) % self.getLength()].deleted:
                if self.table[(index + probeNumber ** 2) % self.getLength()] == Bucket(None, True):
                    probeNumber += 1
                    continue

                if self.table[(index + probeNumber ** 2) % self.getLength()] == Bucket():
                    probeNumber += 1
                    continue

                if self.table[(index + probeNumber ** 2) % self.getLength()].searchkey == searchkey:
                    return self.table[(index + probeNumber ** 2) % self.getLength()].item

                probeNumber += 1
                if probeNumber == self.getLength():
                    return False
            return False

        elif self.type == HashTableType.Type3:
            return self.table[index].searchkeyRetrieve(searchkey)

    def delete(self, searchkey):
        if not self.__exists():
            print("notexist")
            return False

        if self.isEmpty():
            print("isempty")
            return False

        index = self.__hash(searchkey)
        if self.type == HashTableType.Type1:
            probeNumber = 0
            while self.table[(index + probeNumber) % self.getLength()].searchkey is not None or self.table[(index + probeNumber) % self.getLength()].deleted:
                if self.table[(index + probeNumber) % self.getLength()] == Bucket(None, True):
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

        elif self.type == HashTableType.Type2:
            probeNumber = 0
            while self.table[(index + probeNumber ** 2) % self.getLength()].searchkey is not None or self.table[
                (index + probeNumber) % self.getLength()].deleted:
                if self.table[(index + probeNumber ** 2) % self.getLength()] == Bucket(None, True):
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

        elif self.type == HashTableType.Type3:
            return self.table[index].remove(searchkey)

    def print(self):
        for i in range(0, len(self.table)):
            if self.table[i] and self.table[i].item and self.type == HashTableType.Type3:
                self.table[i].item.printChain()
            else:
                print(self.table[i].searchkey)
        return