from Wrapper import *
from Ingredient import *
from Worker import *
from User import *
import binascii
import copy


class Store:

    def __init__(self):
        self.__marshmallowStock = DLCWrapper()
        self.__milkChocolateStock = DLCWrapper()
        self.__darkChocolateStock = DLCWrapper()
        self.__whiteChocolateStock = DLCWrapper()
        self.__brownChocolateStock = DLCWrapper()
        self.__honeyStock = DLCWrapper()
        self.__chilipepperStock = DLCWrapper()

        self.__users = DLCWrapper()
        self.__workers = QueueWrapper()
        self.__workload = StackWrapper()

        self.__chocolateMilkCount = 0
        self.__userCount = 0
        self.__workerCount = 0

        self.__chocolateMilkToBeMade = DLCWrapper()
        self.__finishedChocolateMilks = DLCWrapper()
        self.__newOrders = QueueWrapper()
        self.__waitingOrders = QueueWrapper()
        self.__finishedOrders = DLCWrapper()

        self.__money = 0

    def createStore(self):
        self.__marshmallowStock.create()
        self.__milkChocolateStock.create()
        self.__darkChocolateStock.create()
        self.__whiteChocolateStock.create()
        self.__brownChocolateStock.create()
        self.__honeyStock.create()
        self.__chilipepperStock.create()

        self.__users.create()
        self.__workers.create()
        self.__workload.create()

        self.__chocolateMilkToBeMade.create()
        self.__finishedChocolateMilks.create()
        self.__newOrders.create()
        self.__waitingOrders.create()
        self.__finishedOrders.create()
        return True

    def getMarshmallowStock(self):
        return self.__marshmallowStock

    def getHoneyStock(self):
        return self.__honeyStock

    def getChilipepperStock(self):
        return self.__chilipepperStock

    def getWhiteChocolateStock(self):
        return self.__whiteChocolateStock

    def getBrownChocolateStock(self):
        return self.__brownChocolateStock

    def getDarkChocolateStock(self):
        return self.__darkChocolateStock

    def getMilkChocolateStock(self):
        return self.__milkChocolateStock

    def getUsers(self):
        return self.__users

    def getWorkers(self):
        return self.__workers

    def getWorkload(self):
        return self.__workload

    def getUserCount(self):
        return self.__userCount

    def getChocolateMilkCount(self):
        return self.__chocolateMilkCount

    def getChocolateMilkToBeMade(self):
        return self.__chocolateMilkToBeMade

    def getFinishedChocolateMilks(self):
        return self.__finishedChocolateMilks

    def getNewOrders(self):
        return self.__newOrders

    def getWaitingOrders(self):
        return self.__waitingOrders

    def getFinishedOrders(self):
        return self.__finishedOrders

    def restockMarshmallow(self, expirationDate):
        marshmallowItem = Honey(expirationDate)
        return self.__marshmallowStock.insert(marshmallowItem.searchkey, marshmallowItem)

    def restockHoney(self, expirationDate):
        honeyItem = Honey(expirationDate)
        return self.__honeyStock.insert(honeyItem.searchkey, honeyItem)

    def restockChilipepper(self, expirationDate):
        chilipepperItem = Chilipepper(expirationDate)
        return self.__chilipepperStock.insert(chilipepperItem.searchkey, chilipepperItem)

    def restockMilkChocolateShot(self, expirationDate):
        chocolateType = ChocolateShotType.milk
        milkChocolateShotItem = ChocolateShot(expirationDate, chocolateType)
        return self.__milkChocolateStock.insert(milkChocolateShotItem.searchkey, milkChocolateShotItem)

    def restockBrownChocolateShot(self, expirationDate):
        chocolateType = ChocolateShotType.brown
        brownChocolateShotItem = ChocolateShot(expirationDate, chocolateType)
        return self.__brownChocolateStock.insert(brownChocolateShotItem.searchkey, brownChocolateShotItem)

    def restockDarkChocolateShot(self, expirationDate):
        chocolateType = ChocolateShotType.dark
        darkChocolateShotItem = ChocolateShot(expirationDate, chocolateType)
        return self.__darkChocolateStock.insert(darkChocolateShotItem.searchkey, darkChocolateShotItem)

    def restockWhiteChocolateShot(self, expirationDate):
        chocolateType = ChocolateShotType.white
        whiteChocolateShotItem = ChocolateShot(expirationDate, chocolateType)
        return self.__whiteChocolateStock.insert(whiteChocolateShotItem.searchkey, whiteChocolateShotItem)

    def addWorker(self, firstName, lastName, workLoad):
        worker = Worker(firstName, lastName, workLoad, self.__workerCount)
        if self.__workers.insert(worker.searchkey, worker):
            for i in range(0, worker.getWorkLoad()):
                self.addWorkload()
            self.__userCount += 1
            return True
        return False

    def addUser(self, firstName, lastName, email):
        user = User(firstName, lastName, text_to_bits(email), self.__userCount)
        self.__userCount += 1
        return self.__users.insert(user.searchkey, user)

    def getUser(self, searchkey):
        return self.__users.retrieve(text_to_bits(searchkey))

    def addWorkload(self):
        return self.__workload.insert(None, "credit")

    def addChocolateMilkToBeMade(self, chocolatemilk):
        return self.__chocolateMilkToBeMade.insert(chocolatemilk.searchkey, chocolatemilk)

    def addFinishedChocolateMilks(self, finishedChocolateMilk):
        return self.__finishedChocolateMilks.insert(finishedChocolateMilk.searchkey, finishedChocolateMilk)

    def addNewOrder(self, order):
        return self.__newOrders.insert(order.searchkey, order)

    def addWaitingOrder(self, order):
        return self.__waitingOrders.insert(order.searchkey, order)

    def addFinishedOrder(self, order):
        return self.__finishedOrders.insert(order.searchkey, order)

    def work(self):
        workersCopy = copy.deepcopy(self.__workers)
        while not workersCopy.isEmpty():
            worker = workersCopy.retrieve()
            if not worker.getIsBusy():
                order = None
                if not self.__waitingOrders.isEmpty():
                    order = self.__waitingOrders.retrieve()
                    self.__waitingOrders.delete(None)
                elif not self.__newOrders.isEmpty():
                    order = self.__newOrders.retrieve()
                    self.__newOrders.delete(None)
                else:
                    pass
                if order is not None:
                    worker.setChocolateMilk(self.__chocolateMilkToBeMade.retrieve())
                    worker.setBusyTime(worker.getChocolateMilk().getCredit())
                    worker.setIsBusy(True)
                    worker.setOrder(order)
            if worker.getIsBusy():
                print("busytime: ", worker.getBusyTime())
                worker.setBusyTime(worker.getBusyTime() - worker.getWorkLoad())
                print("maybefinished: ", worker.getBusyTime())
                if worker.getBusyTime() <= 0:
                    self.__finishedOrders.insert(worker.getOrder().searchkey, worker.getOrder())
                    worker.setBusyTime(0)
                    worker.setOrder(None)
                    worker.setIsBusy(False)
                    worker.setChocolateMilk(None)
            workersCopy.delete(None)
            self.__workers.delete(None)
            self.__workers.insert(None, worker)
            if not workersCopy.isEmpty():
                worker = workersCopy.retrieve()

        while not self.__newOrders.isEmpty():
            order = self.__newOrders.retrieve()
            self.__newOrders.delete(None)
            self.__waitingOrders.insert(order.searchkey, order)

    def cleanup(self, time):
        stocklist = [self.__marshmallowStock, self.__milkChocolateStock, self.__whiteChocolateStock, self.__darkChocolateStock,
                     self.__brownChocolateStock, self.__honeyStock, self.__chilipepperStock]
        for i in range(0, len(stocklist)):
            if stocklist[i].isEmpty():
                continue
            while stocklist[i].retrieve().expirationDate < time:
                stocklist[i].delete(stocklist[i].retrieve().searchkey)
                if stocklist[i].isEmpty():
                    continue
        return True

    def addChocolateMilk(self, chocolateMilk):
        sufficientStock = True
        ingredientList = []
        for i in range(0, len(chocolateMilk.getIngredients())):
            if isinstance(chocolateMilk.getIngredients()[i], ChocolateShot):
                if chocolateMilk.getIngredients()[i].type == ChocolateShotType.white:
                    if self.__whiteChocolateStock.isEmpty():
                        sufficientStock = False
                        continue
                    ingredientList.append(self.__whiteChocolateStock.retrieve())
                    self.__whiteChocolateStock.delete(self.__whiteChocolateStock.retrieve().searchkey)
                if chocolateMilk.getIngredients()[i].type == ChocolateShotType.dark:
                    if self.__darkChocolateStock.isEmpty():
                        sufficientStock = False
                        continue
                    ingredientList.append(self.__darkChocolateStock.retrieve())
                    self.__darkChocolateStock.delete(self.__darkChocolateStock.retrieve().searchkey)
                if chocolateMilk.getIngredients()[i].type == ChocolateShotType.brown:
                    if self.__brownChocolateStock.isEmpty():
                        sufficientStock = False
                        continue
                    ingredientList.append(self.__brownChocolateStock.retrieve())
                    self.__brownChocolateStock.delete(self.__brownChocolateStock.retrieve().searchkey)
                if chocolateMilk.getIngredients()[i].type == ChocolateShotType.milk:
                    if self.__milkChocolateStock.isEmpty():
                        sufficientStock = False
                        continue
                    ingredientList.append(self.__milkChocolateStock.retrieve())
                    self.__milkChocolateStock.delete(self.__milkChocolateStock.retrieve().searchkey)
            if isinstance(chocolateMilk.getIngredients()[i], Honey):
                if self.__honeyStock.isEmpty():
                    sufficientStock = False
                    continue
                ingredientList.append(self.__honeyStock.retrieve())
                self.__honeyStock.delete(self.__honeyStock.retrieve().searchkey)
            if isinstance(chocolateMilk.getIngredients()[i], Chilipepper):
                if self.__chilipepperStock.isEmpty():
                    sufficientStock = False
                    continue
                ingredientList.append(self.__chilipepperStock.retrieve())
                self.__chilipepperStock.delete(self.__chilipepperStock.retrieve().searchkey)
            if isinstance(chocolateMilk.getIngredients()[i], Marshmallow):
                if self.__marshmallowStock.isEmpty():
                    sufficientStock = False
                    continue
                ingredientList.append(self.__marshmallowStock.retrieve())
                self.__marshmallowStock.delete(self.__marshmallowStock.retrieve().searchkey)
        if sufficientStock:
            self.__chocolateMilkToBeMade.insert(chocolateMilk.searchkey, chocolateMilk)
            self.__chocolateMilkCount += 1
            return True
        else:
            for i in range(0, len(ingredientList)):
                if isinstance(ingredientList[i], ChocolateShot):
                    if ingredientList[i].type == ChocolateShotType.white:
                        self.__whiteChocolateStock.insert(ingredientList[i].searchkey, ingredientList[i])
                    if ingredientList[i].type == ChocolateShotType.dark:
                        self.__darkChocolateStock.insert(ingredientList[i].searchkey, ingredientList[i])
                    if ingredientList[i].type == ChocolateShotType.brown:
                        self.__brownChocolateStock.insert(ingredientList[i].searchkey, ingredientList[i])
                    if ingredientList[i].type == ChocolateShotType.milk:
                        self.__milkChocolateStock.insert(ingredientList[i].searchkey, ingredientList[i])
                if isinstance(ingredientList[i], Honey):
                    self.__honeyStock.insert(ingredientList[i].searchkey, ingredientList[i])
                if isinstance(ingredientList[i], Chilipepper):
                    self.__chilipepperStock.insert(ingredientList[i].searchkey, ingredientList[i])
                if isinstance(ingredientList[i], Marshmallow):
                    self.__marshmallowStock.insert(ingredientList[i].searchkey, ingredientList[i])
            return False


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    # This function was found online:
    # https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    # This function was found online:
    # https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)


def int2bytes(i):
    # This function was found online:
    # https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

