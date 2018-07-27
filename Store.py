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
        self.waitingOrders.create()
        self.finishedOrders.create()

    def addWorker(self, worker):
        self.workers.insert(worker.workerId, worker)
        for i in range(0, worker.workLoad):
            self.workload.insert(None, "credit")

    def work(self):
        ordersCopy = copy.deepcopy(self.waitingOrders)
        order = ordersCopy.retrieve()
        if order is None:
            return

    def makeChocolateMilk(self, chocolateMilk, time):
        for i in range(0, len(chocolateMilk.ingredients)):
            if isinstance(chocolateMilk.ingredients[i], ChocolateShot):
                print("chocoladeshot")








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

