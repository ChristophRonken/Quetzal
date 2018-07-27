import copy


class LogOutput:

    def __init__(self):
        self.logString = None
        self.rowLength = 11

    def addRow(self, store, tick):
        workerCopy = copy.deepcopy(store.workers)
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

            while not workerCopy.isEmpty():
                self.rowLength += 1
                firstworker = workerCopy.retrieve()
                self.logString += '''<td>''' + firstworker.firstName + " " + firstworker.lastName + '''</td>
                '''
                workerCopy.delete(None)
            self.logString += '''<td>wit</td>
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
            while not workerCopy.isEmpty():
                firstworker = workerCopy.retrieve()
                self.writecube(str(firstworker.workLoad))
                workerCopy.delete(None)
            self.writecube(str(tick))
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
