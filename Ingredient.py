from enum import Enum, auto


class ChocolateShotType(Enum):
    milk = auto()
    white = auto()
    dark = auto()
    brown = auto()


class Ingredient:
    def __init__(self):
        self.credit = 0
        self.price = 0
        self.expirationDate = 0
        self.searchkey = self.expirationDate


class ChocolateMilk(Ingredient):

    def __init__(self, expirationDate):
        Ingredient.__init__(self)
        self.credit = 1
        self.price = 2
        self.expirationDate = expirationDate
        self.searchkey = self.expirationDate


class ChocolateShot(Ingredient):

    def __init__(self, expirationDate, chocolateShotType):
        print(expirationDate)
        Ingredient.__init__(self)
        self.type = chocolateShotType
        self.credit = 1
        self.price = 1
        self.expirationDate = expirationDate


class Honey(Ingredient):

    def __init__(self, expirationDate):
        Ingredient.__init__(self)
        self.credit = 1
        self.price = 0.5
        self.expirationDate = expirationDate


class Marshmallow(Ingredient):

    def __init__(self, expirationDate):
        Ingredient.__init__(self)
        self.credit = 1
        self.price = 0.75
        self.expirationDate = expirationDate


class Chilipepper(Ingredient):

    def __init__(self, expirationDate):
        Ingredient.__init__(self)
        self.credit = 1
        self.price = 0.25
        self.expirationDate = expirationDate
