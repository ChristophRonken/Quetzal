from Wrapper import *
from Ingredient import *
import binascii
import copy


class Store:

    def __init__(self):
        self.orders = BSTWrapper()
        self.marshmallowStock = DLCWrapper()
        self.milkChocolateStock = DLCWrapper()
        self.darkChocolateStock = DLCWrapper()
        self.whiteChocolateStock = DLCWrapper()
        self.brownChocolateStock = DLCWrapper()
        self.honeyStock = DLCWrapper()
        self.chiliStock = DLCWrapper()

        self.users = DLCWrapper()
        self.workers = QueueWrapper()
        self.workload = StackWrapper()
        self.orderlist = QueueWrapper()

        self.chocolateMilkCount = 0
        self.chocolateMilkToBeMade = DLCWrapper()
        self.finishedChocolateMilks = DLCWrapper()
        self.newOrders = QueueWrapper()
        self.waitingOrders = QueueWrapper()
        self.finishedOrders = DLCWrapper()

        self.money = 0

    def createStore(self):
        self.orders = BSTWrapper()
        self.marshmallowStock.create()
        self.milkChocolateStock.create()
        self.darkChocolateStock.create()
        self.whiteChocolateStock.create()
        self.brownChocolateStock.create()
        self.honeyStock.create()
        self.chiliStock.create()

        self.users.create()
        self.workers.create()
        self.workload.create()
        self.orderlist.create()

        self.chocolateMilkToBeMade.create()
        self.finishedChocolateMilks.create()
        self.newOrders.create()
        self.waitingOrders.create()
        self.finishedOrders.create()

    def addWorker(self, worker):
        self.workers.insert(worker.workerId, worker)
        for i in range(0, worker.workLoad):
            self.workload.insert(None, "credit")

    def work(self):
        workersCopy = copy.deepcopy(self.workers)
        while not workersCopy.isEmpty():
            worker = workersCopy.retrieve()
            if not worker.isBusy:
                order = None
                if not self.waitingOrders.isEmpty():
                    order = self.waitingOrders.retrieve()
                    self.waitingOrders.delete(None)
                elif not self.newOrders.isEmpty():
                    order = self.newOrders.retrieve()
                    self.newOrders.delete(None)
                else:
                    pass
                if order is not None:
                    worker.chocolatemilk = self.chocolateMilkToBeMade.retrieve()
                    worker.busyTime = worker.chocolatemilk.credit
                    worker.isBusy = True
                    worker.order = order
            if worker.isBusy:
                print("busytime: ", worker.busyTime)
                worker.busyTime -= worker.workLoad
                print("maybefinished: ", worker.busyTime)
                if worker.busyTime <= 0:
                    self.finishedOrders.insert(worker.order.searchkey, worker.order)
                    worker.busyTime = 0
                    worker.order = None
                    worker.isBusy = False
                    worker.chocolatemilk = None
            workersCopy.delete(None)
            self.workers.delete(None)
            self.workers.insert(None, worker)
            if not workersCopy.isEmpty():
                worker = workersCopy.retrieve()

        while not self.newOrders.isEmpty():
            order = self.newOrders.retrieve()
            self.newOrders.delete(None)
            self.waitingOrders.insert(order.searchkey, order)

    def cleanup(self, time):
        stocklist = [self.marshmallowStock, self.milkChocolateStock, self.whiteChocolateStock, self.darkChocolateStock,
                     self.brownChocolateStock, self.honeyStock, self.chiliStock]
        for i in range(0, len(stocklist)):
            if stocklist[i].isEmpty():
                continue
            while stocklist[i].retrieve().expirationDate < time:
                stocklist[i].delete(stocklist[i].retrieve().searchkey)
                if stocklist[i].isEmpty():
                    continue

    def makeChocolateMilk(self, chocolateMilk):
        sufficientStock = True
        ingredientList = []
        for i in range(0, len(chocolateMilk.ingredients)):
            if isinstance(chocolateMilk.ingredients[i], ChocolateShot):
                if chocolateMilk.ingredients[i].type == ChocolateShotType.white:
                    if self.whiteChocolateStock.isEmpty():
                        sufficientStock = False
                        continue
                    ingredientList.append(self.whiteChocolateStock.retrieve())
                    self.whiteChocolateStock.delete(self.whiteChocolateStock.retrieve().searchkey)
                if chocolateMilk.ingredients[i].type == ChocolateShotType.dark:
                    if self.darkChocolateStock.isEmpty():
                        sufficientStock = False
                        continue
                    ingredientList.append(self.darkChocolateStock.retrieve())
                    self.darkChocolateStock.delete(self.darkChocolateStock.retrieve().searchkey)
                if chocolateMilk.ingredients[i].type == ChocolateShotType.brown:
                    if self.brownChocolateStock.isEmpty():
                        sufficientStock = False
                        continue
                    ingredientList.append(self.brownChocolateStock.retrieve())
                    self.brownChocolateStock.delete(self.brownChocolateStock.retrieve().searchkey)
                if chocolateMilk.ingredients[i].type == ChocolateShotType.milk:
                    if self.milkChocolateStock.isEmpty():
                        sufficientStock = False
                        continue
                    ingredientList.append(self.milkChocolateStock.retrieve())
                    self.milkChocolateStock.delete(self.milkChocolateStock.retrieve().searchkey)
            if isinstance(chocolateMilk.ingredients[i], Honey):
                if self.honeyStock.isEmpty():
                    sufficientStock = False
                    continue
                ingredientList.append(self.honeyStock.retrieve())
                self.honeyStock.delete(self.honeyStock.retrieve().searchkey)
            if isinstance(chocolateMilk.ingredients[i], Chilipepper):
                if self.chiliStock.isEmpty():
                    sufficientStock = False
                    continue
                ingredientList.append(self.chiliStock.retrieve())
                self.chiliStock.delete(self.chiliStock.retrieve().searchkey)
            if isinstance(chocolateMilk.ingredients[i], Marshmallow):
                if self.marshmallowStock.isEmpty():
                    sufficientStock = False
                    continue
                ingredientList.append(self.marshmallowStock.retrieve())
                self.marshmallowStock.delete(self.marshmallowStock.retrieve().searchkey)
        if sufficientStock:
            self.chocolateMilkToBeMade.insert(chocolateMilk.searchkey, chocolateMilk)
            return True
        else:
            for i in range(0, len(ingredientList)):
                if isinstance(ingredientList[i], ChocolateShot):
                    if ingredientList[i].type == ChocolateShotType.white:
                        self.whiteChocolateStock.insert(ingredientList[i].searchkey, ingredientList[i])
                    if ingredientList[i].type == ChocolateShotType.dark:
                        self.darkChocolateStock.insert(ingredientList[i].searchkey, ingredientList[i])
                    if ingredientList[i].type == ChocolateShotType.brown:
                        self.brownChocolateStock.insert(ingredientList[i].searchkey, ingredientList[i])
                    if ingredientList[i].type == ChocolateShotType.milk:
                        self.milkChocolateStock.insert(ingredientList[i].searchkey, ingredientList[i])
                if isinstance(ingredientList[i], Honey):
                    self.honeyStock.insert(ingredientList[i].searchkey, ingredientList[i])
                if isinstance(ingredientList[i], Chilipepper):
                    self.chiliStock.insert(ingredientList[i].searchkey, ingredientList[i])
                if isinstance(ingredientList[i], Marshmallow):
                    self.marshmallowStock.insert(ingredientList[i].searchkey, ingredientList[i])
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

