class StackNode:

    def __init__(self, item):
        self.next = None
        self.item = item


class Stack:

    def __init__(self):
        self.top = None
        self.topData = None
        return

    def isEmpty(self):
        return self.top is None

    def destroyStack(self):
        while not self.isEmpty():
            self.pop()
        self.topData = None
        return

    def push(self, newItem):
        newNode = StackNode(newItem)
        newNode.next = self.top
        self.top = newNode
        return

    def pop(self):
        if self.isEmpty():
            return False
        else:
            deleteNode = self.top
            self.top = self.top.next
            deleteNode.data = None
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
            return False
        else:
            self.topData = self.top.data
            return True
