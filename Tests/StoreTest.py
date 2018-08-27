import sys
import unittest
from User import User
from Store import Store, text_to_bits
from Worker import Worker
from Order import *
from Enums import *


class StoreTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(StoreTest, self).__init__(*args, **kwargs)
        self.store = Store()
        self.store.createStore()

    def test_store(self):
        self.assertEqual(self.store.getChocolateMilkCount(), 0)
        self.assertEqual(self.store.getUserCount(), 0)
        self.assertEqual(self.store.getWorkerCount(), 0)
        self.assertEqual(self.store.getMoney(), 2000)
        self.assertEqual(self.store.getTime(), 0)

    def test_restockMarshmallow(self):
        moneyBefore = self.store.getMoney()
        self.assertFalse(self.store.restockMarshmallow("20180500"))
        self.assertTrue(self.store.restockMarshmallow(20180500))
        self.assertEqual(self.store.getMoney(), moneyBefore - Marshmallow(0).buyPrice)
        self.assertIsInstance(self.store.getMarshmallowStock().retrieve(None), Marshmallow)
        self.assertEqual(self.store.getMarshmallowStock().retrieve(None).getExpirationDate(), 20180500)

    def test_restockChilipepper(self):
        moneyBefore = self.store.getMoney()
        self.assertFalse(self.store.restockChilipepper("20180500"))
        self.assertTrue(self.store.restockChilipepper(20180500))
        self.assertEqual(self.store.getMoney(), moneyBefore - Chilipepper(0).buyPrice)
        self.assertIsInstance(self.store.getChilipepperStock().retrieve(None), Chilipepper)
        self.assertEqual(self.store.getChilipepperStock().retrieve(None).getExpirationDate(), 20180500)

    def test_restockHoney(self):
        moneyBefore = self.store.getMoney()
        self.assertFalse(self.store.restockChilipepper("20180500"))
        self.assertTrue(self.store.restockHoney(20180500))
        self.assertEqual(self.store.getMoney(), moneyBefore - Honey(0).buyPrice)
        self.assertIsInstance(self.store.getHoneyStock().retrieve(None), Honey)
        self.assertEqual(self.store.getHoneyStock().retrieve(None).getExpirationDate(), 20180500)

    def test_restockMilkChocolateShot(self):
        moneyBefore = self.store.getMoney()
        self.assertFalse(self.store.restockMilkChocolateShot("20180500"))
        self.assertTrue(self.store.restockMilkChocolateShot(20180500))
        self.assertEqual(self.store.getMoney(), moneyBefore - ChocolateShot(0, ChocolateShotType.milk).buyPrice)
        self.assertIsInstance(self.store.getMilkChocolateStock().retrieve(None), ChocolateShot)
        self.assertEqual(self.store.getMilkChocolateStock().retrieve(None).getType(), ChocolateShotType.milk)
        self.assertEqual(self.store.getMilkChocolateStock().retrieve(None).getExpirationDate(), 20180500)

    def test_restockBrownChocolateShot(self):
        moneyBefore = self.store.getMoney()
        self.assertFalse(self.store.restockBrownChocolateShot("20180500"))
        self.assertTrue(self.store.restockBrownChocolateShot(20180500))
        self.assertEqual(self.store.getMoney(), moneyBefore - ChocolateShot(0, ChocolateShotType.brown).buyPrice)
        self.assertIsInstance(self.store.getBrownChocolateStock().retrieve(None), ChocolateShot)
        self.assertEqual(self.store.getBrownChocolateStock().retrieve(None).getType(), ChocolateShotType.brown)
        self.assertEqual(self.store.getBrownChocolateStock().retrieve(None).getExpirationDate(), 20180500)

    def test_restockDarkChocolateShot(self):
        moneyBefore = self.store.getMoney()
        self.assertFalse(self.store.restockDarkChocolateShot("20180500"))
        self.assertTrue(self.store.restockDarkChocolateShot(20180500))
        self.assertEqual(self.store.getMoney(), moneyBefore - ChocolateShot(0, ChocolateShotType.dark).buyPrice)
        self.assertIsInstance(self.store.getDarkChocolateStock().retrieve(None), ChocolateShot)
        self.assertEqual(self.store.getDarkChocolateStock().retrieve(None).getType(), ChocolateShotType.dark)
        self.assertEqual(self.store.getDarkChocolateStock().retrieve(None).getExpirationDate(), 20180500)

    def test_restockWhiteChocolateShot(self):
        moneyBefore = self.store.getMoney()
        self.assertFalse(self.store.restockWhiteChocolateShot("20180500"))
        self.assertTrue(self.store.restockWhiteChocolateShot(20180500))
        self.assertEqual(self.store.getMoney(), moneyBefore - ChocolateShot(0, ChocolateShotType.white).buyPrice)
        self.assertIsInstance(self.store.getWhiteChocolateStock().retrieve(None), ChocolateShot)
        self.assertEqual(self.store.getWhiteChocolateStock().retrieve(None).getType(), ChocolateShotType.white)
        self.assertEqual(self.store.getWhiteChocolateStock().retrieve(None).getExpirationDate(), 20180500)

    def test_addWorker(self):
        self.assertFalse(self.store.addWorker("Christoph", "Ronken", "5"))
        self.assertTrue(self.store.addWorker("Christoph", "Ronken", 5))
        workloadCount = 0
        while not self.store.getWorkload().isEmpty():
            workloadCount += 1
            self.store.getWorkload().delete(None)
        self.assertEqual(workloadCount, 5)

        self.assertIsInstance(self.store.getWorkers().retrieve(None), Worker)
        self.assertEqual(self.store.getWorkers().retrieve(None).getFirstName(), "Christoph")
        self.assertEqual(self.store.getWorkers().retrieve(None).getLastName(), "Ronken")
        self.assertEqual(self.store.getWorkers().retrieve(None).getWorkload(), 5)

    def test_addUser(self):
        self.assertFalse(self.store.addUser("Christoph", 5, "christoph.ronken@student.uantwerpen.be"))
        self.assertTrue(self.store.addUser("Christoph", "Ronken", "christoph.ronken@student.uantwerpen.be"))
        self.assertEqual(self.store.getUserCount(), 1)

        self.assertIsInstance(self.store.getUser("christoph.ronken@student.uantwerpen.be"), User)
        self.assertEqual(self.store.getUser("christoph.ronken@student.uantwerpen.be").getFirstName(), "Christoph")
        self.assertEqual(self.store.getUser("christoph.ronken@student.uantwerpen.be").getLastName(), "Ronken")
        self.assertEqual(self.store.getUser("christoph.ronken@student.uantwerpen.be").getEmail(), "christoph.ronken@student.uantwerpen.be")

    def test_addWorkload(self):
        for i in range(0, 5):
            self.assertTrue(self.store.addWorkload())
        workloadcount = 0
        while not self.store.getWorkload().isEmpty():
            workloadcount += 1
            self.store.getWorkload().delete(None)
        self.assertEqual(workloadcount, 5)

    def test_addChocolateMilkToBeMade(self):
        chocolatemilk = ChocolateMilk(5)
        self.assertFalse(self.store.addChocolateMilkToBeMade(5))
        self.assertTrue(self.store.addChocolateMilkToBeMade(chocolatemilk))
        self.assertEqual(self.store.getChocolateMilkToBeMade().retrieve(None), chocolatemilk)

    def test_addNewOrder(self):
        order = Order(5, 7)
        self.assertFalse(self.store.addNewOrder(5))
        self.assertTrue(self.store.addNewOrder(order))
        self.assertEqual(self.store.getNewOrders().retrieve(None), order)

    def test_addWaitingOrder(self):
        order = Order(5, 7)
        self.assertFalse(self.store.addWaitingOrder(5))
        self.assertTrue(self.store.addWaitingOrder(order))
        self.assertEqual(self.store.getWaitingOrders().retrieve(None), order)

    def test_tick(self):
        timeBefore = self.store.getTime()
        self.store.tick()
        self.assertEqual(timeBefore + 1, self.store.getTime())

    def test_cleanup(self):
        self.store.restockMarshmallow(10)
        self.store.restockMarshmallow(11)
        self.store.restockChilipepper(5)
        self.store.restockChilipepper(15)
        self.store.restockHoney(15)
        self.store.restockHoney(5)
        self.store.restockBrownChocolateShot(9)
        self.store.restockBrownChocolateShot(8)
        self.assertFalse(self.store.cleanup("tijd"))
        self.assertTrue(self.store.cleanup(10))
        marshmallowCount = 0
        while not self.store.getMarshmallowStock().isEmpty():
            self.store.getMarshmallowStock().delete(None)
            marshmallowCount += 1
        self.assertEqual(marshmallowCount, 2)
        chilipepperCount = 0
        while not self.store.getChilipepperStock().isEmpty():
            self.store.getChilipepperStock().delete(None)
            chilipepperCount += 1
        self.assertEqual(chilipepperCount, 1)
        honeyCount = 0
        while not self.store.getHoneyStock().isEmpty():
            self.store.getHoneyStock().delete(None)
            honeyCount += 1
        self.assertEqual(honeyCount, 1)
        self.assertTrue(self.store.getBrownChocolateStock().isEmpty())


if __name__ == '__main__':
    unittest.main()
    sys.exit(0)