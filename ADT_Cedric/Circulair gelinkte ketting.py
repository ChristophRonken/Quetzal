class Node():
    def __init__(self, item, next, searchkey):
        self.item = item
        self.next = next
        self.searchkey = searchkey

class circular_chain():
    def __init__(self):
        self.root = Node(None, None, None)
        self.root.next = self.root
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def create_chain(self, item, searchkey):
        self.root.item = item
        self.root.searchkey = searchkey
        self.size = 1

    def destroy_chain(self):
        self.root.next = None

    def to_last_node(self, node):
        for i in range(self.size - 1):
            node = node.next
        return node

    def add_node(self, root, item, searchkey):
        if root.next is self.root:
            root.next = Node(item, self.root, searchkey)
            self.size += 1

        else:
            return self.add_node(root.next, item, searchkey)

    def find_node(self, root, searchkey):

        for i in range(self.size):
            if root.searchkey == searchkey:
                return root
            else:
                root = root.next
        return False

    def delete(self, root, searchkey):
        removed_node = self.find_node(root, searchkey)
        if removed_node != False:
            removed_node_next = self.find_node(root, searchkey).next
            last_node = self.to_last_node(removed_node)
            last_node.next = removed_node_next
        else:
            return False


    def print_chain(self, root):
        print(root.searchkey)
        if root.next is not self.root:
            return self.print_chain(root.next)
        else:
            print(root.next.searchkey)

    def get_size(self):
        return self.size


C = circular_chain()
C.create_chain(6, 6)
C.add_node(C.root, 7, 7)
C.add_node(C.root, 9, 9)
C.delete(C.root, 9)
C.print_chain(C.root)















