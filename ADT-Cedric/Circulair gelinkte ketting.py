class Node():
    def __init__(self, item, next):
        self.item = item
        self.next = next

class circular_chain():
    def __init__(self):
        self.root = Node(None, None)
        self.root.next = self.root
        self.size = 0

    def create_chain(self, item):
        self.root.item = item
        self.size = 1

    def add_node(self, root, item):
        if root.next is self.root:
            root.next = Node(item, self.root)
            self.size += 1

        else:
            return self.add_node(root.next, item)

    def print_chain(self, root):
        print(root.item)
        if root.next is not self.root:
            return self.print_chain(root.next)
        else:
            print(root.next.item)

    def get_size(self):
        return self.size


C = circular_chain()
C.create_chain(6)
C.add_node(C.root, 7)
C.add_node(C.root, 9)
C.print_chain(C.root)















