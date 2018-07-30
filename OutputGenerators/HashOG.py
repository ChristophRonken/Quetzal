import graphviz as gv
import copy
from Enums import HashTableType
from OutputGenerators.DLCOG import printDLC
from OutputGenerators.CLCOG import printCLC
from Wrappers.CLCWrapper import CLCWrapper
from Wrappers.DLCWrapper import DLCWrapper
hlinCounter, hquadCounter, hsepCounter, hashclcCounter = (1,)*4


def printHashTable(hashtable):
    global hlinCounter, hquadCounter, hsepCounter
    hashtableCopy = copy.deepcopy(hashtable)
    figuur = gv.Graph(format='png')

    figuur.node("Zero", label="Zero", style="solid", shape="circle")
    figuur.node("Length", label="Length", style="solid", shape="circle")

    if hashtableCopy.type == HashTableType.Type1:
        for i in range(0, len(hashtableCopy.table)):
            figuur.node(str(i), label=str(hashtable.table[i].searchkey), style="solid", shape="box")
            if i == 0:
                figuur.edge("Zero", str(i))
            if i > 0:
                figuur.edge(str(i-1), str(i))
            if i == len(hashtableCopy.table)-1:
                figuur.edge(str(i), "Length")

        figuur.render(filename='DotFiles/hlin-' + str(hlinCounter) + '.dot')
        hlinCounter += 1

    if hashtableCopy.type == HashTableType.Type2:
        for i in range(0, len(hashtableCopy.table)):
            figuur.node(str(i), label=str(hashtable.table[i].searchkey), style="solid", shape="box")
            if i == 0:
                figuur.edge("Zero", str(i))
            if i > 0:
                figuur.edge(str(i-1), str(i))
            if i == len(hashtableCopy.table)-1:
                figuur.edge(str(i), "Length")

        figuur.render(filename='DotFiles/hquad-' + str(hquadCounter) + '.dot')
        hquadCounter += 1

    if hashtableCopy.type == HashTableType.Type3:
        for i in range(0, len(hashtableCopy.table)):
            if isinstance(hashtableCopy.table[i], CLCWrapper):
                figuur.node("CLC" + str(i), label="hashtableCLL" + str(i), style="solid", shape="box")
                printCLC(hashtableCopy.table[i].ADT, "hashtableCLL")
            elif isinstance(hashtableCopy.table[i], DLCWrapper):
                figuur.node("DLC" + str(i), label="hashtableDLL" + str(i+1), style="solid", shape="box")
                printDLC(hashtableCopy.table[i].ADT, "hashtableDLL")
            if i == 0:
                if isinstance(hashtableCopy.table[i], CLCWrapper):
                    figuur.edge("Zero", "CLC" + str(i))
                if isinstance(hashtableCopy.table[i], DLCWrapper):
                    figuur.edge("Zero", "DLC" + str(i))
            if i > 0:
                if isinstance(hashtableCopy.table[i], CLCWrapper):
                    figuur.edge("CLC" + str(i - 1), "CLC" + str(i))
                if isinstance(hashtableCopy.table[i], DLCWrapper):
                    figuur.edge("DLC" + str(i - 1), "DLC" + str(i))
            if i == len(hashtableCopy.table) - 1:
                if isinstance(hashtableCopy.table[i], CLCWrapper):
                    figuur.edge("CLC" + str(i), "Length")
                if isinstance(hashtableCopy.table[i], DLCWrapper):
                    figuur.edge("DLC" + str(i), "Length")

        figuur.render(filename='DotFiles/hsep-' + str(hsepCounter) + '.dot')
        hsepCounter += 1

    return