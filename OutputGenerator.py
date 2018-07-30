import graphviz as gv
import copy
from Enums import HashTableType
from Wrappers.CLCWrapper import CLCWrapper
from Wrappers.DLCWrapper import DLCWrapper
bstCounter, hlinCounter, hquadCounter, hsepCounter, queueCounter, stackCounter, dlcCounter, clcCounter, hashdlcCounter, hashclcCounter = (1,)*10



def printCLC(clc, customName=None):
    global clcCounter, hashclcCounter
    clcCopy = copy.deepcopy(clc)
    figuur = gv.Graph(format='png')

    figuur.node("Root", label="Root", style="solid", shape="circle")
    startNode = clcCopy.root
    if clcCopy.isEmpty():
        pass
    else:
        figuur.node(str(startNode.searchkey), label=str(startNode.searchkey), style="solid", shape="circle")
        figuur.edge("Root", str(startNode.searchkey))
        while startNode.next != clcCopy.root:
            figuur.node(str(startNode.next.searchkey), label=str(startNode.next.searchkey), style="solid", shape="circle")
            figuur.edge(str(startNode.searchkey), str(startNode.next.searchkey), arrowhead="normal", dir="forward")
            startNode = startNode.next
        figuur.edge(str(startNode.searchkey), str(clcCopy.root.searchkey), arrowhead="normal", dir="forward")

    if not customName:
        figuur.render(filename='DotFiles/cll-' + str(clcCounter) + '.dot')
        clcCounter += 1
    else:
        figuur.render(filename='DotFiles/' + customName + '/' + customName + str(hashclcCounter) + '.dot')
        hashclcCounter += 1
    return
