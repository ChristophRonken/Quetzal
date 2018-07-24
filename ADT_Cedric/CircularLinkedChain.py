class Node:
    def __init__(self, item, next, searchkey):
        self.item = item
        self.next = next
        self.searchkey = searchkey

class circular_chain:
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

    def add_node(self, item, searchkey, root = None):
        if not root:
            root = self.root
        if root.next is self.root:
            root.next = Node(item, self.root, searchkey)
            self.size += 1

        else:
            return self.add_node(item, searchkey, root.next)

    def find_node(self, searchkey):
        node = self.root
        for i in range(self.size):
            if node.searchkey == searchkey:
                return node
            else:
                node = node.next
        return False

    def delete(self, searchkey):
        removed_node = self.find_node(searchkey)
        if removed_node != False:
            removed_node_next = self.find_node(searchkey).next
            last_node = self.to_last_node(removed_node)
            last_node.next = removed_node_next
        else:
            return False


    def print_chain(self):
        node = self.root
        for i in range(self.size):
            print(node.searchkey)
            node = node.next


    def get_size(self):
        return self.size


C = circular_chain()
C.create_chain(6, 6)
C.add_node(7, 7)
C.add_node(9, 9)
C.delete(9)
C.print_chain()