import graphviz as gv

bstCounter, hashCounter, queueCounter, stackCounter = (0,)*4


def printStack(stackCopy):
    figuur = gv.Graph(format='png')
    figuur.node('TOP', label="TOP", style="solid", shape="box")

    i = 0
    while not stackCopy.isEmpty():
        stackCopy.popDisplay()
        figuur.node(str(i), label=str(stackCopy.topItem), style="solid", shape="box")
        i += 1

    if i > 1:
        figuur.edge('TOP', str(0))
        for i in range(0, i-1):
            figuur.edge(str(i), str(i+1), arrowhead="normal", dir="forward")
    if i == 1:
        figuur.edge('TOP', str(0))

    global stackCounter
    figuur.render(filename='DotFiles/stack-'+str(stackCounter)+'.dot')
    stackCounter += 1


def printQueue(queueCopy):
    figuur = gv.Graph(format='png')
    figuur.node('TOP', label="TOP", style="solid", shape="box")

    i = 0
    while not queueCopy.isEmpty():
        queueCopy.popDisplay()
        figuur.node(str(i), label=str(queueCopy.topItem), style="solid", shape="box")
        i += 1

    if i > 1:
        figuur.edge('TOP', str(0))
        for i in range(0, i-1):
            figuur.edge(str(i), str(i+1))
    if i == 1:
        figuur.edge('TOP', str(0))

    global queueCounter
    figuur.render(filename='DotFiles/stack-'+str(queueCounter)+'.dot')
    queueCounter += 1
