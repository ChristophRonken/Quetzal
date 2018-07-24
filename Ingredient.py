class Ingredient:
    def __init__(self):
        self.name = ""
        self.credit = 0
        self.price = 0
        self.expirationDate = 0
        self.searchkey = self.expirationDate

'''
class ChocolateMilk(Ingredient):

    def __init__(self, expirationDate):
        Ingredient.__init__(self)
        self.name = "ChocolateMilk"
        self.credit = 1
        self.price = 2
        self.expirationDate = expirationDate
        self.searchkey = self.expirationDate
'''


class ChocolateShot(Ingredient):

    def __init__(self, expirationDate):
        # kan witte, melk-, bruine, of zwarte chocolade zijn
        Ingredient.__init__(self)
        self.name = "ChocolateShot"
        self.credit = 1
        self.price = 1
        self.expirationDate = expirationDate


class Honey(Ingredient):

    def __init__(self, expirationDate):
        Ingredient.__init__(self)
        self.name = "Honey"
        self.credit = 1
        self.price = 0.5
        self.expirationDate = expirationDate


class Marshmallow(Ingredient):

    def __init__(self, expirationDate):
        Ingredient.__init__(self)
        self.name = "Marshmallow:"
        self.credit = 1
        self.price = 0.75
        self.expirationDate = expirationDate


class Chilipepper(Ingredient):

    def __init__(self, expirationDate):
        Ingredient.__init__(self)
        self.name = "Chilipepper:"
        self.credit = 1
        self.price = 0.25
        self.expirationDate = expirationDate
