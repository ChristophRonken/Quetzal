from Wrappers.BSTWrapper import BSTWrapper
from Wrappers.CLCWrapper import CLCWrapper
from Wrappers.DLCWrapper import DLCWrapper
from Wrappers.HashWrapper import HLinWrapper, HQuadWrapper, HSepWrapper
from Wrappers.QueueWrapper import QueueWrapper
from Wrappers.StackWrapper import StackWrapper
from Worker import Worker
from User import User
from Enums import ChocolateShotType
from Ingredient import ChocolateShot, Honey, Marshmallow, Chilipepper
from bits import text_to_bits
from OutputGenerator import *

import copy


class Store:

    def __init__(self):

        self.__chocolateMilkCount = 0
        self.__userCount = 0
        self.__workerCount = 0
        self.__money = 2000
        self.__currentTime = 0

        # stack or queue
        self.__marshmallowStock = StackWrapper()
        self.__milkChocolateStock = StackWrapper()
        self.__darkChocolateStock = StackWrapper()
        self.__whiteChocolateStock = StackWrapper()
        self.__brownChocolateStock = StackWrapper()
        self.__honeyStock = StackWrapper()
        self.__chilipepperStock = StackWrapper()

        # BST, DLC, Hlin, HQuad, Hsep
        self.__users = HSepWrapper()

        # Stack (works with queue as well)
        self.__workload = StackWrapper()

        # Queue:
        self.__chocolateMilkToBeMade = QueueWrapper()
        self.__newOrders = QueueWrapper()
        self.__waitingOrders = QueueWrapper()

        self.__finishedChocolateMilks = QueueWrapper()
        self.__workers = QueueWrapper()
        self.__finishedOrders = QueueWrapper()

        self.__allOrders = BSTWrapper()

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

    def getMoney(self):
        return round(self.__money, 2)

    def getWorkerCount(self):
        return self.__workerCount

    def getTime(self):
        return self.__currentTime

    def getUser(self, searchkey):
        return self.__users.retrieve(int(text_to_bits(searchkey)))

    def restockMarshmallow(self, expirationDate):
        marshmallowItem = Marshmallow(expirationDate)
        self.__money -= marshmallowItem.buyPrice
        return self.__marshmallowStock.insert(marshmallowItem.searchkey, marshmallowItem)

    def restockHoney(self, expirationDate):
        honeyItem = Honey(expirationDate)
        self.__money -= honeyItem.buyPrice
        return self.__honeyStock.insert(honeyItem.searchkey, honeyItem)

    def restockChilipepper(self, expirationDate):
        chilipepperItem = Chilipepper(expirationDate)
        self.__money -= chilipepperItem.buyPrice
        return self.__chilipepperStock.insert(chilipepperItem.searchkey, chilipepperItem)

    def restockMilkChocolateShot(self, expirationDate):
        chocolateType = ChocolateShotType.milk
        milkChocolateShotItem = ChocolateShot(expirationDate, chocolateType)
        self.__money -= milkChocolateShotItem.buyPrice
        return self.__milkChocolateStock.insert(milkChocolateShotItem.searchkey, milkChocolateShotItem)

    def restockBrownChocolateShot(self, expirationDate):
        chocolateType = ChocolateShotType.brown
        brownChocolateShotItem = ChocolateShot(expirationDate, chocolateType)
        self.__money -= brownChocolateShotItem.buyPrice
        return self.__brownChocolateStock.insert(brownChocolateShotItem.searchkey, brownChocolateShotItem)

    def restockDarkChocolateShot(self, expirationDate):
        chocolateType = ChocolateShotType.dark
        darkChocolateShotItem = ChocolateShot(expirationDate, chocolateType)
        self.__money -= darkChocolateShotItem.buyPrice
        return self.__darkChocolateStock.insert(darkChocolateShotItem.searchkey, darkChocolateShotItem)

    def restockWhiteChocolateShot(self, expirationDate):
        chocolateType = ChocolateShotType.white
        whiteChocolateShotItem = ChocolateShot(expirationDate, chocolateType)
        self.__money -= whiteChocolateShotItem.buyPrice
        return self.__whiteChocolateStock.insert(whiteChocolateShotItem.searchkey, whiteChocolateShotItem)

    def addWorker(self, firstName, lastName, workLoad):
        worker = Worker(firstName, lastName, workLoad, self.__workerCount)
        if self.__workers.insert(worker.searchkey, worker):
            for i in range(0, worker.getWorkload()):
                self.addWorkload()
            self.__userCount += 1
            return True
        return False

    def addUser(self, firstName, lastName, email):
        user = User(firstName, lastName, int(text_to_bits(email)), self.__userCount)
        self.__userCount += 1
        return self.__users.insert(user.searchkey, user)

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

    def tick(self):
        self.__currentTime += 1
        return True

    def work(self):
        workersCopy = copy.deepcopy(self.__workers)
        while not workersCopy.isEmpty():
            worker = workersCopy.retrieve(None)
            if not worker.getIsBusy():
                order = None
                if not self.__waitingOrders.isEmpty():
                    order = self.__waitingOrders.retrieve(None)
                    self.__waitingOrders.delete(None)
                elif not self.__newOrders.isEmpty():
                    order = self.__newOrders.retrieve(None)
                    self.__newOrders.delete(None)
                else:
                    pass
                if order is not None:
                    worker.setChocolateMilk(self.__chocolateMilkToBeMade.retrieve(None))
                    self.__chocolateMilkToBeMade.delete(None)
                    worker.setBusyTime(worker.getChocolateMilk().getCredit())
                    worker.setIsBusy(True)
                    worker.setOrder(order)
            if worker.getIsBusy():
                print("busytime: ", worker.getBusyTime())
                worker.setBusyTime(worker.getBusyTime() - worker.getWorkload())
                print("maybefinished: ", worker.getBusyTime())
                if worker.getBusyTime() <= 0:
                    worker.getOrder().setFinishedTime(self.__currentTime)
                    self.__finishedOrders.insert(worker.getOrder().searchkey, worker.getOrder())
                    self.__finishedChocolateMilks.insert(worker.getChocolateMilk().searchkey, worker.getChocolateMilk())
                    self.__money += worker.getChocolateMilk().getPrice()
                    worker.setBusyTime(0)
                    worker.setOrder(None)
                    worker.setIsBusy(False)
                    worker.setChocolateMilk(None)
            workersCopy.delete(None)
            self.__workers.delete(None)
            self.__workers.insert(None, worker)
            if not workersCopy.isEmpty():
                worker = workersCopy.retrieve(None)

        while not self.__newOrders.isEmpty():
            order = self.__newOrders.retrieve(None)
            self.__newOrders.delete(None)
            self.__waitingOrders.insert(order.searchkey, order)

    def cleanup(self, time):
        stocklist = [self.__marshmallowStock, self.__milkChocolateStock, self.__whiteChocolateStock,
                     self.__darkChocolateStock, self.__brownChocolateStock, self.__honeyStock, self.__chilipepperStock]
        for i in range(0, len(stocklist)):
            if stocklist[i].isEmpty():
                continue
            stockCopy = copy.deepcopy(stocklist[i])
            newStock = StackWrapper()
            newStock.create()
            while not stockCopy.isEmpty():
                if not stockCopy.retrieve(None).getExpirationDate() < time:
                    newStock.insert(stockCopy.retrieve(None).searchkey, stockCopy.retrieve(None))
                stockCopy.delete(None)
            while not stocklist[i].isEmpty():
                stocklist[i].delete(None)
            while not newStock.isEmpty():
                stocklist[i].insert(newStock.retrieve(None).searchkey, newStock.retrieve(None))
                newStock.delete(None)
        return True

    def addChocolateMilk(self, chocolateMilk, order, time):
        sufficientStock = True
        ingredientList = []
        for i in range(0, len(chocolateMilk.getIngredients())):
            self.cleanup(time)
            if isinstance(chocolateMilk.getIngredients()[i], ChocolateShot):
                if chocolateMilk.getIngredients()[i].getType() == ChocolateShotType.white:
                    if self.__whiteChocolateStock.isEmpty():
                        sufficientStock = False
                        continue
                    ingredientList.append(self.__whiteChocolateStock.retrieve(None))
                    self.__whiteChocolateStock.delete(self.__whiteChocolateStock.retrieve(None).searchkey)
                if chocolateMilk.getIngredients()[i].getType() == ChocolateShotType.dark:
                    if self.__darkChocolateStock.isEmpty():
                        sufficientStock = False
                        continue
                    ingredientList.append(self.__darkChocolateStock.retrieve(None))
                    self.__darkChocolateStock.delete(self.__darkChocolateStock.retrieve(None).searchkey)
                if chocolateMilk.getIngredients()[i].getType() == ChocolateShotType.brown:
                    if self.__brownChocolateStock.isEmpty():
                        sufficientStock = False
                        continue
                    ingredientList.append(self.__brownChocolateStock.retrieve(None))
                    self.__brownChocolateStock.delete(self.__brownChocolateStock.retrieve(None).searchkey)
                if chocolateMilk.getIngredients()[i].getType() == ChocolateShotType.milk:
                    if self.__milkChocolateStock.isEmpty():
                        sufficientStock = False
                        continue
                    ingredientList.append(self.__milkChocolateStock.retrieve(None))
                    self.__milkChocolateStock.delete(self.__milkChocolateStock.retrieve(None).searchkey)
            if isinstance(chocolateMilk.getIngredients()[i], Honey):
                if self.__honeyStock.isEmpty():
                    sufficientStock = False
                    continue
                ingredientList.append(self.__honeyStock.retrieve(None))
                self.__honeyStock.delete(self.__honeyStock.retrieve(None).searchkey)
            if isinstance(chocolateMilk.getIngredients()[i], Chilipepper):
                if self.__chilipepperStock.isEmpty():
                    sufficientStock = False
                    continue
                ingredientList.append(self.__chilipepperStock.retrieve(None))
                self.__chilipepperStock.delete(self.__chilipepperStock.retrieve(None).searchkey)
            if isinstance(chocolateMilk.getIngredients()[i], Marshmallow):
                if self.__marshmallowStock.isEmpty():
                    sufficientStock = False
                    continue
                ingredientList.append(self.__marshmallowStock.retrieve(None))
                self.__marshmallowStock.delete(self.__marshmallowStock.retrieve(None).searchkey)
        if sufficientStock:
            self.__newOrders.insert(order.searchkey, order)
            self.__chocolateMilkToBeMade.insert(chocolateMilk.searchkey, chocolateMilk)
            self.__chocolateMilkCount += 1
            print("toegevoegd")
            return True
        else:
            for i in range(0, len(ingredientList)):
                if isinstance(ingredientList[i], ChocolateShot):
                    if ingredientList[i].getType() == ChocolateShotType.white:
                        self.__whiteChocolateStock.insert(ingredientList[i].searchkey, ingredientList[i])
                    if ingredientList[i].getType() == ChocolateShotType.dark:
                        self.__darkChocolateStock.insert(ingredientList[i].searchkey, ingredientList[i])
                    if ingredientList[i].getType() == ChocolateShotType.brown:
                        self.__brownChocolateStock.insert(ingredientList[i].searchkey, ingredientList[i])
                    if ingredientList[i].getType() == ChocolateShotType.milk:
                        self.__milkChocolateStock.insert(ingredientList[i].searchkey, ingredientList[i])
                if isinstance(ingredientList[i], Honey):
                    self.__honeyStock.insert(ingredientList[i].searchkey, ingredientList[i])
                if isinstance(ingredientList[i], Chilipepper):
                    self.__chilipepperStock.insert(ingredientList[i].searchkey, ingredientList[i])
                if isinstance(ingredientList[i], Marshmallow):
                    self.__marshmallowStock.insert(ingredientList[i].searchkey, ingredientList[i])
            return False




