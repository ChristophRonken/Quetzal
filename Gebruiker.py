from Bestelling import Order, ChocolateMilk
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
        self.currentOrder = Order(self.userID, chocolateMilkId)
        self.chocolateMilk = ChocolateMilk(chocolateMilkId)
        return

    def addHoney(self):
        honey = Honey(0)
        self.chocolateMilk.addIngredient(honey)
        return

    def addMarshmallow(self):
        marshmallow = Marshmallow(0)
        self.chocolateMilk.addIngredient(marshmallow)
        return

    def addChocolateShot(self, type):
        chocoladeshot = ChocolateShot(0, type)
        self.chocolateMilk.addIngredient(chocoladeshot)
        return

    def addChilipepper(self):
        chili = Chilipepper(0)
        self.chocolateMilk.addIngredient(chili)
        return

