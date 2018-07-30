from ADT_Cedric.Queue import Queue
from OutputGenerator import printQueue


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

    def destroy(self):
        return self.__ADT.destroyQueue()

    def retrieve(self, searchkey):
        return self.__ADT.getFront()

    def print(self):
        return printQueue(self.__ADT)