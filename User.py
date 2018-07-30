from Order import ChocolateMilk, Order
from Ingredient import ChocolateShot, Honey, Marshmallow, Chilipepper
from bits import text_from_bits
from Enums import ChocolateShotType


class User:
    # zoeksleutel email
    def __init__(self, firstName, lastName, email, UserCount):
        self.__userId = UserCount
        self.__firstName = firstName
        self.__lastName = lastName
        self.__email = email
        self.__currentOrder = None
        self.__chocolateMilk = None

    @property
    def searchkey(self):
        return self.__email

    def getUserId(self):
        return self.__userId

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getEmail(self):
        return text_from_bits(str(self.__email))

    def getCurrentOrder(self):
        return self.__currentOrder

    def getChocolateMilk(self):
        return self.__chocolateMilk

    def createOrder(self, chocolateMilkId):
        if not isinstance(chocolateMilkId, int):
            return False
        self.__currentOrder = Order(self.__userId, chocolateMilkId)
        self.__chocolateMilk = ChocolateMilk(chocolateMilkId)
        return True

    def addHoney(self):
        return self.__chocolateMilk.addIngredient(Honey(0))

    def addMarshmallow(self):
        return self.__chocolateMilk.addIngredient(Marshmallow(0))

    def addChilipepper(self):
        return self.__chocolateMilk.addIngredient(Chilipepper(0))

    def addMilkChocolateShot(self):
        return self.__chocolateMilk.addIngredient(ChocolateShot(0, ChocolateShotType.milk))

    def addBrownChocolateShot(self):
        return self.__chocolateMilk.addIngredient(ChocolateShot(0, ChocolateShotType.brown))

    def addDarkChocolateShot(self):
        return self.__chocolateMilk.addIngredient(ChocolateShot(0, ChocolateShotType.dark))

    def addWhiteChocolateShot(self):
        return self.__chocolateMilk.addIngredient(ChocolateShot(0, ChocolateShotType.white))

    def setCurrentOrder(self, currentOrder):
        self.__currentOrder = currentOrder
        return True

    def setChocolateMilk(self, chocolateMilk):
        self.__chocolateMilk = chocolateMilk
        return True
