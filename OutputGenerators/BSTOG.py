import graphviz as gv
import copy
bstCounter = 1


rootMade = False


def printBST(bst):
    global bstCounter
    bstCopy = copy.deepcopy(bst)

    figuur = gv.Graph(format='png')
    figuur.node('Root', label="Root", style="solid", shape="circle")

    makebst(bstCopy.root, figuur)
    figuur.edge('Root', str(bstCopy.root.searchkey))

    figuur.render(filename='DotFiles/bst-' + str(bstCounter) + '.dot')
    bstCounter += 1
    return


def makebst(root, figuur):
    global rootMade

    if root.searchkey:
        if not rootMade:
            figuur.node(str(root.searchkey), label=str(root.searchkey), style="solid", shape="circle")
            rootMade = True
        if root.lchild:
            figuur.node(str(root.lchild.searchkey), label=str(root.lchild.searchkey), style="solid", shape="circle")
            figuur.edge(str(root.searchkey), str(root.lchild.searchkey), arrowhead="normal", dir="forward")
            makebst(root.lchild, figuur)
        if root.rchild:
            figuur.node(str(root.rchild.searchkey), label=str(root.rchild.searchkey), style="solid", shape="circle")
            figuur.edge(str(root.searchkey), str(root.rchild.searchkey), arrowhead="normal", dir="forward")
            makebst(root.rchild, figuur)
