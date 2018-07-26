import graphviz as gv
import copy
from ADT_Christoph.HashTable.HashTable import HashTableType, Bucket
from ADT_Christoph.DoublyLinkedChain.DoublyLinkedChain import DoublyLinkedChain
from ADT_Cedric.CircularChain import CircularChain
bstCounter, hlinCounter, hquadCounter, hsepCounter, queueCounter, stackCounter, dlcCounter, clcCounter, hashdlcCounter, hashclcCounter = (1,)*10


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
    return


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
            figuur.edge(str(i), str(i+1), arrowhead="normal", dir="back")
        figuur.edge(str(count-1), 'Back')
    if count == 1:
        figuur.edge('Front', str(0))
        figuur.edge(str(0), 'Back')
    if count == 0:
        figuur.edge('Front', 'Back')

    global queueCounter
    figuur.render(filename='DotFiles/queue-'+str(queueCounter)+'.dot')
    queueCounter += 1
    return


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
            if isinstance(hashtableCopy.table[i], CircularChain):
                figuur.node("CLC" + str(i), label="hashtableCLL" + str(i), style="solid", shape="box")
                printCLC(hashtableCopy.table[i], "hashtableCLL")
            elif isinstance(hashtableCopy.table[i], DoublyLinkedChain):
                figuur.node("DLC" + str(i), label="hashtableDLL" + str(i+1), style="solid", shape="box")
                printDLC(hashtableCopy.table[i], "hashtableDLL")
            if i == 0:
                if isinstance(hashtableCopy.table[i], CircularChain):
                    figuur.edge("Zero", "CLC" + str(i))
                if isinstance(hashtableCopy.table[i], DoublyLinkedChain):
                    figuur.edge("Zero", "DLC" + str(i))
            if i > 0:
                if isinstance(hashtableCopy.table[i], CircularChain):
                    figuur.edge("CLC" + str(i - 1), "CLC" + str(i))
                if isinstance(hashtableCopy.table[i], DoublyLinkedChain):
                    figuur.edge("DLC" + str(i - 1), "DLC" + str(i))
            if i == len(hashtableCopy.table) - 1:
                if isinstance(hashtableCopy.table[i], CircularChain):
                    figuur.edge("CLC" + str(i), "Length")
                if isinstance(hashtableCopy.table[i], DoublyLinkedChain):
                    figuur.edge("DLC" + str(i), "Length")

        figuur.render(filename='DotFiles/hsep-' + str(hsepCounter) + '.dot')
        hsepCounter += 1

    return


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
            figuur.edge(str(root.searchkey), str(root.lchild.searchkey))
            makebst(root.lchild, figuur)
        if root.rchild:
            figuur.node(str(root.rchild.searchkey), label=str(root.rchild.searchkey), style="solid", shape="circle")
            figuur.edge(str(root.searchkey), str(root.rchild.searchkey))
            makebst(root.rchild, figuur)


def printDLC(dlc, customName=None):
    global dlcCounter, hashdlcCounter
    dlcCopy = copy.deepcopy(dlc)
    figuur = gv.Graph(format='png')

    figuur.node("Head", label="Head", style="solid", shape="circle")
    figuur.node("Tail", label="Tail", style="solid", shape="circle")

    headNode = dlcCopy.head.next

    count = 0
    while headNode != dlcCopy.tail:
        figuur.node(str(headNode.searchkey), label=str(headNode.searchkey), style="solid", shape="box")
        if count == 0:
            figuur.edge("Head", str(headNode.searchkey))
        if count > 0:
            figuur.edge(str(headNode.prev.searchkey), str(headNode.searchkey), arrowhead="normal", dir="forward")
            figuur.edge(str(headNode.searchkey), str(headNode.prev.searchkey), arrowhead="normal", dir="forward")
        if headNode.next == dlcCopy.tail:
            figuur.edge(str(headNode.searchkey), "Tail")
        headNode = headNode.next
        count += 1
    if not customName:
        figuur.render(filename='DotFiles/dll-' + str(dlcCounter) + '.dot')
        dlcCounter += 1
    else:
        figuur.render(filename='DotFiles/' + customName + '/' + customName + str(hashdlcCounter) + '.dot')
        hashdlcCounter += 1

    return


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
