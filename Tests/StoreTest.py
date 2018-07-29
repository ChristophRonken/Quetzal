import sys
import unittest
from User import User
from Store import Store, text_to_bits
from Ingredient import *
from Worker import Worker


class StoreTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(StoreTest, self).__init__(*args, **kwargs)
        self.store = Store()
        self.store.createStore()

    def test_store(self):
        self.assertEqual(self.store.getChocolateMilkCount(), 0)
        self.assertEqual(self.store.getUserCount(), 0)
        self.assertEqual(self.store.getWorkerCount(), 0)
        self.assertEqual(self.store.getMoney(), 0)
        self.assertEqual(self.store.getTime(), 0)

    def test_restockMarshmallow(self):
        self.assertTrue(self.store.restockMarshmallow(20180500))
        self.assertIsInstance(self.store.getMarshmallowStock().retrieve(None), Marshmallow)
        self.assertEqual(self.store.getMarshmallowStock().retrieve(None).getExpirationDate(), 20180500)

    def test_restockChilipepper(self):
        self.assertTrue(self.store.restockChilipepper(20180500))
        self.assertIsInstance(self.store.getChilipepperStock().retrieve(None), Chilipepper)
        self.assertEqual(self.store.getChilipepperStock().retrieve(None).getExpirationDate(), 20180500)

    def test_restockHoney(self):
        self.assertTrue(self.store.restockHoney(20180500))
        self.assertIsInstance(self.store.getHoneyStock().retrieve(None), Honey)
        self.assertEqual(self.store.getHoneyStock().retrieve(None).getExpirationDate(), 20180500)

    def test_restockMilkChocolateShot(self):
        self.assertTrue(self.store.restockMilkChocolateShot(20180500))
        self.assertIsInstance(self.store.getMilkChocolateStock().retrieve(None), ChocolateShot)
        self.assertEqual(self.store.getMilkChocolateStock().retrieve(None).getType(), ChocolateShotType.milk)
        self.assertEqual(self.store.getMilkChocolateStock().retrieve(None).getExpirationDate(), 20180500)

    def test_restockBrownChocolateShot(self):
        self.assertTrue(self.store.restockBrownChocolateShot(20180500))
        self.assertIsInstance(self.store.getBrownChocolateStock().retrieve(None), ChocolateShot)
        self.assertEqual(self.store.getBrownChocolateStock().retrieve(None).getType(), ChocolateShotType.brown)
        self.assertEqual(self.store.getBrownChocolateStock().retrieve(None).getExpirationDate(), 20180500)

    def test_restockDarkChocolateShot(self):
        self.assertTrue(self.store.restockDarkChocolateShot(20180500))
        self.assertIsInstance(self.store.getDarkChocolateStock().retrieve(None), ChocolateShot)
        self.assertEqual(self.store.getDarkChocolateStock().retrieve(None).getType(), ChocolateShotType.dark)
        self.assertEqual(self.store.getDarkChocolateStock().retrieve(None).getExpirationDate(), 20180500)

    def test_restockWhiteChocolateShot(self):
        self.assertTrue(self.store.restockWhiteChocolateShot(20180500))
        self.assertIsInstance(self.store.getWhiteChocolateStock().retrieve(None), ChocolateShot)
        self.assertEqual(self.store.getWhiteChocolateStock().retrieve(None).getType(), ChocolateShotType.white)
        self.assertEqual(self.store.getWhiteChocolateStock().retrieve(None).getExpirationDate(), 20180500)

    def test_addWorker(self):
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




if __name__ == '__main__':
    unittest.main()
    sys.exit(0)