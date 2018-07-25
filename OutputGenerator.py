import graphviz as gv
import copy
bstCounter, hlinCounter, hquadCounter, hsepCounter, queueCounter, stackCounter = (1,)*6
from ADT_Christoph.HashTable.HashTable import HashTableType, Bucket


def printStack(stack):
    stackCopy = copy.deepcopy(stack)
    figuur = gv.Graph(format='png')
    figuur.node('TOP', label="TOP", style="solid", shape="circle")

    count = 0
    while not stackCopy.isEmpty():
        stackCopy.popDisplay()
        figuur.node(str(count), label=str(stackCopy.topItem), style="solid", shape="box")
        count += 1

    if count > 1:
        figuur.edge('TOP', str(0))
        for i in range(0, count-1):
            figuur.edge(str(i), str(i+1), arrowhead="normal", dir="forward")
    if count == 1:
        figuur.edge('TOP', str(0))

    global stackCounter
    figuur.render(filename='DotFiles/stack-'+str(stackCounter)+'.dot')
    stackCounter += 1


def printQueue(queue):
    queueCopy = copy.deepcopy(queue)
    figuur = gv.Graph(format='png')
    figuur.node('Front', label="Front", style="solid", shape="circle")
    figuur.node('Back', label="Back", style="solid", shape="circle")

    count = 0
    while not queueCopy.isEmpty():
        figuur.node(str(count), label=str(queueCopy.getFront()), style="solid", shape="box")
        queueCopy.deQueue()
        count += 1

    if count > 1:
        figuur.edge('Front', str(0))
        for i in range(0, count-1):
            figuur.edge(str(i), str(i+1))
        figuur.edge(str(count-1), 'Back')
    if count == 1:
        figuur.edge('Front', str(0))
        figuur.edge(str(0), 'Back')
    if count == 0:
        figuur.edge('Front', 'Back')

    global queueCounter
    figuur.render(filename='DotFiles/queue-'+str(queueCounter)+'.dot')
    queueCounter += 1


def printHashTable(hashtable):
    hashtableCopy = copy.deepcopy(hashtable)
    figuur = gv.Graph(format='png')

    figuur.node("Zero", label="Zero", style="solid", shape="circle")
    figuur.node("Length", label="Length", style="solid", shape="circle")

    global hlinCounter, hquadCounter, hsepCounter

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

        figuur.render(filename='DotFiles/hsep-' + str(hsepCounter) + '.dot')
        hsepCounter += 1

