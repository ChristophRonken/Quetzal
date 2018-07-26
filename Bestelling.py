class Order:
    # zoeksleutel timeStamp
    def __init__(self, userId, chocolateMilkId):
        self.userId = userId
        self.timeStamp = None
        self.chocolateMilkId = chocolateMilkId
        self.price = 0
        self.credits = 0
        self.ingredients = []

    def setTimeStamp(self, timeStamp):
        self.timeStamp = timeStamp

    def addIngredient(self, ingredient):
        self.price += ingredient.price
        self.credits += ingredient.credit
        self.ingredients.append(ingredient)
        return
