class Stack:

    def __init__(self):
        self.stack = None
        self.stacktop = None

    def createStack(self):
        self.stack = []
        self.stacktop = None

    def destroyStack(self):
        for i in range(len(self.stack)):
            self.stack.pop()
        self.stacktop = None
        self.stack = None

    def isEmpty(self):
        return self.stack == []

    def push(self, newitem):
        self.stack.append(newitem)
        return True

    def pop(self):
        self.stack.pop()
        return True

    def popDisplay(self):
        self.stacktop = self.stack[len(self.stack)-1]
        self.stack.pop()
        return True

    def getTop(self):
        self.stacktop = self.stack[len(self.stack) - 1]
        return True
