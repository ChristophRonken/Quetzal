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

    def isLeaf(self):
        if self.searchkey and not self.lchild and not self.rchild:
            return True
        else:
            return False

    def leftChild(self):
        if self.searchkey and self.lchild and not self.rchild:
            return True
        else:
            return False

    def rightChild(self):
        if self.searchkey and not self.lchild and self.rchild:
            return True
        else:
            return False

    def twoChild(self):
        if self.searchkey and self.lchild and self.rchild:
            return True
        else:
            return False


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __successor(self, rchild):
        if not rchild:
            return False
        else:
            while rchild.lchild:
                rchild = rchild.lchild
            return rchild

    def createSearchTree(self):
        if not self.exists():
            self.root = Node(None, None)
            return True
        return False

    def insert(self, searchkey, newItem, root=None):
        if not root:
            root = self.root
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
                return self.insert(searchkey, newItem, root.rchild)

        elif root.searchkey > searchkey:
            if not root.lchild:
                root.lchild = Node(searchkey, newItem)
                return True

            else:
                return self.insert(searchkey, newItem, root.lchild)

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

    def findNode(self, searchkey, root=None):
        if not self.exists():
            return False
        if self.isEmpty():
            return False
        if not root:
            root = self.root
        if root.searchkey == searchkey:
            return root
        elif root.searchkey > searchkey:
            if not root.lchild:
                return False
            else:
                return self.findNode(searchkey, root.lchild)
        elif root.searchkey < searchkey:
            if not root.rchild:
                return False
            else:
                return self.findNode(searchkey, root.rchild)

    def deleteNode(self, searchkey, root=None):
        if not root:
            root = self.root

        if not self.findNode(searchkey):
            return False

        else:
            if searchkey > root.searchkey:
                if root.rchild.searchkey != searchkey:
                    self.deleteNode(searchkey, root.rchild)

                else:
                    # enkel element in rchild
                    if not root.rchild.rchild and not root.rchild.lchild:
                        root.rchild.item = None
                        root.rchild.searchkey = None
                        root.rchild.lchild = None
                        root.rchild.rchild = None
                        root.rchild = None
                        return True

                    # rchild heeft lchild
                    elif not root.rchild.rchild and root.rchild.lchild:
                        replacement = root.rchild.lchild
                        root.rchild.item = None
                        root.rchild.searchkey = None
                        root.rchild.lchild = None
                        root.rchild.rchild = None
                        root.rchild = replacement
                        return True

                    # rchild heeft rchild
                    elif not root.rchild.lchild and root.rchild.rchild:
                        replacement = root.rchild.rchild
                        root.rchild.item = None
                        root.rchild.searchkey = None
                        root.rchild.lchild = None
                        root.rchild.rchild = None
                        root.rchild = replacement
                        return True

                    # rchild heeft 2 kinderen
                    if root.rchild.lchild and root.rchild.rchild:
                        successorNode = self.__successor(root.rchild.rchild)
                        if successorNode == root.rchild.rchild:
                            successorNode.lchild = root.rchild.lchild
                            root.rchild = successorNode
                        else:
                            root.rchild.item = successorNode.item
                            root.rchild.searchkey = successorNode.searchkey
                            self.deleteNode(successorNode.searchkey, root.rchild.rchild)
                        return True

            elif searchkey < root.searchkey:
                if root.lchild.searchkey != searchkey:
                    self.deleteNode(searchkey, root.lchild)

                else:
                    # enkel element in lchild
                    if not root.lchild.rchild and not root.lchild.lchild:
                        root.lchild.item = None
                        root.lchild.searchkey = None
                        root.lchild.lchild = None
                        root.lchild.rchild = None
                        root.lchild = None
                        return True

                    # lchild heeft lchild
                    if not root.lchild.rchild and root.lchild.lchild:
                        replacement = root.lchild.lchild
                        root.lchild.item = None
                        root.lchild.searchkey = None
                        root.lchild.lchild = None
                        root.lchild.rchild = None
                        root.lchild = replacement
                        return True

                    # lchild heeft rchild
                    if not root.lchild.lchild and root.lchild.rchild:
                        replacement = root.lchild.rchild
                        root.lchild.item = None
                        root.lchild.searchkey = None
                        root.lchild.lchild = None
                        root.lchild.rchild = None
                        root.lchild = replacement
                        return True

                    # lchild heeft 2 kinderen
                    if root.lchild.lchild and root.lchild.rchild:
                        successorNode = self.__successor(root.lchild.rchild)
                        if successorNode == root.lchild.rchild:
                            successorNode.lchild = root.lchild.lchild
                            root.lchild = successorNode
                        else:
                            root.lchild.item = successorNode.item
                            root.lchild.searchkey = successorNode.searchkey
                            self.deleteNode(successorNode.searchkey, root.lchild.rchild)
                        return True

            else:
                # enkel element in root
                if not root.rchild and not root.lchild:
                    if self.root == root:
                        root.item = None
                        root.searchkey = None
                        root.lchild = None
                        root.rchild = None
                        return True

                # root heeft lchild
                if not root.rchild and root.lchild:
                    if self.root == root:
                        self.root = root.lchild
                        return True

                # root heeft rchild
                if not root.lchild and root.rchild:
                    if root == self.root:
                        self.root = root.rchild
                        return True

                # root heeft 2 kinderen
                if root.lchild and root.rchild:
                    if root == self.root:
                        successorNode = self.__successor(root.rchild)
                        if successorNode == root.rchild:
                            successorNode.lchild = self.root.lchild
                            self.root = successorNode
                        else:
                            self.root.item = successorNode.item
                            self.root.searchkey = successorNode.searchkey
                            self.deleteNode(successorNode.searchkey, self.root.rchild)
                        return True
        return False

    def destroySearchTree(self):
        while self.root != Node(None, None):
            if self.root.rchild:
                self.deleteNode(self.root.rchild.searchkey)
            if self.root.lchild:
                self.deleteNode(self.root.lchild.searchkey)
            if not self.root.lchild and not self.root.rchild:
                self.root.item = None
                self.root.searchkey = None
        self.root = None
        return

    def preOrder(self, root=None):
        if not root:
            root = self.root
        if self.root != Node(None, None):
            print(root.item)
            if root.lchild:
                self.preOrder(root.lchild)
            if root.rchild:
                self.preOrder(root.rchild)

    def inOrder(self, root=None):
        if not root:
            root = self.root
        if self.root != Node(None, None):
            if root.lchild:
                self.inOrder(root.lchild)
            print(root.item)
            if root.rchild:
                self.inOrder(root.rchild)

    def postOrder(self, root=None):
        if not root:
            root = self.root
        if self.root != Node(None, None):
            if root.lchild:
                self.postOrder(root.lchild)
            if root.rchild:
                self.postOrder(root.rchild)
            print(root.item)


for i in range(0, 19):
    a = BinarySearchTree()
    a.createSearchTree()
    a.insert(8, "8")

    a.insert(4, "4")
    a.insert(6, "6")
    a.insert(5, "5")
    a.insert(7, "7")
    a.insert(2, "2")
    a.insert(1, "1")
    a.insert(3, "3")

    a.insert(12, "12")
    a.insert(10, "10")
    a.insert(9, "9")
    a.insert(11, "11")
    a.insert(14, "14")
    a.insert(13, "13")
    a.insert(15, "15")

    a.deleteNode(i)
    a.inOrder()
    print()

