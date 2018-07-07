class Queue():
    def __init__(self):
        pass

    def isEmpty(self):
        return len(self.items) == 0

    def createQueue(self):
        self.items = []

    def destroyQueue(self):
        self.items = []

    def enQueue(self, item):
        self.items.append(item)

    def deQueue(self):
        self.items.pop(0)

    def getFront(self):
        print(self.items[0])
        return self.items[0]

    def getBack(self):
        print(self.items[len(self.items) - 1])
        return self.items[len(self.items) - 1]






Remi = Queue()
Remi.createQueue()
print(Remi.isEmpty())
Remi.enQueue(7)
Remi.enQueue("Blokje kaas")
Remi.enQueue("hesp")
Remi.getFront()
Remi.getBack()


