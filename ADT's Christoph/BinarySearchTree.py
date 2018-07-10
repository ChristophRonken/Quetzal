class Node:
    # searchkey = number
    # gegevens = data
    def __init__(self, searchkey, gegevens):
        self.searchkey = searchkey
        self.data = gegevens
        self.lchild = None
        self.rchild = None

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Node):
            return self.data == other.data and self.searchkey == other.searchkey and self.lchild == other.lchild and self.rchild == other.rchild
        return False


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def createSearchTree(self):
        self.root = Node(None, None)
        return

    def insert(self, root, searchkey, gegevens):
        if self.root == Node(None, None):
            self.root = Node(searchkey, gegevens)
            return True

        elif self.isInTree(self.root, searchkey):
            return False

        elif root.searchkey < searchkey:
            if not root.rchild:
                root.rchild = Node(searchkey, gegevens)
                return True

            else:
                return self.insert(root.rchild, searchkey, gegevens)

        elif root.searchkey > searchkey:
            if not root.lchild:
                root.lchild = Node(searchkey, gegevens)
                return True

            else:
                return self.insert(root.lchild, searchkey, gegevens)

        return False

    def isEmpty(self):
        return self.root == Node(None, None)

    def isInTree(self, root, searchkey):
        if root == Node(None, None):
            return False
        if not root:
            return False
        if root.searchkey == searchkey:
            return True
        elif root.searchkey > searchkey:
            return self.isInTree(root.lchild, searchkey)
        elif root.searchkey < searchkey:
            return self.isInTree(root.rchild, searchkey)

    def successor(self, rchild):
        if not rchild:
            return False
        else:
            while rchild.lchild:
                rchild = rchild.lchild
            return rchild

    '''
    def predecessor(self, lchild):
        if not lchild:
            return False
        else:
            while lchild.rchild:
                lchild = lchild.rchild
            return lchild
    '''

    def parent(self, root):
        return

    def findNode(self, root, searchkey):
        if root == Node(None, None):
            return False
        if root.searchkey == searchkey:
            return root
        elif root.searchkey > searchkey:
            return self.findNode(root.lchild, searchkey)
        elif root.searchkey < searchkey:
            return self.findNode(root.rchild, searchkey)

    def deleteNode(self, root, searchkey):
        if not self.isInTree(root, searchkey):
            return False

        else:
            if searchkey > root.searchkey:
                print("groter dan")

                if root.rchild.searchkey != searchkey:
                    self.deleteNode(root.rchild, searchkey)

                else:
                    if not root.rchild.rchild and not root.rchild.lchild:
                        print("geval 1")
                        root.rchild.data = None
                        root.rchild.searchkey = None
                        root.rchild.lchild = None
                        root.rchild.rchild = None
                        root.rchild = None
                        return True

                    if not root.rchild.rchild and root.rchild.lchild:
                        print("geval 2L")
                        replacement = root.rchild.lchild
                        root.rchild.data = None
                        root.rchild.searchkey = None
                        root.rchild.lchild = None
                        root.rchild.rchild = None
                        root.rchild = replacement
                        return True

                    if not root.rchild.lchild and root.rchild.rchild:
                        print("geval 2R")
                        replacement = root.rchild.rchild
                        root.rchild.data = None
                        root.rchild.searchkey = None
                        root.rchild.lchild = None
                        root.rchild.rchild = None
                        root.rchild = replacement
                        return True

                    if root.rchild.lchild and root.rchild.rchild:
                        print("geval 3")
                        replacement = Node(None, None)
                        replacementSearchkey = self.successor(root.rchild.rchild).searchkey
                        replacementData = self.successor(root.rchild.rchild).data
                        self.deleteNode(root.rchild.rchild, self.successor(root.rchild.rchild).searchkey)
                        root.rchild.data = replacementData
                        root.rchild.searchkey = replacementSearchkey
                        print("replacement: ", replacement.searchkey)
                        print("root.rchild.rchild: ", root.rchild.rchild.searchkey)
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


a = BinarySearchTree()
a.createSearchTree()

a.insert(a.root, 5, "5")
a.insert(a.root, 9, "9")
a.insert(a.root, 9, "9")
a.insert(a.root, 6, "6")
a.insert(a.root, 7, "7")
a.insert(a.root, 8, "8")
a.insert(a.root, 12, "12")
a.insert(a.root, 10, "10")
a.insert(a.root, 11, "11")
a.insert(a.root, 13, "13")
a.insert(a.root, 4, "4")
a.insert(a.root, 2, "2")
a.insert(a.root, 3, "3")
a.insert(a.root, 1, "1")

a.deleteNode(a.root, 1)
a.inOrder(a.root)
a.deleteNode(a.root, 2)
a.inOrder(a.root)
a.deleteNode(a.root, 3)
a.inOrder(a.root)
a.deleteNode(a.root, 4)
a.inOrder(a.root)
print("hey")
a.deleteNode(a.root, 5)
a.inOrder(a.root)
a.deleteNode(a.root, 6)
a.inOrder(a.root)
a.deleteNode(a.root, 7)
a.inOrder(a.root)
a.deleteNode(a.root, 8)
a.inOrder(a.root)
a.deleteNode(a.root, 9)
a.inOrder(a.root)
a.deleteNode(a.root, 10)
a.inOrder(a.root)
a.deleteNode(a.root, 11)
a.inOrder(a.root)
a.deleteNode(a.root, 12)
a.inOrder(a.root)
a.deleteNode(a.root, 13)
a.inOrder(a.root)

'''
t(a.isInTree(a.root, 5))
print(a.deleteNode(a.root, 5))
print(a.isInTree(a.root, 5))
print(a.root)
'''