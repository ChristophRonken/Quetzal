from enum import Enum, auto


class ChocolateShotType(Enum):
    milk = auto()
    white = auto()
    dark = auto()
    brown = auto()


class Ingredient:
    def __init__(self):
        self.credit = 1
        self.price = 0
        self.expirationDate = 0

    @property
    def searchkey(self):
        return self.expirationDate


class ChocolateShot(Ingredient):

    def __init__(self, expirationDate, chocolateShotType):
        Ingredient.__init__(self)
        self.type = chocolateShotType
        self.price = 1
        self.expirationDate = expirationDate


class Honey(Ingredient):

    def __init__(self, expirationDate):
        Ingredient.__init__(self)
        self.price = 0.5
        self.expirationDate = expirationDate


class Marshmallow(Ingredient):

    def __init__(self, expirationDate):
        Ingredient.__init__(self)
        self.price = 0.75
        self.expirationDate = expirationDate


class Chilipepper(Ingredient):

    def __init__(self, expirationDate):
        Ingredient.__init__(self)
        self.price = 0.25
        self.expirationDate = expirationDate
