class Node:
    def __init__(self, item, next, searchkey):
        self.item = item
        self.next = next
        self.searchkey = searchkey


class CircularChain:
    def __init__(self):
        self.root = Node(None, None, None)
        self.root.next = self.root
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def createChain(self):
        self.root = Node(None, None, None)
        self.root.next = self.root
        self.size = 0

    def destroyChain(self):
        for i in range(self.size):
            self.delete()
        return True

    def toLastNode(self, node):
        for i in range(self.size - 1):
            node = node.next
        return node

    def addNode(self, searchkey, newItem, root=None):
        if root is None:
            root = self.root
        if root.searchkey is None:
            root.item = newItem
            root.searchkey = searchkey
            self.size += 1
            return True
        else:
            if root.next is self.root:
                root.next = Node(newItem, self.root, searchkey)
                self.size += 1
                return True
            else:
                return self.addNode(searchkey, newItem, root.next)

    def findNode(self, searchkey):
        node = self.root
        for i in range(self.size):
            if node.searchkey == searchkey:
                return node
            else:
                node = node.next
        return False

    def retrieve(self, searchkey=None):
        if searchkey is None:
            return self.root.item
        node = self.root
        for i in range(self.size):
            if node.searchkey == searchkey:
                return node.item
            else:
                node = node.next
        return False

    def delete(self, searchkey=None):
        if searchkey is None:
            node = self.root
            while node.next is not self.root:
                node = node.next
            if node == self.root:
                self.root.item = None
                self.root.searchkey = None
                self.root.next = self.root
                self.size = 0
                return True
            else:
                last_node = self.toLastNode(node)
                last_node.next = node.next
                self.size -= 1
                return True
        else:
            removed_node = self.findNode(searchkey)
            if removed_node:
                last_node = self.toLastNode(removed_node)
                if removed_node == self.root:
                    self.root = removed_node.next
                last_node.next = removed_node.next
                removed_node.next = None
                removed_node.searchkey = None
                removed_node.item = None
                self.size -= 1
                return True
            else:
                return False

    def printChain(self):
        node = self.root
        for i in range(self.size + 1):
            print(node.searchkey)
            node = node.next

    def get_size(self):
        return self.size


a = CircularChain()
a.createChain()
print(a.addNode(0, "filled"))
print(a.addNode(0, "filled"))
print(a.delete(0))
print(a.delete(0))
print(a.delete(0))
