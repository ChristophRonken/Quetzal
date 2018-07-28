from Ingredient import *


class Order:
    # zoeksleutel timeStamp
    def __init__(self, userId, chocolateMilkId):
        self.__userId = userId
        self.__timeStamp = None
        self.__chocolateMilkId = chocolateMilkId
        self.__pickedUp = False
        self.__finishedTime = None

    @property
    def searchkey(self):
        return self.__timeStamp

    def setTimeStamp(self, timeStamp):
        if not isinstance(timeStamp, int):
            return False
        self.__timeStamp = timeStamp
        return True

    def setPickedUp(self, pickedUp):
        self.__pickedUp = pickedUp

    def setFinishedTime(self, finishedTime):
        self.__finishedTime = finishedTime

    def getUserId(self):
        return self.__userId

    def getTimeStamp(self):
        return self.__timeStamp

    def getChocolateMilkId(self):
        return self.__chocolateMilkId

    def getPickedUp(self):
        return self.__pickedUp

    def getFinishedTime(self):
        return self.__finishedTime


class ChocolateMilk:
    # zoeksleutel price
    def __init__(self, chocolateMilkId):
        self.__chocolateMilkId = chocolateMilkId
        self.__credit = 1
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
        self.__price += ingredient.getPrice()
        self.__credit += ingredient.getCredit()
        self.__ingredients.append(ingredient)
        return True

    def getChocolateMilkId(self):
        return self.__chocolateMilkId
