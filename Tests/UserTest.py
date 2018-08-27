import sys
import unittest
from User import User
from Order import ChocolateMilk, Order
from bits import *


class UserTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(UserTest, self).__init__(*args, **kwargs)

    def test_user(self):
        user = User("Christoph", "Ronken", "christoph.ronken@student.uantwerpen.be", 5)
        self.assertEqual(user.getUserId(), 5)
        self.assertEqual(user.getFirstName(), "Christoph")
        self.assertEqual(user.getLastName(), "Ronken")
        self.assertEqual(user.getEmail(), "christoph.ronken@student.uantwerpen.be")
        self.assertIsNone(user.getCurrentOrder())
        self.assertIsNone(user.getChocolateMilk())
        self.assertEqual(user.searchkey, int(text_to_bits(user.getEmail())))

    def test_createOrder(self):
        user = User("Christoph", "Ronken", "christoph.ronken@student.uantwerpen.be", 7)
        self.assertFalse(user.createOrder("not an integer"))
        self.assertTrue(user.createOrder(5))
        self.assertIsInstance(user.getCurrentOrder(), Order)
        self.assertIsInstance(user.getChocolateMilk(), ChocolateMilk)

    def test_setCurrentOrder(self):
        user = User("Christoph", "Ronken", "christoph.ronken@student.uantwerpen.be", 7)
        self.assertTrue(user.createOrder(5))
        self.assertTrue(user.setCurrentOrder(None))
        self.assertIsNone(user.getCurrentOrder())
        
    def test_setChocolateMilk(self):
        user = User("Christoph", "Ronken", "christoph.ronken@student.uantwerpen.be", 7)
        self.assertTrue(user.createOrder(5))
        self.assertTrue(user.setChocolateMilk(None))
        self.assertIsNone(user.getChocolateMilk())

    def test_addHoney(self):
        user = User("Christoph", "Ronken", "christoph.ronken@student.uantwerpen.be", 7)
        user.createOrder(5)
        self.assertTrue(user.addHoney())

    def test_addMarshmallow(self):
        user = User("Christoph", "Ronken", "christoph.ronken@student.uantwerpen.be", 7)
        user.createOrder(5)
        self.assertTrue(user.addMarshmallow())

    def test_addChilipepper(self):
        user = User("Christoph", "Ronken", "christoph.ronken@student.uantwerpen.be", 7)
        user.createOrder(5)
        self.assertTrue(user.addChilipepper())

    def test_addMilkChocolateShot(self):
        user = User("Christoph", "Ronken", "christoph.ronken@student.uantwerpen.be", 7)
        user.createOrder(5)
        self.assertTrue(user.addMilkChocolateShot())

    def test_addBrownChocolateShot(self):
        user = User("Christoph", "Ronken", "christoph.ronken@student.uantwerpen.be", 7)
        user.createOrder(5)
        self.assertTrue(user.addBrownChocolateShot())

    def test_addDarkChocolateShot(self):
        user = User("Christoph", "Ronken", "christoph.ronken@student.uantwerpen.be", 7)
        user.createOrder(5)
        self.assertTrue(user.addDarkChocolateShot())

    def test_addWhiteChocolateShot(self):
        user = User("Christoph", "Ronken", "christoph.ronken@student.uantwerpen.be", 7)
        user.createOrder(5)
        self.assertTrue(user.addWhiteChocolateShot())



if __name__ == '__main__':
    unittest.main()
    sys.exit(0)