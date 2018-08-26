import copy

class Node:
    def __init__(self, searchkey, parent = None):
        self.searchkeys = [searchkey]
        self.left_child = None
        self.middle_child = None
        self.right_child = None
        self.temp_child = None
        self.parent = None
        if parent:
            self.parent = parent

class Tree:
    def init(self):
        self.root = None

    def createTree(self):
        self.root = Node(None)

    def destroyTree(self):
        pass

    def isEmpty(self):
        if self.root is None:
            return False
        elif len(self.root.items) == 0:
            return True
        else:
            return False

    def hasChildren(self, node):
        if node.left_child is None and node.middle_child is None and node.right_child is None:
            return False
        else:
            return True

    def hasAllChildren(self, node):
        if node.left_child is not None and node.middle_child is not None and node.right_child is not None:
            return True
        else:
            return False

    def treeInsert(self, searchkey, root = None):
        if not root:
            root = self.root

        if self.root.searchkeys == [None]:
            self.root.searchkeys= [searchkey]
            return True

        if not self.hasChildren(root):
            root.searchkeys.append(searchkey)
            root.searchkeys.sort()
            if len(root.searchkeys) == 3:
                self.trickleUp(root)
        else:
            if searchkey < root.searchkeys[0]:
                if root.left_child:
                    self.treeInsert(searchkey, root.left_child)
                else:
                    root.searchkeys.append(item)
                    root.searchkeys.sort()
                    if len(root.searchkeys) == 3:
                        self.trickleUp(root)
            if searchkey > root.searchkeys[-1]:
                if root.right_child:
                    self.treeInsert(searchkey, root.right_child)
            if root.searchkeys[0] < searchkey < root.searchkeys[-1]:
                if root.middle_child:
                    self.treeInsert(searchkey, root.middle_child)

    def treeSearch(self, searchkey, root = None):
        if not root:
            root = self.root

        for i in range(len(root.searchkeys)):
            if root.searchkeys[i] == searchkey:
                return searchkey

        if not self.hasChildren(root):
            for i in range(len(root.searchkeys)):
                if root.searchkeys[i] == searchkey:
                    return searchkey
            return False
        else:
            if searchkey < root.searchkeys[0]:
                return self.treeSearch(searchkey, root.left_child)
            if root.searchkeys[0] < searchkey < root.searchkeys[-1]:
                if root.middle_child is not None:
                    self.treeSearch(searchkey, root.middle_child)
                else:
                    return False
            if root.searchkeys[-1] < searchkey:
                return self.treeSearch(searchkey, root.right_child)

    def treeRetrieve(self, searchkey, root = None):
        if not root:
            root = self.root

        node = self.findNode(searchkey)
        for i in range(len(node.searchkeys)):
            if node.searchkeys[i] == searchkey:
                node.searchkeys.pop[i]

    def findNode(self, searchkey, root = None):
        if not root:
            root = self.root

        for i in range(len(root.searchkeys)):
            if root.searchkeys[i] == searchkey:
                return root

        if not self.hasChildren(root):
            for i in range(len(root.searchkeys)):
                if root.searchkeys[i] == searchkey:
                    return root
            return False

        else:
            if searchkey < root.searchkeys[0]:
                return self.findNode(searchkey, root.left_child)
            if root.searchkeys[0] < searchkey < root.searchkeys[-1]:
                if root.middle_child is not None:
                    self.findNode(searchkey, root.middle_child)
                else:
                    return False
            if root.searchkeys[-1] < searchkey:
                return self.findNode(searchkey, root.right_child)

    def findSuccessor(self, node, searchkey, root = None):
        if len(node.searchkeys) == 1:
            node.searchkeys[0] = node.right_child.searchkeys[0]
            node.right_child.searchkeys[0] = searchkey
            if self.hasChildren(node.right_child) is False:
                node.right_child = None

                return True
            else:
                return self.findSuccessor(node.right_child, node.right_child.searchkeys[0])

    def treeDelete(self, searchkey):
        if self.findNode(searchkey) is False:
            return False
        else:
            node = self.findNode(searchkey)
            for i in range(len(node.searchkeys)):
                if node.searchkeys[i] == searchkey:
                    self.findSuccessor(node, searchkey)

    def trickleUp(self, root):
        if not self.hasChildren(root):
            if not root.parent:
                searchkeyList = copy.deepcopy(root.searchkeys)
                root.searchkeys = [searchkeyList[1]]
                root.left_child = Node(searchkeyList[0], root)
                root.right_child = Node(searchkeyList[2], root)
            else:
                searchkeyList = copy.deepcopy(root.searchkeys)
                root.parent.searchkeys.append(searchkeyList[1])
                root.parent.searchkeys.sort()
                root.searchkeys.remove(searchkeyList[1])
                if root.parent.searchkeys[0] < root.searchkeys[0] < root.parent.searchkeys[-1]:
                    if root.parent.middle_child:
                        if len(root.parent.searchkeys) == 3:
                            root.parent.temp_child = Node(searchkeyList[0])
                            root.searchkeys.remove(searchkeyList[0])
                        else:
                            root.parent.middle_child.searchkeys.append(itemList[0])
                            root.parent.middle_child.searchkeys.sort()
                            root.searchkeys.remove(searchkeyList[0])

                    else:
                        root.parent.middle_child = Node(searchkeyList[0], root.parent)
                        root.searchkeys.remove(searchkeyList[0])
                elif root.parent.searchkeys[0] < root.searchkeys[-1] < root.parent.searchkeys[-1]:
                    if root.parent.middle_child:
                        "double trickle"
                        if len(root.parent.searchkeys) == 3:
                            root.parent.temp_child = Node(searchkeyList[2])
                            root.searchkeys.remove(searchkeyList[2])

                        else:
                            root.parent.middle_child.searchkeys.append(searchkeyList[2])
                            root.parent.middle_child.searchkeys.sort()
                            root.searchkeys.remove(searchkeyList[2])
                    else:
                        root.parent.middle_child = Node(searchkeyList[2], root.parent)
                        root.searchkeys.remove(searchkeyList[2])
                if len(root.parent.searchkeys) == 3:
                    self.trickleUp(root.parent)

        if self.hasAllChildren(root):
            if root.parent is None:
                if root.temp_child is not None:
                    oldRoot = copy.deepcopy(self.root)
                    if root.temp_child.searchkeys[0] < root.middle_child.searchkeys[0]:
                        self.root = None
                        self.root = Node(oldRoot.searchkeys[1])
                        self.root.left_child = Node(oldRoot.searchkeys[0])
                        self.root.left_child.parent = self.root
                        self.root.right_child = Node(oldRoot.searchkeys[2])
                        self.root.right_child.parent = self.root
                        self.root.left_child.left_child = oldRoot.left_child
                        self.root.left_child.left_child.parent = self.root.left_child
                        self.root.right_child.right_child = oldRoot.right_child
                        self.root.right_child.right_child.parent = self.root.right_child
                        self.root.left_child.right_child = oldRoot.temp_child
                        self.root.left_child.right_child.parent = self.root.left_child
                        self.root.right_child.left_child = oldRoot.middle_child
                        self.root.right_child.left_child.parent = self.root.right_child
                    else:
                        self.root = None
                        self.root = Node(oldRoot.searchkeys[1])
                        self.root.left_child = Node(oldRoot.searchkeys[0])
                        self.root.left_child.parent = self.root
                        self.root.right_child = Node(oldRoot.searchkeys[2])
                        self.root.right_child.parent = self.root
                        self.root.left_child.left_child = oldRoot.left_child
                        self.root.left_child.left_child.parent = self.root.left_child
                        self.root.right_child.right_child = oldRoot.right_child
                        self.root.right_child.right_child.parent = self.root.right_child
                        self.root.left_child.right_child = oldRoot.middle_child
                        self.root.left_child.right_child.parent = self.root.left_child
                        self.root.right_child.left_child = oldRoot.temp_child
                        self.root.right_child.left_child.parent = self.root.right_child
            else:
                if root.temp_child is not None:

                    if root.temp_child.searchkeys[0] > root.middle_child.searchkeys[0]:
                        oldNode = copy.deepcopy(root)
                        if root.searchkeys[0] > root.parent.searchkeys[-1]:
                            root.parent.right_child = Node(oldNode.searchkeys[1])
                            root = root.parent.right_child
                        else:
                            root.parent.left_child = Node(oldNode.searchkeys[1])
                            root = root.parent.left_child
                        root.left_child = Node(oldNode.searchkeys[0])
                        root.left_child.parent = root
                        root.right_child = Node(oldNode.searchkeys[2])
                        root.right_child.parent = root
                        root.left_child.left_child = oldNode.left_child
                        root.left_child.left_child.parent = root.left_child
                        root.right_child.right_child = oldNode.right_child
                        root.right_child.right_child.parent = root.right_child
                        root.left_child.right_child = oldNode.middle_child
                        root.left_child.right_child.parent = root.left_child
                        root.right_child.left_child = oldNode.temp_child
                        root.right_child.left_child.parent = root.right_child
                    else:
                        oldNode = copy.deepcopy(root)
                        if root.searchkeys[0] > root.parent.searchkeys[-1]:
                            root.parent.right_child = Node(oldNode.searchkeys[1])
                            root = root.parent.right_child
                        else:
                            root.parent.left_child = Node(oldNode.searchkeys[1])
                            root = root.parent.left_child
                        root.left_child = Node(oldNode.searchkeys[0])
                        root.left_child.parent = root
                        root.right_child = Node(oldNode.searchkeys[2])
                        root.right_child.parent = root
                        root.left_child.left_child = oldNode.left_child
                        root.left_child.left_child.parent = root.left_child
                        root.right_child.right_child = oldNode.right_child
                        root.right_child.right_child.parent = root.right_child
                        root.left_child.right_child = oldNode.temp_child
                        root.left_child.right_child.parent = root.left_child
                        root.right_child.left_child = oldNode.middle_child
                        root.right_child.left_child.parent = root.right_child

    def pre_order(self, root = None):
        if not root:
            print("preorder")
            root = self.root
        print(root.searchkeys)
        if root.left_child is not None:
            print("to left")
            self.pre_order(root.left_child)

        if root.middle_child is not None:
            print("to middle")
            self.pre_order(root.middle_child)

        if root.right_child is not None:
            print("to right")
            self.pre_order(root.right_child)

    def in_order(self, root=None):
        if not root:
            print("inorder")
            root = self.root

        if root.left_child is not None:
            self.in_order(root.left_child)

        print(root.searchkeys[0])

        if root.middle_child is not None:
            self.in_order(root.middle_child)

        if len(root.searchkeys) == 2:
            print(root.searchkeys[1])

        if root.right_child is not None:
            self.in_order(root.right_child)
T = Tree()
T.createTree()
T.treeInsert(5)
T.treeInsert(4)
T.treeInsert(2)
T.treeInsert(9)
T.treeInsert(10)
T.treeInsert(1)
T.treeInsert(0)
T.treeInsert(-1)
T.treeInsert(11)
T.treeInsert(12)
T.treeInsert(13)
T.treeInsert(14)
T.treeInsert(-2)
T.treeInsert(-3)
T.pre_order()




