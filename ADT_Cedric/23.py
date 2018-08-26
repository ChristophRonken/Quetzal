import copy

class Node:
    def __init__(self, item, parent = None):
        self.items = [item]
        self.left_child = None
        self.middle_child = None
        self.right_child = None
        self.temp_child = None
        self.parent = None
        if parent:
            self.parent = parent

class Tree:
    def __init__(self):
        self.size = 0
        self.root = None

    def createTree(self, root):
        self.root = root
        self.size = 1

    def destroyTree(self):
        pass

    def isEmpty(self):
        return self.size == 0

    def hasChildren(self, node):
        if node.left_child == None and node.middle_child == None and node.right_child == None:
            return False
        else:
            return True
    def hasAllChildren(self, node):
        if node.left_child is not None and node.middle_child is not None and node.right_child is not None:
            return True
        else:
            return False

    def treeInsert(self, item, root = None):
        print("inserting", item)
        if not root:
            root = self.root

        if not self.hasChildren(root):
            root.items.append(item)
            root.items.sort()
            print(root.items)
            print(self.root.items)
            if len(root.items) == 3:
                self.trickleUp(root)

        else:
            print("has children")
            if item < root.items[0]:
                if root.left_child:
                    self.treeInsert(item, root.left_child)
                else:
                    root.items.append(item)
                    root.items.sort()
                    print("test")
                    print(root.items)
                    print(self.root.items)
                    if len(root.items) == 3:
                        self.trickleUp(root)
            if item > root.items[-1]:
                if root.right_child:
                    self.treeInsert(item, root.right_child)
            if root.items[0] < item < root.items[-1]:
                if root.middle_child:
                    self.treeInsert(item, root.middle_child)

    def treeSearch(self, item, root = None):
        if not root:
            root = self.root

        for i in range(len(root.items)):
            if root.items[i] == item:
                return True

        if not self.hasChildren(root):
            for i in range(len(root.items)):
                if root.items[i] == item:
                    return True
            return False
        else:
            if item < root.items[0]:
                return self.treeSearch(item, root.left_child)
            if root.items[0] < item < root.items[-1]:
                if root.middle_child is not None:
                    self.treeSearch(item, root.middle_child)
                else:
                    return False
            if root.items[-1] < item:
                return self.treeSearch(item, root.right_child)



    def treeDelete(self, item, root = None):
        if self.treeSearch(item) is False:
            return False



    def trickleUp(self, root):
        print('trickle up')
        if not self.hasChildren(root):
            "if the trickleUp happens in the root"
            if not root.parent:
                itemList = copy.deepcopy(root.items)
                root.items = [itemList[1]]
                print(root.items)
                root.left_child = Node(itemList[0], root)
                print(root.left_child.items)
                root.right_child = Node(itemList[2], root)
                print(root.right_child.items)
            else:
                itemList = copy.deepcopy(root.items)
                root.parent.items.append(itemList[1])
                root.parent.items.sort()
                root.items.remove(itemList[1])
                if root.parent.items[0] < root.items[0] < root.parent.items[-1]:
                    if root.parent.middle_child:
                        if len(root.parent.items) == 3:
                            root.parent.temp_child = Node(itemList[0])
                            root.items.remove(itemList[0])
                        else:
                            root.parent.middle_child.items.append(itemList[0])
                            root.parent.middle_child.items.sort()
                            root.items.remove(itemList[0])

                    else:
                        root.parent.middle_child = Node(itemList[0], root.parent)
                        root.items.remove(itemList[0])
                elif root.parent.items[0] < root.items[-1] < root.parent.items[-1]:
                    if root.parent.middle_child:
                        "double trickle"
                        if len(root.parent.items) == 3:
                            print("root items")
                            print(root.items)
                            root.parent.temp_child = Node(itemList[2])
                            root.items.remove(itemList[2])

                        else:
                            root.parent.middle_child.items.append(itemList[2])
                            root.parent.middle_child.items.sort()
                            root.items.remove(itemList[2])
                    else:
                        root.parent.middle_child = Node(itemList[2], root.parent)
                        root.items.remove(itemList[2])
                if len(root.parent.items) == 3:
                    print('double trickle')
                    self.trickleUp(root.parent)

        if self.hasAllChildren(root):
            if root.parent is None:
                if root.temp_child is not None:
                    print(root.temp_child.items, root.middle_child.items)
                    if root.temp_child.items[0] < root.middle_child.items[0]:
                        oldRoot = copy.deepcopy(self.root)
                        self.root = None
                        self.root = Node(oldRoot.items[1])
                        self.root.left_child = Node(oldRoot.items[0])
                        self.root.left_child.parent = self.root
                        self.root.right_child = Node(oldRoot.items[2])
                        self.root.right_child.parent = self.root
                        self.root.left_child.left_child = oldRoot.left_child
                        self.root.left_child.left_child.parent = self.root.left_child
                        self.root.left_child.right_child = oldRoot.temp_child
                        self.root.left_child.right_child.parent = self.root.left_child
                        self.root.right_child.left_child = oldRoot.middle_child
                        self.root.right_child.left_child.parent = self.root.right_child
                        self.root.right_child.right_child = oldRoot.right_child
                        self.root.right_child.right_child.parent = self.root.right_child
                    else:
                        oldRoot = copy.deepcopy(self.root)
                        self.root = None
                        self.root = Node(oldRoot.items[1])
                        self.root.left_child = Node(oldRoot.items[0])
                        self.root.left_child.parent = self.root
                        self.root.right_child = Node(oldRoot.items[2])
                        self.root.right_child.parent = self.root
                        self.root.left_child.left_child = oldRoot.left_child
                        self.root.left_child.left_child.parent = self.root.left_child
                        self.root.left_child.right_child = oldRoot.middle_child
                        self.root.left_child.right_child.parent = self.root.left_child
                        self.root.right_child.left_child = oldRoot.temp_child
                        self.root.right_child.left_child.parent = self.root.right_child
                        self.root.right_child.right_child = oldRoot.right_child
                        self.root.right_child.right_child.parent = self.root.right_child
            else:
                if root.temp_child is not None:
                    if root.temp_child.items[0] > root.middle_child.items[0]:
                        oldNode = copy.deepcopy(root)
                        if root.items[0] > root.parent.items[-1]:
                            root.parent.right_child = Node(oldNode.items[1])
                            root = root.parent.right_child
                        else:
                            root.parent.left_child = Node(oldNode.items[1])
                            root = root.parent.left_child

                        root.left_child = Node(oldNode.items[0])
                        root.left_child.parent = root
                        root.right_child = Node(oldNode.items[2])
                        root.right_child.parent = root
                        root.left_child.left_child = oldNode.left_child
                        root.left_child.left_child.parent = root.left_child
                        root.left_child.right_child = oldNode.middle_child
                        root.left_child.right_child.parent = root.left_child
                        root.right_child.left_child = oldNode.temp_child
                        root.right_child.left_child.parent = root.right_child
                        root.right_child.right_child = oldNode.right_child
                        root.right_child.right_child.parent = root.right_child
                    else:
                        oldNode = copy.deepcopy(root)
                        if root.items[0] > root.parent.items[-1]:
                            root.parent.right_child = Node(oldNode.items[1])
                            root = root.parent.right_child
                        else:
                            root.parent.left_child = Node(oldNode.items[1])
                            root = root.parent.left_child

                        root.left_child = Node(oldNode.items[0])
                        root.left_child.parent = root
                        root.right_child = Node(oldNode.items[2])
                        root.right_child.parent = root
                        root.left_child.left_child = oldNode.left_child
                        root.left_child.left_child.parent = root.left_child
                        root.left_child.right_child = oldNode.temp_child
                        root.left_child.right_child.parent = root.left_child
                        root.right_child.left_child = oldNode.middle_child
                        root.right_child.left_child.parent = root.right_child
                        root.right_child.right_child = oldNode.right_child
                        root.right_child.right_child.parent = root.right_child

    def pre_order(self, root = None):
        if not root:
            print("preorder")
            root = self.root
        print(root.items)
        if root.left_child is not None:
            print("to left")
            self.pre_order(root.left_child)

        if root.middle_child is not None:
            print("to middle")
            self.pre_order(root.middle_child)

        if root.right_child is not None:
            print("to right")
            self.pre_order(root.right_child)



T = Tree()
T.createTree(Node(6))
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



