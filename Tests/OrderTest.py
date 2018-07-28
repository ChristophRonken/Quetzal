import sys
import unittest
from Order import Order, ChocolateMilk
from Ingredient import *


class OrderTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(OrderTest, self).__init__(*args, **kwargs)

    def test_order(self):
        order = Order(5, 7)
        self.assertEqual(order.userId, 5)
        self.assertEqual(order.chocolateMilkId, 7)
        self.assertIsNone(order.timeStamp)
        self.assertFalse(order.pickedUp)

    def test_setTimeStamp(self):
        order = Order(5, 7)
        self.assertFalse(order.setTimeStamp("not an integer"))
        self.assertTrue(order.setTimeStamp(20180728))
        self.assertEqual(order.timeStamp, 20180728)


class ChocolateMilkTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(ChocolateMilkTest, self).__init__(*args, **kwargs)

    def test_chocolateMilk(self):
        chocolateMilk = ChocolateMilk(3)
        self.assertEqual(chocolateMilk.chocolateMilkId, 3)
        self.assertEqual(chocolateMilk.credit, 1)
        self.assertEqual(chocolateMilk.price, 2)
        self.assertEqual(chocolateMilk.searchkey, chocolateMilk.price)

    def test_addIngredient(self):
        chocolateMilk = ChocolateMilk(3)
        ingredient = Honey(0)
        self.assertFalse(chocolateMilk.addIngredient("not an ingredient"))
        self.assertTrue(chocolateMilk.addIngredient(ingredient))
        self.assertEqual(chocolateMilk.credit, 1+ingredient.credit)
        self.assertEqual(chocolateMilk.price, 2+ingredient.price)
        self.assertEqual(chocolateMilk.searchkey, chocolateMilk.price)




if __name__ == '__main__':
    unittest.main()
    sys.exit(0)