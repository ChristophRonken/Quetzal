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

    def destroy_search_tree(self):
        self.root = None
        self.size = 0

    def search_tree_insert(self, root, node):
        if root.item < node.item:
            if root.right_child is None:
                root.right_child = node
                self.size += 1
                return True
            else:
                return self.search_tree_insert(root.right_child, node)

        if root.item > node.item:
            if root.left_child is None:
                root.left_child = node
                self.size += 1
                return True
            else:
                return self.search_tree_insert(root.left_child, node)
        else:
            return False

    def search_tree_delete(self, key):
        pass

    def search_tree_retrieve(self, root, key):
        if root.item == key:
            return True
        else:
            if root.item < key:
                if root.right_child is not None:
                    print("right")
                    return self.search_tree_retrieve(root.right_child, key)

            if root.item > key:
                if root.left_child is not None:
                    print("left")
                    return self.search_tree_retrieve(root.left_child, key)
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

N = Node(4)
BST = BinarySearchTree()
BST.create_search_tree(N)
print(BST.search_tree_insert(N, Node(6)))
print(BST.search_tree_insert(N, Node(2)))
print(BST.search_tree_insert(N, Node(1)))
print(BST.search_tree_insert(N, Node(3)))
print(BST.search_tree_insert(N, Node(5)))
print(BST.search_tree_insert(N, Node(7)))
print(BST.search_tree_retrieve(N, 7))
BST.post_order(N)














