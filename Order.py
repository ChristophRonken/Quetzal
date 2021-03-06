from Ingredient import *
from Enums import OrderStates


class Order:
    # zoeksleutel timeStamp
    def __init__(self, userId, chocolateMilkId):
        self.__userId = userId
        self.__timeStamp = None
        self.__chocolateMilkId = chocolateMilkId
        self.__state = OrderStates.NotOrdered
        self.__finishedTime = None

    @property
    def searchkey(self):
        return self.__timeStamp

    def setTimeStamp(self, timeStamp):
        if isinstance(timeStamp, int):
            self.__timeStamp = timeStamp
            return True
        return False

    def setFinishedTime(self, finishedTime):
        if isinstance(finishedTime, int):
            self.__finishedTime = finishedTime
            return True
        return False

    def getUserId(self):
        return self.__userId

    def getTimeStamp(self):
        return self.__timeStamp

    def getChocolateMilkId(self):
        return self.__chocolateMilkId

    def getFinishedTime(self):
        return self.__finishedTime

    def setState(self, state):
        self.__state = state
        return True

    def getState(self):
        return self.__state


class ChocolateMilk:
    # zoeksleutel price
    def __init__(self, chocolateMilkId):
        self.__chocolateMilkId = chocolateMilkId
        self.__credit = 5
        self.__price = 2
        self.__ingredients = []

    @property
    def searchkey(self):
        return self.__price

    def getCredit(self):
        return self.__credit

    def getPrice(self):
        return self.__price

    def getIngredients(self):
        return self.__ingredients

    def addIngredient(self, ingredient):
        if (isinstance(ingredient, ChocolateShot) or isinstance(ingredient, Honey) or
                isinstance(ingredient, Chilipepper) or isinstance(ingredient, Marshmallow)):
            self.__price += ingredient.getPrice()
            self.__credit += ingredient.getCredit()
            self.__ingredients.append(ingredient)
            return True
        return False

    def getChocolateMilkId(self):
        return self.__chocolateMilkId
