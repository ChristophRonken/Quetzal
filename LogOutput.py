import copy


class LogOutput:

    def __init__(self):
        self.__logString = None
        self.__rowLength = 11

    def addRow(self, store, tick):
        if self.__logString is None:
            self.__logString = '''<html>
    <head>
    <style>
        table {
            border-collapse: collapse;
        }

        table, td, th {
            border: 1px solid black;
        }
    </style>
</head>
    <body>
        <h1>Log</h1>
        <table>
            </thead>
                <td>tijdstip</td>
                <td>Stack</td>
                '''
            workerCopy = copy.deepcopy(store.getWorkers())
            while not workerCopy.isEmpty():
                self.__rowLength += 1
                firstworker = workerCopy.retrieve(None)
                self.__logString += '''<td>''' + firstworker.getFirstName() + " " + firstworker.getLastName() + '''</td>
                '''
                workerCopy.delete(None)
            self.__logString += '''<td>Nieuwe bestellingen</td>
                <td>Wachtende bestellingen</td>
                <td>wit</td>
                <td>melk</td>
                <td>bruin</td>
                <td>zwart</td>
                <td>honing</td>
                <td>marshmallow</td>
                <td>chili</td>
                <td>money</td>
            </thead>
            <tbody>
            '''
        else:
            self.__startRow()
            self.__writecube(str(tick))
            stackstring = ""

            workerCopy = copy.deepcopy(store.getWorkers())
            while not workerCopy.isEmpty():
                if not workerCopy.retrieve(None).getIsBusy():
                    stackstring += str(workerCopy.retrieve(None).getWorkload())
                    workerCopy.delete(None)
                else:
                    stackstring += "_"
                    workerCopy.delete(None)
                if not workerCopy.isEmpty():
                    stackstring += " | "
            self.__writecube(stackstring)

            workerCopy = copy.deepcopy(store.getWorkers())
            while not workerCopy.isEmpty():
                worker = workerCopy.retrieve(None)
                if worker.getIsBusy():
                    self.__writecube(str(worker.getBusyTime()))
                else:
                    self.__writecube(" ")
                workerCopy.delete(None)

            newOrderCopy = copy.deepcopy(store.getNewOrders())
            if newOrderCopy.isEmpty():
                self.__writecube(" ")
            else:
                orderstring = ""
                while not newOrderCopy.isEmpty():
                    order = newOrderCopy.retrieve(None)
                    orderstring += str(order.getChocolateMilkId())
                    newOrderCopy.delete(None)
                    if not newOrderCopy.isEmpty():
                        orderstring += " | "
                self.__writecube(orderstring)

            waitingOrderCopy = copy.deepcopy(store.getWaitingOrders())
            if waitingOrderCopy.isEmpty():
                self.__writecube(" ")
            else:
                orderstring = ""
                while not waitingOrderCopy.isEmpty():
                    order = waitingOrderCopy.retrieve(None)
                    orderstring += str(order.getChocolateMilkId())
                    waitingOrderCopy.delete(None)
                    if not waitingOrderCopy.isEmpty():
                        orderstring += " | "
                self.__writecube(orderstring)

            stockList = [store.getWhiteChocolateStock(), store.getMilkChocolateStock(),
                         store.getBrownChocolateStock(), store.getDarkChocolateStock(),
                         store.getHoneyStock(), store.getMarshmallowStock(), store.getChilipepperStock()]
            for i in range(0, len(stockList)):
                j = 0
                stockCopy = copy.deepcopy(stockList[i])
                if stockCopy.isEmpty():
                    self.__writecube(str(0))
                while not stockCopy.isEmpty():
                    item = stockCopy.retrieve(None)
                    stockCopy.delete(item.searchkey)
                    j += 1
                    if stockCopy.isEmpty():
                        self.__writecube(str(j))
            self.__writecube('€'+ str(store.getMoney()))
            self.__endRow()
        return

    def __writecube(self, string):
        self.__logString += '''    <td>''' + string + '''</td>
                '''
        return

    def __startRow(self):
        self.__logString += '''    <tr>
                '''

    def __endRow(self):
        self.__logString += '''</tr>
            '''

    def writeHtml(self):
        printString = self.__logString
        printString += '''</tbody>
        </table>
    </body>
</html>'''

        file = open("outputLog.html", "w")
        file.write(printString)
