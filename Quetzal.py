from Store import Store, text_from_bits, text_to_bits

from Wrapper import *
from InputReader import InputReader
from Ingredient import *
from OutputGenerator import *
from Gebruiker import User
from Werknemer import Worker


class ADTSimulator:

    def __init__(self):
        self.inputReader = InputReader("adt.txt")
        self.inputReader.StoreInputData()
        self.inputReader.InputFileToCommands()
        self.Wrapper = None

    def runADTSimulation(self):
        i = 0
        newItem = False
        searchkey = False
        while i != len(self.inputReader.commands):
            print(self.inputReader.commands[i])

            if self.inputReader.commands[i] == "type=bst":
                self.Wrapper = BSTWrapper()
                self.Wrapper.create()
                newItem = False
                searchkey = True
                i += 1

            elif self.inputReader.commands[i] == "type=stack":
                self.Wrapper = StackWrapper()
                self.Wrapper.create()
                newItem = True
                searchkey = False
                i += 1

            elif self.inputReader.commands[i] == "type=queue":
                self.Wrapper = QueueWrapper()
                self.Wrapper.create()
                newItem = True
                searchkey = False
                i += 1

            elif self.inputReader.commands[i] == "type=dll":
                self.Wrapper = DLCWrapper()
                self.Wrapper.create()
                newItem = False
                searchkey = True
                i += 1

            elif self.inputReader.commands[i] == "type=cll":
                self.Wrapper = CLCWrapper()
                self.Wrapper.create()
                newItem = False
                searchkey = True
                i += 1

            elif self.inputReader.commands[i] == "type=hlin":
                self.Wrapper = HashWrapper()
                self.Wrapper.ADT.type = HashTableType.Type1
                self.Wrapper.create()
                newItem = False
                searchkey = True
                i += 1

            elif self.inputReader.commands[i] == "type=hquad":
                self.Wrapper = HashWrapper()
                self.Wrapper.ADT.type = HashTableType.Type2
                self.Wrapper.create()
                newItem = False
                searchkey = True
                i += 1

            elif self.inputReader.commands[i] == "type=hsep":
                self.Wrapper = HashWrapper()
                self.Wrapper.ADT.type = HashTableType.Type3
                self.Wrapper.create()
                newItem = False
                searchkey = True
                i += 1

            elif self.inputReader.commands[i] == "insert":
                i += 1
                if not newItem:
                    self.Wrapper.insert(int(self.inputReader.commands[i]), None)
                elif not searchkey:
                    self.Wrapper.insert(None, int(self.inputReader.commands[i]))
                i += 1
            elif self.inputReader.commands[i] == "delete":
                i += 1
                if not searchkey:
                    self.Wrapper.delete(None)
                else:
                    self.Wrapper.delete(int(self.inputReader.commands[i]))
                    i += 1

            elif self.inputReader.commands[i] == "print":
                self.Wrapper.print()
                i += 1
        return


class StoreSimulator:
    def __init__(self):
        self.store = Store()
        self.inputReader = InputReader("system.txt")
        self.inputReader.StoreInputData()
        self.inputReader.InputFileToCommands()

    def storeSimulation(self):
        i = 0
        while i != len(self.inputReader.commands):
            print(self.inputReader.commands[i])
            if self.inputReader.commands[i] == "init":
                i += 1
                self.quetzal.createQuetzal()
                continue

            if self.inputReader.commands[i] == "start":
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
                        self.quetzal.milkChocolateStock.insert(milkChoocolateItem.expirationDate, milkChoocolateItem)
                    continue
                elif type == "wit":
                    for j in range(0, int(amount)):
                        whiteChoocolateItem = ChocolateShot(int(year+month+day), ChocolateShotType.white)
                        self.quetzal.whiteChocolateStock.insert(whiteChoocolateItem.expirationDate, whiteChoocolateItem)
                    continue
                elif type == "zwart":
                    for j in range(0, int(amount)):
                        darkChoocolateItem = ChocolateShot(int(year+month+day), ChocolateShotType.dark)
                        self.quetzal.darkChocolateStock.insert(darkChoocolateItem.expirationDate, darkChoocolateItem)
                    continue
                elif type == "bruin":
                    for j in range(0, int(amount)):
                        brownChoocolateItem = ChocolateShot(int(year+month+day), ChocolateShotType.brown)
                        self.quetzal.brownChocolateStock.insert(brownChoocolateItem.expirationDate, brownChoocolateItem)
                    continue
                return False
            if self.inputReader.commands[i] == "honing":
                i += 1
                amount = self.inputReader.commands[i]
                i += 1
                year = self.inputReader.commands[i]
                i += 1
                month = self.inputReader.commands[i]
                i += 1
                day = self.inputReader.commands[i]
                i += 1
                for j in range(0, int(amount)):
                    honeyItem = Honey(int(year + month + day))
                    self.quetzal.honeyStock.insert(honeyItem.expirationDate, honeyItem)
                continue
            if self.inputReader.commands[i] == "marshmallow":
                i += 1
                amount = self.inputReader.commands[i]
                i += 1
                year = self.inputReader.commands[i]
                i += 1
                month = self.inputReader.commands[i]
                i += 1
                day = self.inputReader.commands[i]
                i += 1
                for j in range(0, int(amount)):
                    marshmallowItem = Marshmallow(int(year + month + day))
                    self.quetzal.marshmallowStock.insert(marshmallowItem.expirationDate, marshmallowItem)
                continue
            if self.inputReader.commands[i] == "chili":
                i += 1
                amount = self.inputReader.commands[i]
                i += 1
                year = self.inputReader.commands[i]
                i += 1
                month = self.inputReader.commands[i]
                i += 1
                day = self.inputReader.commands[i]
                i += 1
                for j in range(0, int(amount)):
                    chiliItem = Marshmallow(int(year + month + day))
                    self.quetzal.chiliStock.insert(chiliItem.expirationDate, chiliItem)
                continue
            if self.inputReader.commands[i] == "gebruiker":
                i += 1
                firstName = self.inputReader.commands[i]
                i += 1
                lastName = self.inputReader.commands[i]
                i += 1
                email = self.inputReader.commands[i]
                i += 1
                userItem = User(firstName, lastName, email)
                self.quetzal.users.insert(text_to_bits(userItem.email), userItem)
                print(text_from_bits(text_to_bits(userItem.email)))
                continue
            if self.inputReader.commands[i] == "werknemer":
                i += 1
                firstName = self.inputReader.commands[i]
                i += 1
                lastName = self.inputReader.commands[i]
                i += 1
                workLoad = self.inputReader.commands[i]
                i += 1
                workerItem = Worker(firstName, lastName, workLoad)
                self.quetzal.workers.insert(workerItem.workerId, workerItem)
                continue
            if self.inputReader.commands[i] == "bestel":
                return
        return


a = ADTSimulator()
a.runADTSimulation()
'''
a = StoreSimulator()
a.storeSimulation()
printDLC(a.quetzal.milkChocolateStock.ADT)
printDLC(a.quetzal.darkChocolateStock.ADT)
printDLC(a.quetzal.brownChocolateStock.ADT)
printDLC(a.quetzal.whiteChocolateStock.ADT)
printDLC(a.quetzal.honeyStock.ADT)
printDLC(a.quetzal.marshmallowStock.ADT)
printDLC(a.quetzal.users.ADT)
printDLC(a.quetzal.workers.ADT)
'''