class User:
    # zoeksleutel email
    def __init__(self, userID, firstName, lastName, email):
        self.userID = userID
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.currentOrder = None
        self.orders = []
        self.store = None

    def createOrder(self):
        return

    def addHoney(self):
        return

    def addMarshmallow(self):
        return

    def addChocolateShot(self):
        return

    def addChilipepper(self):
        return

