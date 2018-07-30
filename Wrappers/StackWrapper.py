from ADT_Christoph.Stack.Stack import Stack
from OutputGenerators.StackOG import printStack


class StackWrapper:

    def __init__(self):
        self.__ADT = Stack()
        return

    def create(self):
        return

    def isEmpty(self):
        return self.__ADT.isEmpty()

    def insert(self, searchkey, newItem):
        return self.__ADT.push(newItem)

    def delete(self, searchkey):
        return self.__ADT.pop()

    def destroy(self):
        return self.__ADT.destroyStack()

    def retrieve(self, searchkey):
        if self.__ADT.getTop()[0]:
            return self.__ADT.getTop()[1]
        return False

    def print(self):
        return printStack(self.__ADT)
