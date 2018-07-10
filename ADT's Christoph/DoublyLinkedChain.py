
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedChain:

    def __init__(self):
        self.startnode = None
        self.endnode = None
        self.size = None

    def createChain(self):
        self.startnode = Node(None)
        self.endnode = Node(None)
        self.startnode.next = self.endnode
        self.endnode.prev = self.startnode
        self.size = 0

    def destroyChain(self):
        while self.startnode.next != self.endnode and self.endnode.prev != self.startnode:
            self.remove(self.startnode.next.data)
        self.startnode = None
        self.endnode = None
        self.size = None

    def isEmpty(self):
        if self.startnode and self.endnode:
            return self.startnode.next == self.endnode and self.endnode.prev == self.startnode

    def add(self, newnode):
        if self.startnode and self.endnode:
            if not self.retrieve(newnode):
                if newnode.prev is None and newnode.next is None:
                        if self.startnode.next == self.endnode and self.endnode.prev == self.startnode:
                            self.startnode.next = newnode
                            self.endnode.prev = newnode
                            newnode.next = self.endnode
                            newnode.prev = self.startnode
                            self.size += 1
                            return True

                elif newnode.prev is None and newnode.next is not None:
                        if self.startnode.next == newnode.next and newnode.next.prev == self.startnode:
                            self.startnode.next = newnode
                            newnode.next.prev = newnode
                            newnode.prev = self.startnode
                            self.size += 1
                            return True

                elif newnode.prev is not None and newnode.next is None:
                        if newnode.prev.next == self.endnode and self.endnode.prev == newnode.prev:
                            self.endnode.prev = newnode
                            newnode.prev.next = newnode
                            newnode.next = self.endnode
                            self.size += 1
                            return True

                elif newnode.prev is not None and newnode.next is not None:
                        if newnode.prev.next == newnode.next and newnode.next.prev == newnode.prev:
                            newnode.prev.next = newnode
                            newnode.next.prev = newnode
                            self.size += 1
                            return True

        return False

    def addLast(self, data):
        if self.startnode and self.endnode:
            if not self.dataRetrieve(data):
                newnode = Node(data)
                if self.startnode.next == self.endnode and self.endnode.prev == self.startnode:
                    self.startnode.next = newnode
                    self.endnode.prev = newnode
                    newnode.next = self.endnode
                    newnode.prev = self.startnode
                    return True
                else:
                    laatstenode = self.startnode
                    while laatstenode.next != self.endnode:
                        laatstenode = laatstenode.next
                    laatstenode.next = newnode
                    self.endnode.prev = newnode
                    newnode.next = self.endnode
                    newnode.prev = laatstenode
                    return True

        return False

    def remove(self, data):
        if self.startnode and self.endnode:
            if self.dataRetrieve(data):
                deletenode = self.dataRetrieve(data)
                if deletenode.prev is self.startnode and deletenode.next is self.endnode:
                    if self.startnode.next == deletenode and self.endnode.prev == deletenode:
                        self.startnode.next = self.endnode
                        self.endnode.prev = self.startnode
                        deletenode.next = None
                        deletenode.prev = None
                        deletenode.data = None
                        self.size -= 1
                        return True

                elif deletenode.prev is self.startnode and deletenode.next is not None:
                    if self.startnode.next == deletenode and deletenode.next.prev == deletenode:
                        self.startnode.next = deletenode.next
                        deletenode.next.prev = self.startnode
                        deletenode.next = None
                        deletenode.prev = None
                        deletenode.data = None
                        self.size -= 1
                        return True

                elif deletenode.prev is not None and deletenode.next is self.endnode:
                    if deletenode.prev.next == deletenode and self.endnode.prev == deletenode:
                        deletenode.prev.next = self.endnode
                        self.endnode.prev = deletenode.prev
                        deletenode.next = None
                        deletenode.prev = None
                        deletenode.data = None
                        self.size -= 1
                        return True

                elif deletenode.prev is not None and deletenode.next is not None:
                    if deletenode.prev.next == deletenode and deletenode.next.prev == deletenode:
                        deletenode.prev.next = deletenode.next
                        deletenode.next.prev = deletenode.prev
                        deletenode.next = None
                        deletenode.prev = None
                        deletenode.data = None
                        self.size -= 1
                        return True

        return False

    def printChain(self):
        if self.startnode and self.endnode:
            displaynode = self.startnode
            while displaynode is not self.endnode.prev:
                displaynode = displaynode.next
                if displaynode == self.startnode.next:
                    print(displaynode.data)
                    if displaynode.next != self.endnode:
                        print(displaynode.next.data)
                elif displaynode != self.endnode.prev:
                    print(displaynode.prev.data)
                    print(displaynode.data)
                    print(displaynode.next.data)
                elif displaynode == self.endnode.prev:
                    print(displaynode.prev.data)
                    print(displaynode.data)

    def dataRetrieve(self, data):
        searchnode = self.startnode.next
        check = 0
        while searchnode is not self.endnode and check < self.size:
            if searchnode.data == data:
                return searchnode
            check += 1
            searchnode = searchnode.next
        return False

    def retrieve(self, retrievenode):
        searchnode = self.startnode.next
        check = 0
        while searchnode is not self.endnode and check < self.size:
            if searchnode.data == retrievenode.data and searchnode.next == retrievenode.next and searchnode.prev == retrievenode.prev:
                return searchnode
            check += 1
            searchnode = searchnode.next
        return False


b = Node(6, None, None)
f = Node(11, None, b)
c = Node(9, b, None)
d = Node(12, b, c)
e = Node(11, None, b)
print("c - d - b - e")
a = DoublyLinkedChain()
a.createChain()
print(a.isEmpty())
a.add(b)
print(a.isEmpty())
a.destroyChain()
print(a.isEmpty())
print(a.add(b))
print("startnode:", b.prev)
print("endnode:", b.next)
print(a.add(c))
print(a.add(d))
print(a.add(e))
a.printChain()
print(a.retrieve(c).data)
print("_________________________________________")
print(a.remove(9))
a.printChain()
print(a.remove(f))
print(a.isEmpty())
a.destroyChain()
print("reset")
print(a.addLast(6))
print(a.addLast(7))
print(a.addLast(6))
a.printChain()
print(a.remove(6))
print(a.addLast(6))
print(a.remove(6))

print(a.isEmpty())
