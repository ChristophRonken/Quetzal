from Simulator import ADTSimulator
from Wrapper import *
from InputReader import InputReader
from Ingredient import *
from OutputGenerator import  *


class Quetzal:

    def __init__(self):
        self.orders = BSTWrapper()
        self.marshmallowStock = DLCWrapper()
        self.marshmallowStock.create()
        self.milkChocolateStock = DLCWrapper()
        self.milkChocolateStock.create()
        self.darkChocolateStock = DLCWrapper()
        self.darkChocolateStock.create()
        self.whiteChocolateStock = DLCWrapper()
        self.whiteChocolateStock.create()
        self.brownChocolateStock = DLCWrapper()
        self.brownChocolateStock.create()
        self.honeyStock = DLCWrapper()
        self.chiliStock = DLCWrapper()
        self.users = DLCWrapper()
        self.workers = DLCWrapper()

        self.inputReader = InputReader("system.txt")
        self.inputReader.StoreInputData()
        self.inputReader.InputFileToCommands()

    def ADTSimulation(self):
        ADTSimulator().runADTSimulation()

    def createorder(self):
        return

    def addOrder(self, order):
        return self.orders.insert('orderid', order)

    def honeyRestock(self, honeyItem):
        self.honeyStock.insert('vervaldatum', honeyItem)
        return

    def chiliRestock(self, chiliItem):
        self.chiliStock.insert('vervaldatum', chiliItem)
        return

    def marshmallowRestock(self, marshmallowItem):
        self.marshmallowStock.insert('vervaldatum', marshmallowItem)
        return

    def milkChocolateRestock(self, expirationDate, milkChoocolateItem):
        self.milkChocolateStock.insert(expirationDate, milkChoocolateItem)
        return

    def darkChocolateRestock(self, expirationDate, darkChoocolateItem):
        self.darkChocolateStock.insert(expirationDate, darkChoocolateItem)
        return

    def whiteChocolateRestock(self, expirationDate, whiteChoocolateItem):
        self.whiteChocolateStock.insert(expirationDate, whiteChoocolateItem)
        return

    def brownChocolateRestock(self, expirationDate, brownChoocolateItem):
        self.brownChocolateStock.insert(expirationDate, brownChoocolateItem)
        return

    def StoreSimulation(self):
        i = 0
        newItem = False
        searchkey = False
        while i != len(self.inputReader.commands):
            print(self.inputReader.commands[i])
            if self.inputReader.commands[i] == "init":
                i += 1
                continue
            if self.inputReader.commands[i] == "honing":
                i += 1
                return

            if self.inputReader.commands[i] == "shot":
                i += 1
                type = self.inputReader.commands[i]
                i += 1
                amount = self.inputReader.commands[i]
                i += 1
                year = self.inputReader.commands[i]
                i += 1
                month = self.inputReader.commands[i]
                i += 1
                day = self.inputReader.commands[i]
                i += 1
                if type == "melk":
                    for j in range(0, int(amount)):
                        milkChoocolateItem = ChocolateShot(int(year+month+day), ChocolateShotType.milk)
                        self.milkChocolateRestock(milkChoocolateItem.expirationDate, milkChoocolateItem)
                    continue
                elif type == "wit":
                    for j in range(0, int(amount)):
                        whiteChoocolateItem = ChocolateShot(int(year+month+day), ChocolateShotType.white)
                        self.whiteChocolateRestock(whiteChoocolateItem.expirationDate, whiteChoocolateItem)
                    continue
                elif type == "zwart":
                    for j in range(0, int(amount)):
                        darkChoocolateItem = ChocolateShot(int(year+month+day), ChocolateShotType.dark)
                        self.darkChocolateRestock(darkChoocolateItem.expirationDate, darkChoocolateItem)
                    continue
                elif type == "bruin":
                    for j in range(0, int(amount)):
                        brownChoocolateItem = ChocolateShot(int(year+month+day), ChocolateShotType.brown)
                        self.brownChocolateRestock(brownChoocolateItem.expirationDate, brownChoocolateItem)
                    continue
                return False
        return


a = Quetzal()
a.StoreSimulation()
printDLC(a.milkChocolateStock.ADT)
printDLC(a.darkChocolateStock.ADT)
printDLC(a.brownChocolateStock.ADT)
printDLC(a.whiteChocolateStock.ADT)


