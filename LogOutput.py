import copy


class LogOutput:

    def __init__(self):
        self.logString = None
        self.rowLength = 11

    def addRow(self, store, tick):
        if self.logString is None:
            self.logString = '''<html>
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
            workerCopy = copy.deepcopy(store.workers)
            while not workerCopy.isEmpty():
                self.rowLength += 1
                firstworker = workerCopy.retrieve()
                self.logString += '''<td>''' + firstworker.firstName + " " + firstworker.lastName + '''</td>
                '''
                workerCopy.delete(None)
            self.logString += '''<td>Nieuwe bestellingen</td>
                <td>Wachtende bestellingen</td>
                <td>wit</td>
                <td>melk</td>
                <td>bruin</td>
                <td>zwart</td>
                <td>honing</td>
                <td>marshmallow</td>
                <td>chili</td>
            </thead>
            <tbody>
            '''
        else:
            self.__startRow()
            self.__writecube(str(tick))
            stackstring = ""

            workerCopy = copy.deepcopy(store.workers)
            while not workerCopy.isEmpty():
                if not workerCopy.retrieve().isBusy:
                    stackstring += str(workerCopy.retrieve().workLoad)
                    workerCopy.delete(None)
                else:
                    stackstring += "_"
                    workerCopy.delete(None)
                if not workerCopy.isEmpty():
                    stackstring += " | "
            self.__writecube(stackstring)

            workerCopy = copy.deepcopy(store.workers)
            while not workerCopy.isEmpty():
                worker = workerCopy.retrieve()
                if worker.isBusy:
                    self.__writecube(str(worker.busyTime))
                else:
                    self.__writecube(" ")
                workerCopy.delete(None)

            newOrderCopy = copy.deepcopy(store.newOrders)
            if newOrderCopy.isEmpty():
                self.__writecube(" ")
            else:
                orderstring = ""
                while not newOrderCopy.isEmpty():
                    order = newOrderCopy.retrieve()
                    orderstring += str(order.chocolateMilkId)
                    newOrderCopy.delete(None)
                    if not newOrderCopy.isEmpty():
                        orderstring += " | "
                self.__writecube(orderstring)

            waitingOrderCopy = copy.deepcopy(store.waitingOrders)
            if waitingOrderCopy.isEmpty():
                self.__writecube(" ")
            else:
                orderstring = ""
                while not waitingOrderCopy.isEmpty():
                    order = waitingOrderCopy.retrieve()
                    orderstring += str(order.chocolateMilkId)
                    waitingOrderCopy.delete(None)
                    if not waitingOrderCopy.isEmpty():
                        orderstring += " | "
                self.__writecube(orderstring)

            stockList = [store.whiteChocolateStock, store.milkChocolateStock, store.brownChocolateStock,
                         store.darkChocolateStock, store.honeyStock, store.marshmallowStock, store.chiliStock]
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

            self.__endRow()
        return

    def __writecube(self, string):
        self.logString += '''    <td>''' + string + '''</td>
                '''
        return

    def __startRow(self):
        self.logString += '''    <tr>
                '''

    def __endRow(self):
        self.logString += '''</tr>
            '''

    def writeHtml(self):
        printString = self.logString
        printString += '''</tbody>
        </table>
    </body>
</html>'''

        file = open("outputLog.html", "w")
        file.write(printString)
