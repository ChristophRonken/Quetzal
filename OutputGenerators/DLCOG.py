import graphviz as gv
import copy
dlcCounter, hashdlcCounter = (1,)*2


def printDLC(dlc, customName=None):
    global dlcCounter, hashdlcCounter
    dlcCopy = copy.deepcopy(dlc)
    figuur = gv.Graph(format='png')

    figuur.node("Head", label="Head", style="solid", shape="circle")
    figuur.node("Tail", label="Tail", style="solid", shape="circle")

    headNode = dlcCopy.head.next

    count = 0
    while headNode != dlcCopy.tail:
        figuur.node(str(count), label=str(headNode.searchkey), style="solid", shape="box")
        if count == 0:
            figuur.edge("Head", str(count))
        if count > 0:
            figuur.edge(str(count-1), str(count), arrowhead="normal", dir="forward")
            figuur.edge(str(count), str(count-1), arrowhead="normal", dir="forward")
        if headNode.next == dlcCopy.tail:
            figuur.edge(str(count), "Tail")
        headNode = headNode.next
        count += 1
    if not customName:
        figuur.render(filename='DotFiles/dll-' + str(dlcCounter) + '.dot')
        dlcCounter += 1
    else:
        figuur.render(filename='DotFiles/' + customName + '/' + customName + str(hashdlcCounter) + '.dot')
        hashdlcCounter += 1

    return