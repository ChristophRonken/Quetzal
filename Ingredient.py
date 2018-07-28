from enum import Enum, auto


class ChocolateShotType(Enum):
    milk = auto()
    white = auto()
    dark = auto()
    brown = auto()


class Ingredient:
    def __init__(self):
        self.__credit = 1
        self.__price = 0
        self.__expirationDate = 0

    @property
    def searchkey(self):
        return self.__expirationDate

    def getCredit(self):
        return self.__credit

    def getPrice(self):
        return self.__price

    def getExpirationDate(self):
        return self.__expirationDate


class ChocolateShot(Ingredient):

    def __init__(self, expirationDate, chocolateShotType):
        Ingredient.__init__(self)
        self.type = chocolateShotType
        self.price = 1
        self.expirationDate = expirationDate

    def getType(self):
        return self.type


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
