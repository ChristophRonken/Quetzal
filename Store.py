from Wrapper import *
import binascii


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

    def createorder(self):
        return

    def addOrder(self, order):
        return self.orders.insert('orderid', order)


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

