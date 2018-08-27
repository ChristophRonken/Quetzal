import sys
import unittest
from Order import Order, ChocolateMilk
from Ingredient import *


class OrderTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(OrderTest, self).__init__(*args, **kwargs)

    def test_order(self):
        order = Order(5, 7)
        self.assertEqual(order.getUserId(), 5)
        self.assertEqual(order.getChocolateMilkId(), 7)
        self.assertIsNone(order.getTimeStamp())
        self.assertIsNone(order.getFinishedTime())
        self.assertEqual(order.searchkey, order.getTimeStamp())

    def test_setTimeStamp(self):
        order = Order(5, 7)
        self.assertFalse(order.setTimeStamp("not an integer"))
        self.assertTrue(order.setTimeStamp(20180728))
        self.assertEqual(order.getTimeStamp(), 20180728)

    def test_setFinishedTime(self):
        order = Order(5, 7)
        self.assertFalse(order.setFinishedTime("not an integer"))
        self.assertTrue(order.setFinishedTime(20180728))
        self.assertEqual(order.getFinishedTime(), 20180728)


class ChocolateMilkTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(ChocolateMilkTest, self).__init__(*args, **kwargs)

    def test_chocolateMilk(self):
        chocolateMilk = ChocolateMilk(3)
        self.assertEqual(chocolateMilk.getChocolateMilkId(), 3)
        self.assertEqual(chocolateMilk.getCredit(), 5)
        self.assertEqual(chocolateMilk.getPrice(), 2)
        self.assertEqual(chocolateMilk.getIngredients(), [])
        self.assertEqual(chocolateMilk.searchkey, chocolateMilk.getPrice())

    def test_addIngredient(self):
        chocolateMilk = ChocolateMilk(3)
        ingredient = Honey(0)
        self.assertFalse(chocolateMilk.addIngredient("not an ingredient"))
        self.assertTrue(chocolateMilk.addIngredient(ingredient))
        self.assertEqual(chocolateMilk.getCredit(), 5 + ingredient.getCredit())
        self.assertEqual(chocolateMilk.getPrice(), 2 + ingredient.getPrice())




if __name__ == '__main__':
    unittest.main()
    sys.exit(0)