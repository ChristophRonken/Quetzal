import copy

class Node:
    def __init__(self, searchkey, item, parent = None):
        self.searchkeys = [(searchkey, item)]
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
        self.root = Node(None, None)
        return True

    def destroyTree(self):
        pass

    def isEmpty(self):
        if self.root .searchkeys == [(None, None)]:
            return True
        elif len(self.root.searchkeys) == 0:
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

    def sort(self, node):
        if len(node.searchkeys) == 2:
            if node.searchkeys[0][0] > node.searchkeys[1][0]:
                temp = node.searchkeys[1]
                node.searchkeys.pop(-1)
                node.searchkeys.insert(0, temp)
        if len(node.searchkeys) == 3:
            if node.searchkeys[1][0] > node.searchkeys[2][0]:
                temp = node.searchkeys[2]
                node.searchkeys.pop(-1)
                node.searchkeys.insert(1, temp)
            if node.searchkeys[0][0] > node.searchkeys[1][0]:
                temp = node.searchkeys[1]
                node.searchkeys.pop(1)
                node.searchkeys.insert(0, temp)
            if node.searchkeys[1][0] > node.searchkeys[2][0]:
                temp = node.searchkeys[2]
                node.searchkeys.pop(-1)
                node.searchkeys.insert(1, temp)
        return node

    def treeInsert(self, searchkey, item, root = None):
        if not root:
            root = self.root

        if self.treeRetrieve(searchkey)[0] is not False:
            return False

        if self.root.searchkeys == [(None, None)]:
            self.root.searchkeys = [(searchkey, item)]
            return True

        if not self.hasChildren(root):
            root.searchkeys.append((searchkey, item))
            root = self.sort(root)
            if len(root.searchkeys) == 3:
                self.__trickleUp(root)
            return True
        else:
            if searchkey < root.searchkeys[0][0]:
                if root.left_child:
                    return self.treeInsert(searchkey, item, root.left_child)
                else:
                    root.searchkeys.append((searchkey, item))
                    root = self.sort(root)
                    if len(root.searchkeys) == 3:
                        self.__trickleUp(root)
                    return True
            if searchkey > root.searchkeys[-1][0]:
                if root.right_child:
                    return self.treeInsert(searchkey, item, root.right_child)
            if root.searchkeys[0][0] < searchkey < root.searchkeys[-1][0]:
                if root.middle_child:
                    return self.treeInsert(searchkey, item, root.middle_child)
        return False

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
            if root.searchkeys[0][0] < searchkey < root.searchkeys[-1][0]:
                if root.middle_child is not None:
                    self.treeSearch(searchkey, root.middle_child)
                else:
                    return False
            if root.searchkeys[-1][0] < searchkey:
                return self.treeSearch(searchkey, root.right_child)
        return False

    def treeRetrieve(self, searchkey, root = None):
        if not root:
            root = self.root

        node = self.findNode(searchkey)
        if node[0] is not False:
            for i in range(len(node[1].searchkeys)):
                if node[1].searchkeys[i][0] == searchkey:
                    return (True, node[1].searchkeys[i][1])
        return (False, None)

    def findNode(self, searchkey, root = None):
        if not root:
            root = self.root

        for i in range(len(root.searchkeys)):
            if root.searchkeys[i][0] == searchkey:
                return (True, root)

        if not self.hasChildren(root):
            for i in range(len(root.searchkeys)):
                if root.searchkeys[i][0] == searchkey:
                    return (True, root)
            return (False, None)

        else:
            if searchkey < root.searchkeys[0][0]:
                return self.findNode(searchkey, root.left_child)
            if root.searchkeys[0][0] < searchkey < root.searchkeys[-1][0]:
                if root.middle_child is not None:
                    self.findNode(searchkey, root.middle_child)
                else:
                    return (False, None)
            if root.searchkeys[-1][0] < searchkey:
                return self.findNode(searchkey, root.right_child)

    def __findSuccessor(self, node, searchkey, root = None):
        if len(node.searchkeys) == 1:
            node.searchkeys[0] = node.right_child.searchkeys[0]
            node.right_child.searchkeys[0][0] = searchkey
            if self.hasChildren(node.right_child) is False:
                node.right_child = None
                return True
            else:
                return self.__findSuccessor(node.right_child, node.right_child.searchkeys[0][0])

    def treeDelete(self, searchkey):
        if self.findNode(searchkey) is False:
            return False
        else:
            node = self.findNode(searchkey)[1]
            for i in range(len(node.searchkeys)):
                if node.searchkeys[i] == searchkey:
                    self.__findSuccessor(node, searchkey)

    def __trickleUp(self, root):
        if not self.hasChildren(root):
            if not root.parent:
                searchkeyList = copy.deepcopy(root.searchkeys)
                root.searchkeys = [(searchkeyList[1][0], searchkeyList[1][1])]
                root.left_child = Node(searchkeyList[0][0], searchkeyList[0][1], root)
                root.right_child = Node(searchkeyList[2][0], searchkeyList[2][1], root)
            else:
                searchkeyList = copy.deepcopy(root.searchkeys)
                root.parent.searchkeys.append(searchkeyList[1])
                root.parent = self.sort(root.parent)
                root.searchkeys.remove(searchkeyList[1])
                if root.parent.searchkeys[0][0] < root.searchkeys[0][0] < root.parent.searchkeys[-1][0]:
                    if root.parent.middle_child:
                        if len(root.parent.searchkeys) == 3:
                            root.parent.temp_child = Node(searchkeyList[0][0], searchkeyList[0][1])
                            root.searchkeys.remove(searchkeyList[0])
                        else:
                            root.parent.middle_child.searchkeys.append(searchkeyList[0])
                            root.parent.middle_child.searchkeys.sort()
                            root.searchkeys.remove(searchkeyList[0])

                    else:
                        root.parent.middle_child = Node(searchkeyList[0][0], searchkeyList[0][1], root.parent)
                        root.searchkeys.remove(searchkeyList[0])
                elif root.parent.searchkeys[0][0] < root.searchkeys[-1][0] < root.parent.searchkeys[-1][0]:
                    if root.parent.middle_child:
                        "double trickle"
                        if len(root.parent.searchkeys) == 3:
                            root.parent.temp_child = Node(searchkeyList[2][0], searchkeyList[2][1])
                            root.searchkeys.remove(searchkeyList[2])

                        else:
                            root.parent.middle_child.searchkeys.append(searchkeyList[2])
                            root.parent.middle_child = self.sort(root.parent.middle_child)
                            root.searchkeys.remove(searchkeyList[2])
                    else:
                        root.parent.middle_child = Node(searchkeyList[2][0], searchkeyList[2][1], root.parent)
                        root.searchkeys.remove(searchkeyList[2])
                if len(root.parent.searchkeys) == 3:
                    self.__trickleUp(root.parent)

        if self.hasAllChildren(root):
            if root.parent is None:
                if root.temp_child is not None:
                    oldRoot = copy.deepcopy(self.root)
                    if root.temp_child.searchkeys[0] < root.middle_child.searchkeys[0]:
                        self.root = None
                        self.root = Node(oldRoot.searchkeys[1][0], oldRoot.searchkeys[1][1])
                        self.root.left_child = Node(oldRoot.searchkeys[0][0], oldRoot.searchkeys[0][1])
                        self.root.left_child.parent = self.root
                        self.root.right_child = Node(oldRoot.searchkeys[2][0], oldRoot.searchkeys[2][1])
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
                        self.root = Node(oldRoot.searchkeys[1][0], oldRoot.searchkeys[1][1])
                        self.root.left_child = Node(oldRoot.searchkeys[0][0], oldRoot.searchkeys[0][1])
                        self.root.left_child.parent = self.root
                        self.root.right_child = Node(oldRoot.searchkeys[2][0], oldRoot.searchkeys[2][1])
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
                            root.parent.right_child = Node(oldNode.searchkeys[1][0], oldNode.searchkeys[1][1])
                            root = root.parent.right_child
                        else:
                            root.parent.left_child = Node(oldNode.searchkeys[1][0], oldNode.searchkeys[1][1])
                            root = root.parent.left_child
                        root.left_child = Node(oldNode.searchkeys[0][0], oldNode.searchkeys[0][1])
                        root.left_child.parent = root
                        root.right_child = Node(oldNode.searchkeys[2][0], oldNode.searchkeys[2][1])
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
                        if root.searchkeys[0][0] > root.parent.searchkeys[-1][0]:
                            root.parent.right_child = Node(oldNode.searchkeys[1][0], oldNode.searchkeys[1][1])
                            root = root.parent.right_child
                        else:
                            root.parent.left_child = Node(oldNode.searchkeys[1][0], oldNode.searchkeys[1][1])
                            root = root.parent.left_child
                        root.left_child = Node(oldNode.searchkeys[0][0], oldNode.searchkeys[0][1])
                        root.left_child.parent = root
                        root.right_child = Node(oldNode.searchkeys[2][0], oldNode.searchkeys[2][1])
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





