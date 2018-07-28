from enum import Enum, auto


class ChocolateShotType(Enum):
    milk = auto()
    white = auto()
    dark = auto()
    brown = auto()


class ChocolateShot:

    def __init__(self, expirationDate, chocolateShotType):
        self.__type = chocolateShotType
        self.__price = 1
        self.__expirationDate = expirationDate
        self.__credit = 1

    @property
    def searchkey(self):
        return self.__expirationDate

    def getType(self):
        return self.__type

    def getExpirationDate(self):
        return self.__expirationDate

    def getPrice(self):
        return self.__price

    def getCredit(self):
        return self.__credit


class Honey:

    def __init__(self, expirationDate):
        self.__price = 0.5
        self.__expirationDate = expirationDate
        self.__credit = 1

    @property
    def searchkey(self):
        return self.__expirationDate

    def getExpirationDate(self):
        return self.__expirationDate

    def getPrice(self):
        return self.__price

    def getCredit(self):
        return self.__credit


class Marshmallow:

    def __init__(self, expirationDate):
        self.__price = 0.75
        self.__expirationDate = expirationDate
        self.__credit = 1

    @property
    def searchkey(self):
        return self.__expirationDate

    def getExpirationDate(self):
        return self.__expirationDate

    def getPrice(self):
        return self.__price

    def getCredit(self):
        return self.__credit


class Chilipepper:

    def __init__(self, expirationDate):
        self.__price = 0.25
        self.__expirationDate = expirationDate
        self.__credit = 1

    @property
    def searchkey(self):
        return self.__expirationDate

    def getExpirationDate(self):
        return self.__expirationDate

    def getPrice(self):
        return self.__price

    def getCredit(self):
        return self.__credit
