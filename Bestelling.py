class Order:
    # zoeksleutel timeStamp
    def __init__(self, userId, chocolateMilkId):
        self.userId = userId
        self.timeStamp = None
        self.chocolateMilkId = chocolateMilkId

    @property
    def searchkey(self):
        return self.timeStamp

    def setTimeStamp(self, timeStamp):
        self.timeStamp = timeStamp


class ChocolateMilk:
    # zoeksleutel price
    def __init__(self, chocolateMilkId):
        self.chocolateMilkId = chocolateMilkId
        self.credit = 1
        self.price = 2
        self.ingredients = []

    @property
    def searchkey(self):
        return self.price

    def addIngredient(self, ingredient):
        self.price += ingredient.price
        self.credit += ingredient.credit
        self.ingredients.append(ingredient)
        return
