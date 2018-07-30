class StackNode:

    def __init__(self, item):
        self.next = None
        self.item = item


class Stack:

    def __init__(self):
        self.top = None
        self.topItem = None

    def isEmpty(self):
        return self.top is None

    def destroyStack(self):
        while not self.isEmpty():
            self.pop()
        self.topItem = None
        return True

    def push(self, newItem):
        newNode = StackNode(newItem)
        newNode.next = self.top
        self.top = newNode
        return True

    def pop(self):
        if self.isEmpty():
            return False
        else:
            deleteNode = self.top
            self.top = self.top.next
            deleteNode.item = None
            deleteNode.next = None
            return True

    def popDisplay(self):
        if self.isEmpty():
            return False
        else:
            self.getTop()
            self.pop()
            return True

    def getTop(self):
        if self.isEmpty():
            return False, None
        else:
            self.topItem = self.top.item
            return True, self.topItem
