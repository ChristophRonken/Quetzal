import graphviz as gv
import copy
stackCounter = 1


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
