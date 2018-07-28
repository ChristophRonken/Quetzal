import sys
import unittest
from Ingredient import *


class IngredientTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(IngredientTest, self).__init__(*args, **kwargs)

    def test_ingredient(self):
        ingredient = Ingredient()
        self.assertEqual(ingredient.credit, 1)
        self.assertEqual(ingredient.price, 0)
        self.assertEqual(ingredient.expirationDate, 0)
        self.assertEqual(ingredient.searchkey, ingredient.expirationDate)

    def test_milkChocolateShot(self):
        milkChocolateShot = ChocolateShot(20180728, ChocolateShotType.milk)
        self.assertEqual(milkChocolateShot.credit, 1)
        self.assertEqual(milkChocolateShot.price, 1)
        self.assertEqual(milkChocolateShot.expirationDate, 20180728)
        self.assertEqual(milkChocolateShot.searchkey, milkChocolateShot.expirationDate)

    def test_brownChocolateShot(self):
        brownChocolateShot = ChocolateShot(20180728, ChocolateShotType.brown)
        self.assertEqual(brownChocolateShot.credit, 1)
        self.assertEqual(brownChocolateShot.price, 1)
        self.assertEqual(brownChocolateShot.expirationDate, 20180728)
        self.assertEqual(brownChocolateShot.searchkey, brownChocolateShot.expirationDate)

    def test_darkChocolateShot(self):
        darkChocolateShot = ChocolateShot(20180728, ChocolateShotType.dark)
        self.assertEqual(darkChocolateShot.credit, 1)
        self.assertEqual(darkChocolateShot.price, 1)
        self.assertEqual(darkChocolateShot.expirationDate, 20180728)
        self.assertEqual(darkChocolateShot.searchkey, darkChocolateShot.expirationDate)

    def test_whiteChocolateShot(self):
        whiteChocolateShot = ChocolateShot(20180728, ChocolateShotType.milk)
        self.assertEqual(whiteChocolateShot.credit, 1)
        self.assertEqual(whiteChocolateShot.price, 1)
        self.assertEqual(whiteChocolateShot.expirationDate, 20180728)
        self.assertEqual(whiteChocolateShot.searchkey, whiteChocolateShot.expirationDate)

    def test_honey(self):
        honey = Honey(20180728)
        self.assertEqual(honey.credit, 1)
        self.assertEqual(honey.price, 0.5)
        self.assertEqual(honey.expirationDate, 20180728)
        self.assertEqual(honey.searchkey, honey.expirationDate)

    def test_chili(self):
        chili = Chilipepper(20180728)
        self.assertEqual(chili.credit, 1)
        self.assertEqual(chili.price, 0.25)
        self.assertEqual(chili.expirationDate, 20180728)
        self.assertEqual(chili.searchkey, chili.expirationDate)

    def test_marshmallow(self):
        marshmallow = Marshmallow(20180728)
        self.assertEqual(marshmallow.credit, 1)
        self.assertEqual(marshmallow.price, 0.75)
        self.assertEqual(marshmallow.expirationDate, 20180728)
        self.assertEqual(marshmallow.searchkey, marshmallow.expirationDate)


if __name__ == '__main__':
    unittest.main()
    sys.exit(0)