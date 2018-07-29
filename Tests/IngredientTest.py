import sys
import unittest
from Ingredient import *


class IngredientTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(IngredientTest, self).__init__(*args, **kwargs)

    def test_milkChocolateShot(self):
        milkChocolateShot = ChocolateShot(20180728, ChocolateShotType.milk)
        self.assertEqual(milkChocolateShot.getCredit(), 1)
        self.assertEqual(milkChocolateShot.getPrice(), 1)
        self.assertEqual(milkChocolateShot.getExpirationDate(), 20180728)
        self.assertEqual(milkChocolateShot.searchkey, milkChocolateShot.getExpirationDate())

    def test_brownChocolateShot(self):
        brownChocolateShot = ChocolateShot(20180728, ChocolateShotType.brown)
        self.assertEqual(brownChocolateShot.getCredit(), 1)
        self.assertEqual(brownChocolateShot.getPrice(), 1)
        self.assertEqual(brownChocolateShot.getExpirationDate(), 20180728)
        self.assertEqual(brownChocolateShot.searchkey, brownChocolateShot.getExpirationDate())

    def test_darkChocolateShot(self):
        darkChocolateShot = ChocolateShot(20180728, ChocolateShotType.dark)
        self.assertEqual(darkChocolateShot.getCredit(), 1)
        self.assertEqual(darkChocolateShot.getPrice(), 1)
        self.assertEqual(darkChocolateShot.getExpirationDate(), 20180728)
        self.assertEqual(darkChocolateShot.searchkey, darkChocolateShot.getExpirationDate())

    def test_whiteChocolateShot(self):
        whiteChocolateShot = ChocolateShot(20180728, ChocolateShotType.milk)
        self.assertEqual(whiteChocolateShot.getCredit(), 1)
        self.assertEqual(whiteChocolateShot.getPrice(), 1)
        self.assertEqual(whiteChocolateShot.getExpirationDate(), 20180728)
        self.assertEqual(whiteChocolateShot.searchkey, whiteChocolateShot.getExpirationDate())

    def test_honey(self):
        honey = Honey(20180728)
        self.assertEqual(honey.getCredit(), 1)
        self.assertEqual(honey.getPrice(), 0.5)
        self.assertEqual(honey.getExpirationDate(), 20180728)
        self.assertEqual(honey.searchkey, honey.getExpirationDate())

    def test_chili(self):
        chili = Chilipepper(20180728)
        self.assertEqual(chili.getCredit(), 1)
        self.assertEqual(chili.getPrice(), 0.25)
        self.assertEqual(chili.getExpirationDate(), 20180728)
        self.assertEqual(chili.searchkey, chili.getExpirationDate())

    def test_marshmallow(self):
        marshmallow = Marshmallow(20180728)
        self.assertEqual(marshmallow.getCredit(), 1)
        self.assertEqual(marshmallow.getPrice(), 0.75)
        self.assertEqual(marshmallow.getExpirationDate(), 20180728)
        self.assertEqual(marshmallow.searchkey, marshmallow.getExpirationDate())


if __name__ == '__main__':
    unittest.main()
    sys.exit(0)