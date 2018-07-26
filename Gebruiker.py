from Bestelling import Order
from Ingredient import *

UserIdCount = 1


class User:
    # zoeksleutel email
    def __init__(self, firstName, lastName, email):
        global UserIdCount
        self.userID = UserIdCount
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.currentOrder = None
        self.orders = []
        self.store = None
        UserIdCount += 1

    def createOrder(self, chocolateMilkId):
        self.currentOrder = Order(self.userID, chocolateMilkId)
        return

    def pushOrder(self):
        return

    def addHoney(self):
        honey = Honey(0)
        self.currentOrder.addIngredient(honey)
        return

    def addMarshmallow(self):
        marshmallow = Marshmallow(0)
        self.currentOrder.addIngredient(marshmallow)
        return

    def addChocolateShot(self, type):
        chocoladeshot = ChocolateShot(0, type)
        self.currentOrder.addIngredient(chocoladeshot)
        return

    def addChilipepper(self):
        chili = Chilipepper(0)
        self.currentOrder.addIngredient(chili)
        return

