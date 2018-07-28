from Ingredient import Ingredient


class Order:
    # zoeksleutel timeStamp
    def __init__(self, userId, chocolateMilkId):
        self.userId = userId
        self.timeStamp = None
        self.chocolateMilkId = chocolateMilkId
        self.pickedUp = False

    @property
    def searchkey(self):
        return self.timeStamp

    def setTimeStamp(self, timeStamp):
        if not isinstance(timeStamp, int):
            return False
        self.timeStamp = timeStamp
        return True


class ChocolateMilk:
    # zoeksleutel price
    def __init__(self, chocolateMilkId):
        self.chocolateMilkId = chocolateMilkId
        self.credit = 1
        self.price = 2
        self.ingredients = []
        chocolateMilkId += 1

    @property
    def searchkey(self):
        return self.price

    def addIngredient(self, ingredient):
        if not isinstance(ingredient, Ingredient):
            return False
        self.price += ingredient.price
        self.credit += ingredient.credit
        self.ingredients.append(ingredient)
        return True
