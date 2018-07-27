from Store import Store, text_from_bits, text_to_bits
from LogOutput import LogOutput
from Wrapper import *
from InputReader import InputReader
from OutputGenerator import *
from Gebruiker import *
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
        self.logOut = LogOutput()
        self.inputReader = InputReader("system.txt")
        self.inputReader.StoreInputData()
        self.inputReader.InputFileToCommands()
        self.currentTick = 0

    def storeSimulation(self):
        print(self.inputReader.commands)
        i = 0
        while i != len(self.inputReader.commands):
            print(self.inputReader.commands[i])
            if self.inputReader.commands[i] == "init":
                i += 1
                self.store.createStore()
                continue

            if self.inputReader.commands[i] == "start":
                i += 1
                self.getToWork(i)
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
                        self.store.milkChocolateStock.insert(milkChoocolateItem.expirationDate, milkChoocolateItem)
                    continue
                elif type == "wit":
                    for j in range(0, int(amount)):
                        whiteChoocolateItem = ChocolateShot(int(year+month+day), ChocolateShotType.white)
                        self.store.whiteChocolateStock.insert(whiteChoocolateItem.expirationDate, whiteChoocolateItem)
                    continue
                elif type == "zwart":
                    for j in range(0, int(amount)):
                        darkChoocolateItem = ChocolateShot(int(year+month+day), ChocolateShotType.dark)
                        self.store.darkChocolateStock.insert(darkChoocolateItem.expirationDate, darkChoocolateItem)
                    continue
                elif type == "bruin":
                    for j in range(0, int(amount)):
                        brownChoocolateItem = ChocolateShot(int(year+month+day), ChocolateShotType.brown)
                        self.store.brownChocolateStock.insert(brownChoocolateItem.expirationDate, brownChoocolateItem)
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
                    self.store.honeyStock.insert(honeyItem.expirationDate, honeyItem)
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
                    self.store.marshmallowStock.insert(marshmallowItem.expirationDate, marshmallowItem)
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
                    chiliItem = Chilipepper(int(year + month + day))
                    self.store.chiliStock.insert(chiliItem.expirationDate, chiliItem)
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
                self.store.users.insert(text_to_bits(userItem.email), userItem)
                continue
            if self.inputReader.commands[i] == "werknemer":
                i += 1
                firstName = self.inputReader.commands[i]
                i += 1
                lastName = self.inputReader.commands[i]
                i += 1
                workLoad = self.inputReader.commands[i]
                i += 1
                workerItem = Worker(firstName, lastName, int(workLoad))
                self.store.addWorker(workerItem)
                continue
        return

    def getToWork(self, i):
        while i != len(self.inputReader.commands):
            print("currentTick = ", self.currentTick)
            if self.inputReader.commands[i] == str(self.currentTick + 1):
                self.logOut.addRow(self.store, self.currentTick)
                self.currentTick += 1
                i += 1
                continue
            if self.inputReader.commands[i] == str(self.currentTick):
                i += 1
                continue
            if self.inputReader.commands[i] == "bestel":
                i += 1
                email = self.inputReader.commands[i]
                i += 1
                user = self.store.users.retrieve(text_to_bits(email))
                user.createOrder(self.store.chocolateMilkCount)
                self.store.chocolateMilkCount += 1
                while (self.inputReader.commands[i] == "melk" or self.inputReader.commands[i] == "wit" or
                       self.inputReader.commands[i] == "zwart" or self.inputReader.commands[i] == "bruin" or
                       self.inputReader.commands[i] == "marshmallow" or self.inputReader.commands[i] == "chili" or
                       self.inputReader.commands[i] == "honey"):
                    if self.inputReader.commands[i] == "melk":
                        user.addChocolateShot(ChocolateShotType.milk)
                    elif self.inputReader.commands[i] == "wit":
                        user.addChocolateShot(ChocolateShotType.wit)
                    elif self.inputReader.commands[i] == "zwart":
                        user.addChocolateShot(ChocolateShotType.dark)
                    elif self.inputReader.commands[i] == "bruin":
                        user.addChocolateShot(ChocolateShotType.brown)
                    elif self.inputReader.commands[i] == "marshmallow":
                        user.addMarshmallow()
                    elif self.inputReader.commands[i] == "chili":
                        user.addChilipepper()
                    elif self.inputReader.commands[i] == "honey":
                        user.addHoney()
                    i += 1
                year = self.inputReader.commands[i]
                i += 1
                month = self.inputReader.commands[i]
                i += 1
                day = self.inputReader.commands[i]
                i += 1
                hour = self.inputReader.commands[i]
                i += 1
                minute = self.inputReader.commands[i]
                i += 1
                user.currentOrder.setTimeStamp(int(year+month+day+hour+minute))
                self.store.cleanup(int(year+month+day))
                if self.store.makeChocolateMilk(user.chocolateMilk):
                    self.store.newOrders.insert(user.currentOrder.searchkey, user.currentOrder)

                    user.chocolateMilk = None
                    user.currentOrder = None
                else:
                    print(user.chocolateMilk.ingredients)
                    print("too little items in stock")
            if self.inputReader.commands[i] == "stock":
                i += 1
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
                            milkChoocolateItem = ChocolateShot(int(year + month + day), ChocolateShotType.milk)
                            self.store.milkChocolateStock.insert(milkChoocolateItem.expirationDate, milkChoocolateItem)
                        continue
                    elif type == "wit":
                        for j in range(0, int(amount)):
                            whiteChoocolateItem = ChocolateShot(int(year + month + day), ChocolateShotType.white)
                            self.store.whiteChocolateStock.insert(whiteChoocolateItem.expirationDate,
                                                                  whiteChoocolateItem)
                        continue
                    elif type == "zwart":
                        for j in range(0, int(amount)):
                            darkChoocolateItem = ChocolateShot(int(year + month + day), ChocolateShotType.dark)
                            self.store.darkChocolateStock.insert(darkChoocolateItem.expirationDate, darkChoocolateItem)
                        continue
                    elif type == "bruin":
                        for j in range(0, int(amount)):
                            brownChoocolateItem = ChocolateShot(int(year + month + day), ChocolateShotType.brown)
                            self.store.brownChocolateStock.insert(brownChoocolateItem.expirationDate,
                                                                  brownChoocolateItem)
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
                        self.store.honeyStock.insert(honeyItem.expirationDate, honeyItem)
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
                        self.store.marshmallowStock.insert(marshmallowItem.expirationDate, marshmallowItem)
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
                        self.store.chiliStock.insert(chiliItem.expirationDate, chiliItem)
                    continue
            if self.inputReader.commands[i] == "log":
                self.logOut.addRow(self.store, self.currentTick)
                self.logOut.writeHtml()
                return
        return

'''
a = ADTSimulator()
a.runADTSimulation()
'''
a = StoreSimulator()
a.storeSimulation()
'''
printDLC(a.store.milkChocolateStock.ADT)
printDLC(a.store.darkChocolateStock.ADT)
printDLC(a.store.brownChocolateStock.ADT)
printDLC(a.store.whiteChocolateStock.ADT)
printDLC(a.store.honeyStock.ADT)
printDLC(a.store.marshmallowStock.ADT)
printDLC(a.store.workers.ADT)
'''