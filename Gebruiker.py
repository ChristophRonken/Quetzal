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

    def createOrder(self):
        return

    def pushOrder(self):
        return

    def addHoney(self):
        return

    def addMarshmallow(self):
        return

    def addChocolateShot(self):
        return

    def addChilipepper(self):
        return

