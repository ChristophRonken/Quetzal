class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue():
    def __init__(self):
        self.size = 0
        self.root = None

    def isEmpty(self):
        return self.size == 0

    def createQueue(self):
        self.root = Node(None, None)

    def destroyQueue(self):
        self.root = Node(None, None)

    def enQueue(self, value):
        if self.size == 0:
            self.root = Node(value)
            self.size += 1
        else:
            searchnode = self.root
            while searchnode.next is not None:
                searchnode = self.root.next
            searchnode.next = Node(value)
            self.size += 1

    def deQueue(self):
        searchnode = self.root
        for i in range(self.size - 1):
            searchnode = searchnode.next
        searchnode.next = None

    def getFront(self):
        print(self.root.value)
        return self.root.value

    def getBack(self):
        searchnode = self.root
        for i in range(self.size - 1):
            searchnode = searchnode.next
        print(searchnode.value)
        return searchnode.value


Remi = Queue()
print(Remi.isEmpty())
Remi.enQueue(7)
Remi.enQueue(8)
Remi.getFront()
Remi.getBack()
print(Remi.isEmpty())