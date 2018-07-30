import graphviz as gv
import copy
queueCounter = 1


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
