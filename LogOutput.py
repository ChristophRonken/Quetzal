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
            self.startRow()
            self.writecube(str(tick))
            workloadCopy = copy.deepcopy(store.workload)
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
            self.writecube(stackstring)

            workerCopy = copy.deepcopy(store.workers)
            while not workerCopy.isEmpty():
                worker = workerCopy.retrieve()
                if worker.order is not None:
                    self.writecube(str(worker.order.credit))
                else:
                    self.writecube(" ")
                workerCopy.delete(None)

            newOrderCopy = copy.deepcopy(store.newOrders)
            if newOrderCopy.isEmpty():
                self.writecube(" ")
            else:
                orderstring = ""
                while not newOrderCopy.isEmpty():
                    order = newOrderCopy.retrieve()
                    orderstring += str(order.chocolateMilkId)
                    newOrderCopy.delete(None)
                    if not newOrderCopy.isEmpty():
                        orderstring += " | "
                self.writecube(orderstring)

            waitingOrderCopy = copy.deepcopy(store.waitingOrders)
            if waitingOrderCopy.isEmpty():
                self.writecube(" ")
            else:
                orderstring = ""
                while not waitingOrderCopy.isEmpty():
                    order = waitingOrderCopy.retrieve()
                    orderstring += str(order.chocolateMilkId)
                    waitingOrderCopy.delete(None)
                    if not waitingOrderCopy.isEmpty():
                        orderstring += " | "
                self.writecube(orderstring)

            stockList = [store.milkChocolateStock, store.whiteChocolateStock, store.brownChocolateStock,
                         store.darkChocolateStock, store.honeyStock, store.marshmallowStock, store.chiliStock]
            for i in range(0, len(stockList)):
                j = 0
                stockCopy = copy.deepcopy(stockList[i])
                while not stockCopy.isEmpty():
                    item = stockCopy.retrieve()
                    stockCopy.delete(item.searchkey)
                    j += 1
                    if stockCopy.isEmpty():
                        self.writecube(str(j))

            self.endRow()
        return

    def writecube(self, string):
        self.logString += '''    <td>''' + string + '''</td>
                '''
        return

    def startRow(self):
        self.logString += '''    <tr>
                '''

    def endRow(self):
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
