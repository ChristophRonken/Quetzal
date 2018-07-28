from Order import Order, ChocolateMilk
from Ingredient import *


class User:
    # zoeksleutel email
    def __init__(self, firstName, lastName, email, UserCount):
        self.userID = UserCount
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.currentOrder = None
        self.chocolateMilk = None
        self.orders = []
        UserCount += 1

    def createOrder(self, chocolateMilkId):
        if not isinstance(chocolateMilkId, int):
            return False
        self.currentOrder = Order(self.userID, chocolateMilkId)
        self.chocolateMilk = ChocolateMilk(chocolateMilkId)
        return True

    def addHoney(self):
        return self.chocolateMilk.addIngredient(Honey(0))

    def addMarshmallow(self):
        return self.chocolateMilk.addIngredient(Marshmallow(0))

    def addChilipepper(self):
        return self.chocolateMilk.addIngredient(Chilipepper(0))

    def addMilkChocolateShot(self):
        return self.chocolateMilk.addIngredient(ChocolateShot(0, ChocolateShotType.milk))

    def addBrownChocolateShot(self):
        return self.chocolateMilk.addIngredient(ChocolateShot(0, ChocolateShotType.brown))

    def addDarkChocolateShot(self):
        return self.chocolateMilk.addIngredient(ChocolateShot(0, ChocolateShotType.dark))

    def addWhiteChocolateShot(self):
        return self.chocolateMilk.addIngredient(ChocolateShot(0, ChocolateShotType.white))
