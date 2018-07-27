
class Node:
    def __init__(self, searchkey, item, next=None, prev=None):
        self.searchkey = searchkey
        self.next = next
        self.prev = prev
        self.item = item

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Node):
            return self.item is other.item and self.searchkey is other.searchkey and self.next is other.next and self.prev is other.prev
        return False


class DoublyLinkedChain:

    def __init__(self):
        self.head = None
        self.tail = None

    def createChain(self):
        if not self.exists():
            self.head = Node(None, None)
            self.tail = Node(None, None)
            self.head.next = self.tail
            self.tail.prev = self.head
            return True
        return False

    def destroyChain(self):
        if not self.exists():
            return
        while not self.isEmpty():
            self.removeFirst()
        self.head = None
        self.tail = None
        return

    def exists(self):
        if self.head and self.tail:
            return True
        else:
            return False

    def isInChain(self, searchkey):
        if self.exists():
            if self.isEmpty():
                return False
            searchNode = self.head.next
            while searchNode.searchkey != searchkey:
                searchNode = searchNode.next
                if searchNode == self.tail:
                    return False
            return True
        return False

    def isEmpty(self):
        if self.exists():
            return self.head.next == self.tail and self.tail.prev == self.head
        return False

    def add(self, searchkey, newItem):
        if self.exists():
            newNode = Node(searchkey, newItem)
            if self.isEmpty():
                newNode.prev = self.head
                newNode.next = self.tail
                self.head.next = newNode
                self.tail.prev = newNode
                return True
            insertNode = self.head.next
            while insertNode.searchkey < newNode.searchkey:
                if insertNode.next == self.tail:
                    newNode.next = self.tail
                    newNode.prev = self.tail.prev
                    newNode.prev.next = newNode
                    newNode.next.prev = newNode
                    return True
                insertNode = insertNode.next
            newNode.next = insertNode
            newNode.prev = insertNode.prev
            newNode.prev.next = newNode
            newNode.next.prev = newNode
            return True
        return False

    def addFirst(self, searchkey, newItem):
        if self.exists():
            newNode = Node(searchkey, newItem)
            if self.isEmpty():
                newNode.prev = self.head
                newNode.next = self.tail
                self.head.next = newNode
                self.tail.prev = newNode
            else:
                newNode.prev = self.head
                newNode.next = self.head.next
                self.head.next.prev = newNode
                self.head.next = newNode
            return True
        return False

    def addLast(self, searchkey, newItem):
        if self.exists():
            newNode = Node(searchkey, newItem)
            if self.isEmpty():
                newNode.prev = self.head
                newNode.next = self.tail
                self.head.next = newNode
                self.tail.prev = newNode
            else:
                newNode.prev = self.tail.prev
                newNode.next = self.tail
                self.tail.prev.next = newNode
                self.tail.prev = newNode
            return True
        return False

    def removeLast(self):
        if self.exists():
            if self.isEmpty():
                return False
            else:
                self.tail.prev.item = None
                self.tail.prev.searchkey = None
                self.tail.prev.next = None
                self.tail.prev = self.tail.prev.prev
                self.tail.prev.next.prev = None
                self.tail.prev.next = self.tail
                return True
        return False

    def removeFirst(self):
        if self.exists():
            if self.isEmpty():
                return False
            else:
                self.head.next.item = None
                self.head.next.searchkey = None
                self.head.next.prev = None
                self.head.next = self.head.next.next
                self.head.next.prev.next = None
                self.head.next.prev = self.head
                return True
        return False

    def remove(self, searchkey):
        if self.exists():
            if not self.isInChain(searchkey):
                return False
            else:
                removeNode = self.head.next
                while removeNode.searchkey != searchkey:
                    removeNode = removeNode.next
                removeNode.item = None
                removeNode.searchkey = None
                removeNode.next.prev = removeNode.prev
                removeNode.prev.next = removeNode.next
                removeNode.next = None
                removeNode.prev = None
                return True
        return False

    def printChain(self):
        if self.exists():
            displayNode = self.head
            printString = ""
            while displayNode is not None:
                if displayNode == self.head:
                    printString += "head"
                    printString += " <=> "
                elif displayNode == self.tail:
                    printString += "tail"
                    print(printString)
                    return
                else:
                    printString += str(displayNode.searchkey)
                    printString += " <=> "
                displayNode = displayNode.next

    def searchkeyRetrieve(self, searchkey):
        if searchkey is None:
            if self.exists():
                return self.head.next.item
            return False
        if not self.isInChain(searchkey):
            return False
        else:
            searchNode = self.head.next
            while searchNode.searchkey != searchkey:
                searchNode = searchNode.next
            return searchNode.item
