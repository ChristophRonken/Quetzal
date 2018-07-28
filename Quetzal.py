from Store import *
from LogOutput import LogOutput
from Wrapper import *
from InputReader import InputReader
from OutputGenerator import *


class ADTSimulator:

    def __init__(self):
        self.__inputReader = InputReader("adt.txt")
        self.__inputReader.StoreInputData()
        self.__inputReader.InputFileToCommands()
        self.__Wrapper = None

    def runADTSimulation(self):
        i = 0
        newItem = False
        searchkey = False
        while i != len(self.__inputReader.getCommands()):
            print(self.__inputReader.getCommands()[i])

            if self.__inputReader.getCommands()[i] == "type=bst":
                self.__Wrapper = BSTWrapper()
                self.__Wrapper.create()
                newItem = False
                searchkey = True
                i += 1

            elif self.__inputReader.getCommands()[i] == "type=stack":
                self.__Wrapper = StackWrapper()
                self.__Wrapper.create()
                newItem = True
                searchkey = False
                i += 1

            elif self.__inputReader.getCommands()[i] == "type=queue":
                self.__Wrapper = QueueWrapper()
                self.__Wrapper.create()
                newItem = True
                searchkey = False
                i += 1

            elif self.__inputReader.getCommands()[i] == "type=dll":
                self.__Wrapper = DLCWrapper()
                self.__Wrapper.create()
                newItem = False
                searchkey = True
                i += 1

            elif self.__inputReader.getCommands()[i] == "type=cll":
                self.__Wrapper = CLCWrapper()
                self.__Wrapper.create()
                newItem = False
                searchkey = True
                i += 1

            elif self.__inputReader.getCommands()[i] == "type=hlin":
                self.__Wrapper = HLinWrapper()
                self.__Wrapper.create()
                newItem = False
                searchkey = True
                i += 1

            elif self.__inputReader.getCommands()[i] == "type=hquad":
                self.__Wrapper = HQuadWrapper()
                self.__Wrapper.create()
                newItem = False
                searchkey = True
                i += 1

            elif self.__inputReader.getCommands()[i] == "type=hsep":
                self.__Wrapper = HSepWrapper()
                self.__Wrapper.create()
                newItem = False
                searchkey = True
                i += 1

            elif self.__inputReader.getCommands()[i] == "insert":
                i += 1
                if not newItem:
                    self.__Wrapper.insert(int(self.__inputReader.getCommands()[i]), None)
                elif not searchkey:
                    self.__Wrapper.insert(None, int(self.__inputReader.getCommands()[i]))
                i += 1
            elif self.__inputReader.getCommands()[i] == "delete":
                i += 1
                if not searchkey:
                    self.__Wrapper.delete(None)
                else:
                    self.__Wrapper.delete(int(self.__inputReader.getCommands()[i]))
                    i += 1

            elif self.__inputReader.getCommands()[i] == "print":
                self.__Wrapper.print()
                i += 1
        return


class StoreSimulator:
    def __init__(self):
        self.__store = Store()
        self.__logOut = LogOutput()
        self.__inputReader = InputReader("system.txt")
        self.__inputReader.StoreInputData()
        self.__inputReader.InputFileToCommands()
        self.__currentTick = 0

    def initialise(self):
        print(self.__inputReader.getLines())
        print(self.__inputReader.getCommands())
        i = 0
        while i != len(self.__inputReader.getCommands()):
            print(self.__inputReader.getCommands()[i])
            if self.__inputReader.getCommands()[i] == "init":
                i += 1
                self.__store.createStore()
                continue

            if self.__inputReader.getCommands()[i] == "start":
                i += 1
                return i

            if self.__inputReader.getCommands()[i] == "shot":
                i += 1
                type = self.__inputReader.getCommands()[i]
                i += 1
                amount = self.__inputReader.getCommands()[i]
                i += 1
                year = self.__inputReader.getCommands()[i]
                i += 1
                month = self.__inputReader.getCommands()[i]
                i += 1
                day = self.__inputReader.getCommands()[i]
                i += 1
                if type == "melk":
                    for j in range(0, int(amount)):
                        self.__store.restockMilkChocolateShot(int(year+month+day))
                    continue
                elif type == "wit":
                    for j in range(0, int(amount)):
                        self.__store.restockWhiteChocolateShot(int(year+month+day))
                    continue
                elif type == "zwart":
                    for j in range(0, int(amount)):
                        self.__store.restockDarkChocolateShot(int(year+month+day))
                    continue
                elif type == "bruin":
                    for j in range(0, int(amount)):
                        self.__store.restockBrownChocolateShot(int(year+month+day))
                    continue
                return False
            if self.__inputReader.getCommands()[i] == "honing":
                i += 1
                amount = self.__inputReader.getCommands()[i]
                i += 1
                year = self.__inputReader.getCommands()[i]
                i += 1
                month = self.__inputReader.getCommands()[i]
                i += 1
                day = self.__inputReader.getCommands()[i]
                i += 1
                for j in range(0, int(amount)):
                    self.__store.restockHoney(int(year + month + day))
                continue
            if self.__inputReader.getCommands()[i] == "marshmallow":
                i += 1
                amount = self.__inputReader.getCommands()[i]
                i += 1
                year = self.__inputReader.getCommands()[i]
                i += 1
                month = self.__inputReader.getCommands()[i]
                i += 1
                day = self.__inputReader.getCommands()[i]
                i += 1
                for j in range(0, int(amount)):
                    self.__store.restockMarshmallow(int(year + month + day))
                continue
            if self.__inputReader.getCommands()[i] == "chili":
                i += 1
                amount = self.__inputReader.getCommands()[i]
                i += 1
                year = self.__inputReader.getCommands()[i]
                i += 1
                month = self.__inputReader.getCommands()[i]
                i += 1
                day = self.__inputReader.getCommands()[i]
                i += 1
                for j in range(0, int(amount)):
                    self.__store.restockChilipepper(int(year + month + day))
                continue
            if self.__inputReader.getCommands()[i] == "gebruiker":
                i += 1
                firstName = self.__inputReader.getCommands()[i]
                i += 1
                lastName = self.__inputReader.getCommands()[i]
                i += 1
                email = self.__inputReader.getCommands()[i]
                i += 1
                self.__store.addUser(firstName, lastName, email)
                continue
            if self.__inputReader.getCommands()[i] == "werknemer":
                i += 1
                firstName = self.__inputReader.getCommands()[i]
                i += 1
                lastName = self.__inputReader.getCommands()[i]
                i += 1
                workLoad = self.__inputReader.getCommands()[i]
                i += 1
                self.__store.addWorker(firstName, lastName, int(workLoad))
                continue
        return

    def simulate(self, i):
        self.__logOut.addRow(self.__store, self.__currentTick)
        while i != len(self.__inputReader.getCommands()):
            print("currentTick = ", self.__currentTick)
            if self.__inputReader.getCommands()[i] == "pass":
                i += 1
                continue
            if self.__inputReader.getCommands()[i] == str(self.__currentTick + 1):
                self.__logOut.addRow(self.__store, self.__currentTick)
                print("working at tick ", self.__currentTick)
                self.__store.work()
                workersCopy = copy.deepcopy(self.__store.getWorkers())
                while not workersCopy.isEmpty():
                    worker = workersCopy.retrieve()
                    workersCopy.delete(None)
                self.__currentTick += 1
                i += 1
                continue
            if self.__inputReader.getCommands()[i] == str(self.__currentTick):
                i += 1
                continue
            if self.__inputReader.getCommands()[i] == "bestel":
                i += 1
                email = self.__inputReader.getCommands()[i]
                i += 1
                user = self.__store.getUser(email)
                user.createOrder(self.__store.getChocolateMilkCount())
                while (self.__inputReader.getCommands()[i] == "melk" or self.__inputReader.getCommands()[i] == "wit" or
                       self.__inputReader.getCommands()[i] == "zwart" or self.__inputReader.getCommands()[i] == "bruin" or
                       self.__inputReader.getCommands()[i] == "marshmallow" or self.__inputReader.getCommands()[i] == "chili" or
                       self.__inputReader.getCommands()[i] == "honey"):
                    if self.__inputReader.getCommands()[i] == "melk":
                        user.addMilkChocolateShot()
                    elif self.__inputReader.getCommands()[i] == "wit":
                        user.addWhiteChocolateShot()
                    elif self.__inputReader.getCommands()[i] == "zwart":
                        user.addDarkChocolateShot()
                    elif self.__inputReader.getCommands()[i] == "bruin":
                        user.addBrownChocolateShot()
                    elif self.__inputReader.getCommands()[i] == "marshmallow":
                        user.addMarshmallow()
                    elif self.__inputReader.getCommands()[i] == "chili":
                        user.addChilipepper()
                    elif self.__inputReader.getCommands()[i] == "honey":
                        user.addHoney()
                    i += 1
                year = self.__inputReader.getCommands()[i]
                i += 1
                month = self.__inputReader.getCommands()[i]
                i += 1
                day = self.__inputReader.getCommands()[i]
                i += 1
                hour = self.__inputReader.getCommands()[i]
                i += 1
                minute = self.__inputReader.getCommands()[i]
                i += 1
                user.getCurrentOrder().setTimeStamp(int(year+month+day+hour+minute))
                self.__store.cleanup(int(year+month+day))
                if self.__store.addChocolateMilk(user.getChocolateMilk()):
                    self.__store.addNewOrder(user.getCurrentOrder())
                    user.setChocolateMilk(None)
                    user.setCurrentOrder(None)
                else:
                    print(user.chocolateMilk.ingredients)
            if self.__inputReader.getCommands()[i] == "stock":
                i += 1
                if self.__inputReader.getCommands()[i] == "shot":
                    i += 1
                    type = self.__inputReader.getCommands()[i]
                    i += 1
                    amount = self.__inputReader.getCommands()[i]
                    i += 1
                    year = self.__inputReader.getCommands()[i]
                    i += 1
                    month = self.__inputReader.getCommands()[i]
                    i += 1
                    day = self.__inputReader.getCommands()[i]
                    i += 1
                    if type == "melk":
                        for j in range(0, int(amount)):
                            self.__store.restockMilkChocolateShot(int(year+month+day))
                        continue
                    elif type == "wit":
                        for j in range(0, int(amount)):
                            self.__store.restockWhiteChocolateShot(int(year+month+day))
                        continue
                    elif type == "zwart":
                        for j in range(0, int(amount)):
                            self.__store.restockDarkChocolateShot(int(year+month+day))
                        continue
                    elif type == "bruin":
                        for j in range(0, int(amount)):
                            self.__store.restockBrownChocolateShot(int(year+month+day))
                        continue
                    return False
                if self.__inputReader.getCommands()[i] == "honing":
                    i += 1
                    amount = self.__inputReader.getCommands()[i]
                    i += 1
                    year = self.__inputReader.getCommands()[i]
                    i += 1
                    month = self.__inputReader.getCommands()[i]
                    i += 1
                    day = self.__inputReader.getCommands()[i]
                    i += 1
                    for j in range(0, int(amount)):
                        self.__store.restockHoney(int(year+month+day))
                    continue
                if self.__inputReader.getCommands()[i] == "marshmallow":
                    i += 1
                    amount = self.__inputReader.getCommands()[i]
                    i += 1
                    year = self.__inputReader.getCommands()[i]
                    i += 1
                    month = self.__inputReader.getCommands()[i]
                    i += 1
                    day = self.__inputReader.getCommands()[i]
                    i += 1
                    for j in range(0, int(amount)):
                        self.__store.restockMarshmallow(int(year+month+day))
                    continue
                if self.__inputReader.getCommands()[i] == "chili":
                    i += 1
                    amount = self.__inputReader.getCommands()[i]
                    i += 1
                    year = self.__inputReader.getCommands()[i]
                    i += 1
                    month = self.__inputReader.getCommands()[i]
                    i += 1
                    day = self.__inputReader.getCommands()[i]
                    i += 1
                    for j in range(0, int(amount)):
                        self.__store.restockChilipepper(int(year+month+day))
                    continue
            if self.__inputReader.getCommands()[i] == "log":
                self.__logOut.addRow(self.__store, self.__currentTick)
                self.__logOut.writeHtml()
                return
        return


a = StoreSimulator()
a.simulate(a.initialise())
'''
b = ADTSimulator()
b.runADTSimulation()
'''
