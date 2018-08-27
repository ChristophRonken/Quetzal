from Wrappers.BSTWrapper import BSTWrapper
from Wrappers.CLCWrapper import CLCWrapper
from Wrappers.DLCWrapper import DLCWrapper
from Wrappers.HashWrapper import HLinWrapper, HQuadWrapper, HSepWrapper
from Wrappers.QueueWrapper import QueueWrapper
from Wrappers.StackWrapper import StackWrapper
from Worker import Worker
from User import User
from Enums import ChocolateShotType, OrderStates
from Ingredient import ChocolateShot, Honey, Marshmallow, Chilipepper
from bits import text_to_bits
from Order import *

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
        self.__users = BSTWrapper()
        self.__allOrders = HLinWrapper()

        # Stack (works with queue as well)
        self.__workload = StackWrapper()

        # Queue:
        self.__chocolateMilkToBeMade = QueueWrapper()
        self.__newOrders = QueueWrapper()
        self.__waitingOrders = QueueWrapper()
        self.__workers = QueueWrapper()

        self.__makeTimes = QueueWrapper()
        self.__allTimes = QueueWrapper()

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
        self.__newOrders.create()
        self.__waitingOrders.create()

        self.__allOrders.create()
        self.__makeTimes.create()
        self.__allTimes.create()
        return True

    def getAllTimes(self):
        return self.__allTimes

    def getAllOrders(self):
        return self.__allOrders

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

    def getNewOrders(self):
        return self.__newOrders

    def getWaitingOrders(self):
        return self.__waitingOrders

    def getMoney(self):
        return round(self.__money, 2)

    def getWorkerCount(self):
        return self.__workerCount

    def getTime(self):
        return self.__currentTime

    def getUser(self, searchkey):
        return self.__users.retrieve(int(text_to_bits(searchkey)))

    def restockMarshmallow(self, expirationDate):
        if not isinstance(expirationDate, int):
            return False
        marshmallowItem = Marshmallow(expirationDate)
        self.__money -= marshmallowItem.buyPrice
        return self.__marshmallowStock.insert(marshmallowItem.searchkey, marshmallowItem)

    def restockHoney(self, expirationDate):
        if not isinstance(expirationDate, int):
            return False
        honeyItem = Honey(expirationDate)
        self.__money -= honeyItem.buyPrice
        return self.__honeyStock.insert(honeyItem.searchkey, honeyItem)

    def restockChilipepper(self, expirationDate):
        if not isinstance(expirationDate, int):
            return False
        chilipepperItem = Chilipepper(expirationDate)
        self.__money -= chilipepperItem.buyPrice
        return self.__chilipepperStock.insert(chilipepperItem.searchkey, chilipepperItem)

    def restockMilkChocolateShot(self, expirationDate):
        if not isinstance(expirationDate, int):
            return False
        chocolateType = ChocolateShotType.milk
        milkChocolateShotItem = ChocolateShot(expirationDate, chocolateType)
        self.__money -= milkChocolateShotItem.buyPrice
        return self.__milkChocolateStock.insert(milkChocolateShotItem.searchkey, milkChocolateShotItem)

    def restockBrownChocolateShot(self, expirationDate):
        if not isinstance(expirationDate, int):
            return False
        chocolateType = ChocolateShotType.brown
        brownChocolateShotItem = ChocolateShot(expirationDate, chocolateType)
        self.__money -= brownChocolateShotItem.buyPrice
        return self.__brownChocolateStock.insert(brownChocolateShotItem.searchkey, brownChocolateShotItem)

    def restockDarkChocolateShot(self, expirationDate):
        if not isinstance(expirationDate, int):
            return False
        chocolateType = ChocolateShotType.dark
        darkChocolateShotItem = ChocolateShot(expirationDate, chocolateType)
        self.__money -= darkChocolateShotItem.buyPrice
        return self.__darkChocolateStock.insert(darkChocolateShotItem.searchkey, darkChocolateShotItem)

    def restockWhiteChocolateShot(self, expirationDate):
        if not isinstance(expirationDate, int):
            return False
        chocolateType = ChocolateShotType.white
        whiteChocolateShotItem = ChocolateShot(expirationDate, chocolateType)
        self.__money -= whiteChocolateShotItem.buyPrice
        return self.__whiteChocolateStock.insert(whiteChocolateShotItem.searchkey, whiteChocolateShotItem)

    def addWorker(self, firstName, lastName, workLoad):
        if not (isinstance(firstName, str) and isinstance(lastName, str) and isinstance(workLoad, int)):
            return False
        worker = Worker(firstName, lastName, workLoad, self.__workerCount)
        if self.__workers.insert(worker.searchkey, worker):
            for i in range(0, worker.getWorkload()):
                self.addWorkload()
            self.__userCount += 1
            return True
        return False

    def addUser(self, firstName, lastName, email):
        if not (isinstance(firstName, str) and isinstance(lastName, str) and isinstance(email, str)):
            return False
        user = User(firstName, lastName, email, self.__userCount)
        self.__userCount += 1
        return self.__users.insert(user.searchkey, user)

    def addWorkload(self):
        return self.__workload.insert(None, "credit")

    def addChocolateMilkToBeMade(self, chocolatemilk):
        if not isinstance(chocolatemilk, ChocolateMilk):
            return False
        return self.__chocolateMilkToBeMade.insert(chocolatemilk.searchkey, chocolatemilk)

    def addNewOrder(self, order):
        if not isinstance(order, Order):
            return False
        return self.__newOrders.insert(order.searchkey, order)

    def addWaitingOrder(self, order):
        if not isinstance(order, Order):
            return False
        return self.__waitingOrders.insert(order.searchkey, order)

    def tick(self):
        self.__currentTime += 1
        return

    def work(self):
        self.newToWaiting()
        print("start work")
        workersCopy = copy.deepcopy(self.__workers)

        # while there are workers which haven't been checked:
        while not workersCopy.isEmpty():
            worker = workersCopy.retrieve(None)
            # if the worker is not busy and there is a time in maketimes:
            if not worker.getIsBusy() and not self.__makeTimes.isEmpty():
                # time is the first time in the queue
                # order is the first order at that time, this order is deleted from allOrders
                # order state is set to beingmade and the order is added back to allOrders
                # worker takes first chocolatemilk from queue and this gets deleted
                # worker's busytime and order is set
                time = self.__makeTimes.retrieve(None)
                order = self.__allOrders.retrieve(time).retrieve(None)
                self.__allOrders.retrieve(time).delete(None)
                order.setState(OrderStates.BeingMade)
                self.__allOrders.retrieve(time).insert(None, order)
                worker.setChocolateMilk(self.__chocolateMilkToBeMade.retrieve(None))
                self.__chocolateMilkToBeMade.delete(None)
                worker.setBusyTime(worker.getChocolateMilk().getCredit())
                worker.setIsBusy(True)
                worker.setOrder(order)

                # if the first order in the orderqueue is being made then that time has no more orders
                if self.__allOrders.retrieve(time).retrieve(None).getState() == OrderStates.BeingMade:
                    self.__makeTimes.delete(None)

            # if the worker appears to be busy, the busytime decreases
            # if the worker finishes his order, the finishedtime is set for the order
            # while there are orders for the order searchkey, if the order searchkeys match state is set to finished
            # newqueue becomes a orderqueue with one order set to finished
            # allorders gets updated with newqueue
            # worker's busytime and order is unset
            # next worker is selected

            if worker.getIsBusy():
                worker.setBusyTime(worker.getBusyTime() - worker.getWorkload())
                if worker.getBusyTime() <= 0:
                    worker.getOrder().setFinishedTime(self.__currentTime)
                    newQueue = QueueWrapper()
                    newQueue.create()
                    while not self.__allOrders.retrieve(worker.getOrder().getTimeStamp()).isEmpty():
                        order = self.__allOrders.retrieve(worker.getOrder().getTimeStamp()).retrieve(None)
                        if order.searchkey == worker.getOrder().searchkey:
                            order.setState(OrderStates.Finished)
                        self.__allOrders.retrieve(worker.getOrder().getTimeStamp()).delete(None)
                        newQueue.insert(None, order)
                    self.__allOrders.delete(worker.getOrder().getTimeStamp())
                    self.__allOrders.insert(worker.getOrder().getTimeStamp(), newQueue)

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

        print("end work")
        return

    def newToWaiting(self):
        if self.__allTimes.isEmpty():
            return
        else:
            alltimesCopy = copy.deepcopy(self.__allTimes)
            while not alltimesCopy.isEmpty():
                time = alltimesCopy.retrieve(None)
                orderQueue = QueueWrapper()
                orderQueue.create()
                # while the orderqueue with a time from alltimes is not empty:
                while not self.__allOrders.retrieve(time).isEmpty():
                    # if the order state is new, then it gets set to waiting
                    # this order is added to a new queue which later replaces the original orderqueue
                    order = self.__allOrders.retrieve(time).retrieve(None)
                    if order.getState() == OrderStates.NewOrder:
                        order.setState(OrderStates.WaitingOrder)
                    orderQueue.insert(None, order)
                    self.__allOrders.retrieve(time).delete(None)
                self.__allOrders.delete(time)
                self.__allOrders.insert(time, orderQueue)
                alltimesCopy.delete(None)
        return

    def cleanup(self, time):
        if not isinstance(time, int):
            return False
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

    def addChocolateMilk(self, chocolateMilk, order, time, timeStamp):
        if not (isinstance(chocolateMilk, ChocolateMilk) and isinstance(order, Order) and isinstance(time, int) and isinstance(timeStamp, int)):
            return False
        sufficientStock = True
        ingredientList = []

        # checks if there are plenty of ingredients
        # adds ingredient to ingredientlist (and removes from stock) if used
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
            # a new order is created
            order.setState(OrderStates.NewOrder)
            self.__newOrders.insert(order.searchkey, order)

            # if the time on which the order is made is not yet used, a queue is inserted
            # the queue is used to hold a queue of orders for that timestamp
            if not self.__allOrders.retrieve(order.searchkey):
                newQueue = QueueWrapper()
                newQueue.create()
                print("allorders time added: ", timeStamp)
                self.__allOrders.insert(timeStamp, newQueue)

            # the order is inserted in the queue for a certain timestamp
            print("order added to allorders with time: ", order.getChocolateMilkId())
            self.__allOrders.retrieve(timeStamp).insert(None, order)

            # adds the current timestamp to maketimes and allTimes if not already in there
            allTimesCopy = copy.deepcopy(self.__allTimes)
            times = []
            while not allTimesCopy.isEmpty():
                times.append(allTimesCopy.retrieve(None))
                allTimesCopy.delete(None)
            if timeStamp not in times:
                self.__makeTimes.insert(None, timeStamp)
                self.__allTimes.insert(None, timeStamp)

            # adds a chocolatemilk to chocolateMilkToBeMade and increases the chocolatemilk count
            self.__chocolateMilkToBeMade.insert(chocolateMilk.searchkey, chocolateMilk)
            print("added to ToBeMade: ", chocolateMilk, " with ingredients: ", chocolateMilk.getIngredients())
            self.__chocolateMilkCount += 1
            return True
        else:
            # returns ingredients to the stock if there is not sufficient stock
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




