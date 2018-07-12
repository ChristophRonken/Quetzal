class Node:
    def __init__(self, searchkey, item):
        self.searchkey = searchkey
        self.item = item
        self.lchild = None
        self.rchild = None

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Node):
            return self.item is other.item and self.searchkey is other.searchkey and self.lchild is other.lchild and self.rchild is other.rchild
        return False


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def createSearchTree(self):
        if not self.exists():
            self.root = Node(None, None)
            return True
        return False

    def insert(self, root, searchkey, newItem):
        if not self.exists():
            return False

        elif self.isEmpty():
            self.root = Node(searchkey, newItem)
            return True

        elif root.searchkey == searchkey:
            return False

        elif root.searchkey < searchkey:
            if not root.rchild:
                root.rchild = Node(searchkey, newItem)
                return True

            else:
                return self.insert(root.rchild, searchkey, newItem)

        elif root.searchkey > searchkey:
            if not root.lchild:
                root.lchild = Node(searchkey, newItem)
                return True

            else:
                return self.insert(root.lchild, searchkey, newItem)

        return False

    def exists(self):
        if not self.root:
            return False
        else:
            return True

    def isEmpty(self):
        if self.exists():
            return self.root == Node(None, None)
        return False

    def __successor(self, rchild):
        if not rchild:
            return False
        else:
            while rchild.lchild:
                rchild = rchild.lchild
            return rchild

    def __parent(self, searchkey):
        if not self.exists():
            return False
        elif self.isEmpty():
            return False
        elif self.root.searchkey == searchkey:
            return False
        elif not self.findNode(self.root, searchkey):
            return False
        parentNode = self.root
        return False

    def findNode(self, root, searchkey):
        if not self.exists():
            return False
        if self.isEmpty():
            return False
        if root.searchkey == searchkey:
            return root
        elif root.searchkey > searchkey:
            return self.findNode(root.lchild, searchkey)
        elif root.searchkey < searchkey:
            return self.findNode(root.rchild, searchkey)

    def deleteNode(self, root, searchkey):
        if not self.findNode(root, searchkey):
            return False

        else:
            if searchkey > root.searchkey:

                if root.rchild.searchkey != searchkey:
                    self.deleteNode(root.rchild, searchkey)

                else:
                    if not root.rchild.rchild and not root.rchild.lchild:
                        root.rchild.data = None
                        root.rchild.searchkey = None
                        root.rchild.lchild = None
                        root.rchild.rchild = None
                        root.rchild = None
                        return True

                    elif not root.rchild.rchild and root.rchild.lchild:
                        replacement = root.rchild.lchild
                        root.rchild.data = None
                        root.rchild.searchkey = None
                        root.rchild.lchild = None
                        root.rchild.rchild = None
                        root.rchild = replacement
                        return True

                    elif not root.rchild.lchild and root.rchild.rchild:
                        replacement = root.rchild.rchild
                        root.rchild.data = None
                        root.rchild.searchkey = None
                        root.rchild.lchild = None
                        root.rchild.rchild = None
                        root.rchild = replacement
                        return True

                    else:
                        replacement = Node(None, None)
                        replacementSearchkey = self.successor(root.rchild.rchild).searchkey
                        replacementData = self.successor(root.rchild.rchild).data
                        self.deleteNode(root.rchild.rchild, self.successor(root.rchild.rchild).searchkey)
                        root.rchild.data = replacementData
                        root.rchild.searchkey = replacementSearchkey
                        if root.rchild.rchild != Node(None, None):
                            root.rchild.rchild = root.rchild.rchild
                        else:
                            root.rchild.rchild = None
                        return True

            elif searchkey < root.searchkey:
                print("kleiner dan")
                if root.lchild.searchkey != searchkey:
                    self.deleteNode(root.lchild, searchkey)

                else:
                    if not root.lchild.rchild and not root.lchild.lchild:
                        print("geval 1")
                        root.lchild.data = None
                        root.lchild.searchkey = None
                        root.lchild.lchild = None
                        root.lchild.rchild = None
                        root.lchild = None
                        return True

                    if not root.lchild.rchild and root.lchild.lchild:
                        print("geval 2L")
                        replacement = root.lchild.lchild
                        root.lchild.data = None
                        root.lchild.searchkey = None
                        root.lchild.lchild = None
                        root.lchild.rchild = None
                        root.lchild = replacement
                        return True

                    if not root.lchild.lchild and root.lchild.rchild:
                        print("geval 2R")
                        replacement = root.lchild.rchild
                        root.lchild.data = None
                        root.lchild.searchkey = None
                        root.lchild.lchild = None
                        root.lchild.rchild = None
                        root.lchild = replacement
                        return True

                    if root.lchild.lchild and root.lchild.rchild:
                        print("geval 3")
                        replacement = Node(None, None)
                        replacementSearchkey = self.successor(root.lchild.rchild).searchkey
                        replacementData = self.successor(root.lchild.rchild).data
                        self.deleteNode(root.lchild.rchild, self.successor(root.lchild.rchild).searchkey)
                        root.lchild.data = replacementData
                        root.lchild.searchkey = replacementSearchkey
                        print("replacement: ", replacement.searchkey)
                        print("root.rchild.rchild: ", root.lchild.rchild.searchkey)
                        if root.lchild.rchild != Node(None, None):
                            root.lchild.rchild = root.lchild.rchild
                        else:
                            root.lchild.rchild = None
                        return True

            else:
                print("hey")
                if not root.rchild and not root.lchild:
                    root.data = None
                    root.searchkey = None
                    root.lchild = None
                    root.rchild = None
                    root = None
                    return True

                if not root.rchild and root.lchild:
                    if root == self.root:
                        self.root = root.rchild
                    return True

                if not root.lchild and root.rchild:
                    if root == self.root:
                        self.root = root.rchild
                    return True

                if root.lchild and root.rchild:
                    print("geval 3")
                    replacement = Node(None, None)
                    replacementSearchkey = self.successor(root.rchild).searchkey
                    replacementData = self.successor(root.rchild).data
                    self.deleteNode(root.rchild, self.successor(root.rchild).searchkey)
                    root.data = replacementData
                    root.searchkey = replacementSearchkey
                    print("replacement: ", replacement.searchkey)
                    print("root.rchild.rchild: ", root.rchild.searchkey)
                    if root.rchild != Node(None, None):
                        root.rchild = root.rchild
                    else:
                        root.rchild = None
                    return True

    def destroySearchTree(self):
        while self.root != Node(None, None):
            if self.root.rchild:
                self.deleteNode(self.root, self.root.rchild.searchkey)
            if self.root.lchild:
                self.deleteNode(self.root, self.root.lchild.searchkey)
            if not self.root.lchild and not self.root.rchild:
                self.root.data = None
                self.root.searchkey = None
        self.root = None
        return

    def preOrder(self, root):
        if self.root != Node(None, None):
            print(root.data)
            if root.lchild:
                self.preOrder(root.lchild)
            if root.rchild:
                self.preOrder(root.rchild)

    def inOrder(self, root):
        if self.root != Node(None, None):
            if root.lchild:
                self.inOrder(root.lchild)
            print(root.data)
            if root.rchild:
                self.inOrder(root.rchild)

    def postOrder(self, root):
        if self.root != Node(None, None):
            if root.lchild:
                self.postOrder(root.lchild)
            if root.rchild:
                self.postOrder(root.rchild)
            print(root.data)
