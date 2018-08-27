class Node:
    def __init__(self, item):
        self.item = item
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self):
        self.size = 0
        self.root = None

    def create_search_tree(self, root):
        self.root = root
        self.size = 1
        return True

    def destroy_search_tree(self):
        self.root = None
        self.size = 0

    def search_tree_insert(self, node, root = None):
        if not root:
            root = self.root

        if root.item < node.item:
            if root.right_child is None:
                root.right_child = node
                self.size += 1
                return True
            else:
                return self.search_tree_insert(node, root.right_child)

        if root.item > node.item:
            if root.left_child is None:
                root.left_child = node
                self.size += 1
                return True
            else:
                return self.search_tree_insert(node, root.left_child)
        else:
            return False

    def search_tree_delete(self, key):
        pass

    def search_tree_retrieve(self, key, root = None):
        if not root:
            root = self.root

        if root.item == key:
            return True
        else:
            if root.item < key:
                if root.right_child is not None:
                    return self.search_tree_retrieve(key, root.right_child)

            if root.item > key:
                if root.left_child is not None:
                    return self.search_tree_retrieve(key, root.left_child)
        return False

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def get_root(self):
        return self.root.item

    def pre_order(self, root):
        print(root.item)
        if root.left_child is not None:
            self.pre_order(root.left_child)
        if root.right_child is not None:
            self.pre_order(root.right_child)

    def in_order(self, root):
        if root.left_child is not None:
            self.in_order(root.left_child)
        print(root.item)
        if root.right_child is not None:
            self.in_order(root.right_child)

    def post_order(self, root):
        if root.left_child is not None:
            self.post_order(root.left_child)
        if root.right_child is not None:
            self.post_order(root.right_child)
        print(root.item)















