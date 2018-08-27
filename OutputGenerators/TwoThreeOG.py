import graphviz as gv
import copy
TreeCounter = 1


rootMade = False


def print23(tree):
    global TreeCounter
    treeCopy = copy.deepcopy(tree)

    figuur = gv.Graph(format='png')
    figuur.node('Root', label="Root", style="solid", shape="circle")

    make23(treeCopy.root, figuur)
    rootstring = ""
    i = 0
    while i < len(treeCopy.root.searchkeys):
        rootstring += str(treeCopy.root.searchkeys[i][0])
        rootstring += ", "
        i += 1
    rootstring = rootstring[:-2]
    figuur.edge('Root', rootstring)

    figuur.render(filename='DotFiles/23-' + str(TreeCounter) + '.dot')
    TreeCounter += 1
    return


def make23(root, figuur):
    global rootMade

    if root.searchkeys is not None:
        string = ""
        leftstring = ""
        middlestring = ""
        rightstring = ""

        i = 0
        while i < len(root.searchkeys):
            string += str(root.searchkeys[i][0])
            string += ", "
            i += 1

        if root.left_child is not None:
            i = 0
            while i < len(root.left_child.searchkeys):
                leftstring += str(root.left_child.searchkeys[i][0])
                leftstring += ", "
                i += 1

        if root.middle_child:
            i = 0
            while i < len(root.middle_child.searchkeys):
                middlestring += str(root.middle_child.searchkeys[i][0])
                middlestring += ", "
                i += 1

        if root.right_child:
            i = 0
            while i < len(root.right_child.searchkeys):
                rightstring += str(root.right_child.searchkeys[i][0])
                rightstring += ", "
                i += 1

        string = string[:-2]
        leftstring = leftstring[:-2]
        middlestring = middlestring[:-2]
        rightstring = rightstring[:-2]

        if root.left_child is not None:
            print("left: ", leftstring)

        if root.middle_child is not None:
            print("middle: ", middlestring)

        if root.right_child is not None:
            print("right: ", rightstring)

        if not rootMade:
            figuur.node(string, label=string, style="solid", shape="circle")
            rootMade = True
        if root.left_child is not None:
            figuur.edge(string, leftstring, arrowhead="normal", dir="forward")
            make23(root.left_child, figuur)
        if root.middle_child is not None:
            figuur.edge(string, middlestring, arrowhead="normal", dir="forward")
            make23(root.middle_child, figuur)
        if root.right_child is not None:
            figuur.edge(string, rightstring, arrowhead="normal", dir="forward")
            make23(root.right_child, figuur)