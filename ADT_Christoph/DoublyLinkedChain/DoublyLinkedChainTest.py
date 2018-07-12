import sys
import unittest
from ADT_Christoph.DoublyLinkedChain.DoublyLinkedChain import DoublyLinkedChain


class DoublyLinkedChainTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(DoublyLinkedChainTest, self).__init__(*args, **kwargs)
        self.doublyLinkedChain = DoublyLinkedChain()

    def test_createChain(self):
        self.assertTrue(self.doublyLinkedChain.createChain())
        self.assertEqual(self.doublyLinkedChain.head.next, self.doublyLinkedChain.tail)
        self.assertEqual(self.doublyLinkedChain.tail.prev, self.doublyLinkedChain.head)
        self.assertEqual(self.doublyLinkedChain.size, 0)
        self.assertFalse(self.doublyLinkedChain.createChain())

    def test_exists(self):
        self.assertFalse(self.doublyLinkedChain.exists())
        self.doublyLinkedChain.createChain()
        self.assertTrue(self.doublyLinkedChain.exists())

    def test_isEmpty(self):
        self.assertFalse(self.doublyLinkedChain.isEmpty())
        self.doublyLinkedChain.createChain()
        self.assertTrue(self.doublyLinkedChain.isEmpty())
        self.doublyLinkedChain.add(5, "testItem")
        self.assertFalse(self.doublyLinkedChain.isEmpty())

    def test_destroyChain(self):
        self.doublyLinkedChain.createChain()
        self.doublyLinkedChain.add(5, "test0")
        self.doublyLinkedChain.add(6, "test1")
        self.doublyLinkedChain.add(7, "test2")
        self.doublyLinkedChain.destroyChain()
        self.assertEqual(self.doublyLinkedChain.head, None)
        self.assertEqual(self.doublyLinkedChain.tail, None)
        self.assertEqual(self.doublyLinkedChain.size, None)

    def test_add(self):
        self.assertFalse(self.doublyLinkedChain.add(6, "test0"))
        self.doublyLinkedChain.createChain()
        self.assertTrue(self.doublyLinkedChain.add(6, "test0"))
        self.assertTrue(self.doublyLinkedChain.add(7, "test1"))
        self.assertTrue(self.doublyLinkedChain.add(4, "test2"))
        self.assertTrue(self.doublyLinkedChain.add(5, "test3"))

    def test_addFirst(self):
        self.assertFalse(self.doublyLinkedChain.addFirst(6, "test0"))
        self.doublyLinkedChain.createChain()
        self.assertTrue(self.doublyLinkedChain.addFirst(6, "test0"))

    def test_addLast(self):
        self.assertFalse(self.doublyLinkedChain.addLast(6, "test0"))
        self.doublyLinkedChain.createChain()
        self.assertTrue(self.doublyLinkedChain.addLast(6, "test0"))

    def test_isInChain(self):
        self.assertFalse(self.doublyLinkedChain.isInChain(5))
        self.doublyLinkedChain.createChain()
        self.assertFalse(self.doublyLinkedChain.isInChain(5))
        self.assertTrue(self.doublyLinkedChain.add(5, "test0"))
        self.assertTrue(self.doublyLinkedChain.isInChain(5))

    def test_removeLast(self):
        self.assertFalse(self.doublyLinkedChain.removeLast())
        self.doublyLinkedChain.createChain()
        self.assertFalse(self.doublyLinkedChain.removeLast())
        self.assertTrue(self.doublyLinkedChain.add(7, "test1"))
        self.assertTrue(self.doublyLinkedChain.add(4, "test2"))
        self.assertTrue(self.doublyLinkedChain.add(5, "test3"))
        self.assertTrue(self.doublyLinkedChain.removeLast())
        self.assertFalse(self.doublyLinkedChain.isInChain(7))

    def test_removeFirst(self):
        self.assertFalse(self.doublyLinkedChain.removeFirst())
        self.doublyLinkedChain.createChain()
        self.assertFalse(self.doublyLinkedChain.removeFirst())
        self.assertTrue(self.doublyLinkedChain.add(7, "test1"))
        self.assertTrue(self.doublyLinkedChain.add(4, "test2"))
        self.assertTrue(self.doublyLinkedChain.add(5, "test3"))
        self.assertTrue(self.doublyLinkedChain.removeFirst())
        self.assertFalse(self.doublyLinkedChain.isInChain(4))

    def test_remove(self):
        self.assertFalse(self.doublyLinkedChain.remove(5))
        self.doublyLinkedChain.createChain()
        self.assertFalse(self.doublyLinkedChain.remove(5))
        self.assertTrue(self.doublyLinkedChain.add(7, "test1"))
        self.assertTrue(self.doublyLinkedChain.add(4, "test2"))
        self.assertTrue(self.doublyLinkedChain.add(5, "test3"))
        self.assertTrue(self.doublyLinkedChain.add(9, "test4"))
        self.assertTrue(self.doublyLinkedChain.add(6, "test5"))
        self.assertTrue(self.doublyLinkedChain.add(3, "test6"))
        self.assertTrue(self.doublyLinkedChain.remove(3))
        self.assertTrue(self.doublyLinkedChain.remove(5))
        self.assertTrue(self.doublyLinkedChain.remove(9))

    def test_searchkeyRetrieve(self):
        self.assertFalse(self.doublyLinkedChain.searchkeyRetrieve(4))
        self.doublyLinkedChain.createChain()
        self.assertFalse(self.doublyLinkedChain.searchkeyRetrieve(4))
        self.assertTrue(self.doublyLinkedChain.add(7, "test1"))
        self.assertTrue(self.doublyLinkedChain.add(4, "test2"))
        self.assertTrue(self.doublyLinkedChain.add(5, "test3"))


if __name__ == '__main__':
    unittest.main()
    sys.exit(0)