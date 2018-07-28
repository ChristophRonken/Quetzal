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

    def addChocolateShot(self, type):
        return self.chocolateMilk.addIngredient(ChocolateShot(0, type))

    def addChilipepper(self):
        return self.chocolateMilk.addIngredient(Chilipepper(0))


