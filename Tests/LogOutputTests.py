import sys
import unittest
import filecmp
from LogOutput import LogOutput
from Store import Store
from Ingredient import *
from Enums import *


class LogOutputTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(LogOutputTest, self).__init__(*args, **kwargs)
        self.log = LogOutput()
        self.store = Store()
        self.store.createStore()

        self.store.addWorker("Werknemer", "Nummer 1", 5)
        self.store.addWorker("Werknemer", "Nummer 2", 10)
        self.store.addUser("Christoph", "Ronken", "ronkenchristoph@gmail.com")
        self.store.addUser("Cedric", "Hollanders", "hollanderscedric@gmail.com")

        self.store.getUser("ronkenchristoph@gmail.com").createOrder(1)
        self.store.getUser("ronkenchristoph@gmail.com").addWhiteChocolateShot()

        for i in range(0, 10):
            self.store.restockBrownChocolateShot(2000)
            self.store.restockWhiteChocolateShot(2000)
            self.store.restockDarkChocolateShot(2000)
            self.store.restockMilkChocolateShot(2000)
            self.store.restockChilipepper(2000)
            self.store.restockHoney(2000)
            self.store.restockMarshmallow(2000)

    def test_logOutput(self):
        for i in range(0,5):
            self.log.addRow(self.store, i)
        self.log.writeHtml()
        self.assertTrue(filecmp.cmp("TestBase.html", "outputLog.html", False))


if __name__ == '__main__':
    unittest.main()
    sys.exit(0)