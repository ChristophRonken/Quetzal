class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class Queue:
    def __init__(self):
        self.size = 0
        self.root = None

    def isEmpty(self):
        return self.size == 0

    def createQueue(self):
        self.root = Node(None)

    def destroyQueue(self):
        for i in range(self.size - 1):
            self.deQueue()
        self.root.item = None
        self.root.next = None
        return True

    def enQueue(self, newItem):
        if self.size == 0:
            self.root = Node(newItem)
            self.size += 1
        else:
            searchnode = self.root
            while searchnode.next is not None:
                searchnode = searchnode.next
            searchnode.next = Node(newItem)
            self.size += 1
        return True

    def deQueue(self):
        new_root = self.root.next
        self.root = new_root
        self.size -= 1
        return True

    def getFront(self):
        return self.root.item

    def getBack(self):
        searchnode = self.root
        for i in range(self.size - 1):
            searchnode = searchnode.next
        return searchnode.item

