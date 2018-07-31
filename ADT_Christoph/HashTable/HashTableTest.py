import sys
import unittest
from ADT_Christoph.HashTable.HashTable import HashTable, Bucket
from Enums import HashTableType
from Wrappers.DLCWrapper import DLCWrapper
from Wrappers.CLCWrapper import CLCWrapper


class HashTableTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(HashTableTest, self).__init__(*args, **kwargs)
        self.hashTableLinear = HashTable()
        self.hashTableLinear.type = HashTableType.Linear
        self.hashTableQuadratic = HashTable()
        self.hashTableQuadratic.type = HashTableType.Quadratic
        self.hashTableSeperate = HashTable()
        self.hashTableSeperate.type = HashTableType.Seperate

    def test_createHashTable(self):
        for i in range(0, len(self.hashTableLinear.table)):
            self.assertEqual(self.hashTableLinear.table[i], None)
        for i in range(0, len(self.hashTableQuadratic.table)):
            self.assertEqual(self.hashTableQuadratic.table[i], None)
        for i in range(0, len(self.hashTableSeperate.table)):
            self.assertEqual(self.hashTableSeperate.table[i], None)

        self.assertTrue(self.hashTableLinear.createHashTable())
        self.assertTrue(self.hashTableQuadratic.createHashTable())
        self.assertTrue(self.hashTableSeperate.createHashTable())

        for i in range(0, len(self.hashTableLinear.table)):
            self.assertEqual(self.hashTableLinear.table[i], Bucket())
        for i in range(0, len(self.hashTableQuadratic.table)):
            self.assertEqual(self.hashTableQuadratic.table[i], Bucket())
        for i in range(0, len(self.hashTableSeperate.table)):
            self.assertIsInstance(self.hashTableSeperate.table[i], CLCWrapper)

    def test_isEmpty(self):
        self.assertFalse(self.hashTableLinear.isEmpty())
        self.assertFalse(self.hashTableQuadratic.isEmpty())
        self.assertFalse(self.hashTableSeperate.isEmpty())

        self.assertTrue(self.hashTableLinear.createHashTable())
        self.assertTrue(self.hashTableQuadratic.createHashTable())
        self.assertTrue(self.hashTableSeperate.createHashTable())

        self.assertTrue(self.hashTableLinear.isEmpty())
        self.assertTrue(self.hashTableQuadratic.isEmpty())
        self.assertTrue(self.hashTableSeperate.isEmpty())

        self.assertTrue(self.hashTableLinear.insert(1, "filled"))
        self.assertTrue(self.hashTableQuadratic.insert(1, "filled"))
        self.assertTrue(self.hashTableSeperate.insert(1, "filled"))

        self.assertFalse(self.hashTableLinear.isEmpty())
        self.assertFalse(self.hashTableQuadratic.isEmpty())
        self.assertFalse(self.hashTableSeperate.isEmpty())

    def test_isFull(self):
        self.assertFalse(self.hashTableLinear.isFull())
        self.assertFalse(self.hashTableQuadratic.isFull())
        self.assertFalse(self.hashTableSeperate.isFull())

        self.assertTrue(self.hashTableLinear.createHashTable())
        self.assertTrue(self.hashTableQuadratic.createHashTable())
        self.assertTrue(self.hashTableSeperate.createHashTable())

        for i in range(0, len(self.hashTableLinear.table)):
            self.assertFalse(self.hashTableLinear.isFull())
            self.assertTrue(self.hashTableLinear.insert(i, "filled"))
        self.assertTrue(self.hashTableLinear.isFull())
        for i in range(0, len(self.hashTableQuadratic.table)):
            self.assertFalse(self.hashTableQuadratic.isFull())
            self.assertTrue(self.hashTableQuadratic.insert(i, "filled"))
        self.assertTrue(self.hashTableQuadratic.isFull())
        for i in range(0, len(self.hashTableSeperate.table)):
            self.assertFalse(self.hashTableSeperate.isFull())
            self.assertTrue(self.hashTableSeperate.insert(i, "filled"))
        self.assertFalse(self.hashTableSeperate.isFull())

    def test_insert(self):
        self.assertFalse(self.hashTableLinear.insert(0, "failed"))
        self.assertFalse(self.hashTableQuadratic.insert(0, "failed"))
        self.assertFalse(self.hashTableSeperate.insert(0, "failed"))

        self.assertTrue(self.hashTableLinear.createHashTable())
        self.assertTrue(self.hashTableQuadratic.createHashTable())
        self.assertTrue(self.hashTableSeperate.createHashTable())

        for i in range(0, len(self.hashTableLinear.table)):
            self.assertFalse(self.hashTableLinear.isFull())
            self.assertTrue(self.hashTableLinear.insert(i, "filled"))
        self.assertFalse(self.hashTableLinear.insert(0, "filled"))
        self.assertTrue(self.hashTableLinear.isFull())
        for i in range(0, len(self.hashTableQuadratic.table)):
            self.assertFalse(self.hashTableQuadratic.isFull())
            self.assertTrue(self.hashTableQuadratic.insert(i, "filled"))
        self.assertFalse(self.hashTableQuadratic.insert(0, "filled"))
        self.assertTrue(self.hashTableQuadratic.isFull())
        for i in range(0, len(self.hashTableSeperate.table)):
            self.assertFalse(self.hashTableSeperate.isFull())
            self.assertTrue(self.hashTableSeperate.insert(i, "filled"))
        self.assertTrue(self.hashTableSeperate.insert(0, "filled"))
        self.assertFalse(self.hashTableSeperate.isFull())

    def test_getLength(self):
        self.assertEqual(self.hashTableLinear.getLength(), self.hashTableLinear.size)
        self.assertEqual(self.hashTableQuadratic.getLength(), self.hashTableQuadratic.size)
        self.assertEqual(self.hashTableSeperate.getLength(), self.hashTableSeperate.size)

    def test_retrieve(self):
        self.assertFalse(self.hashTableLinear.retrieve(0)[0])
        self.assertFalse(self.hashTableQuadratic.retrieve(0)[0])
        self.assertFalse(self.hashTableSeperate.retrieve(0)[0])

        self.assertTrue(self.hashTableLinear.createHashTable())
        self.assertTrue(self.hashTableQuadratic.createHashTable())
        self.assertTrue(self.hashTableSeperate.createHashTable())

        self.assertFalse(self.hashTableLinear.retrieve(0)[0])
        self.assertFalse(self.hashTableQuadratic.retrieve(0)[0])
        self.assertFalse(self.hashTableSeperate.retrieve(0)[0])

        self.assertTrue(self.hashTableLinear.insert(1, "filled"))
        self.assertTrue(self.hashTableQuadratic.insert(1, "filled"))
        self.assertTrue(self.hashTableSeperate.insert(1, "filled"))

        self.assertTrue(self.hashTableLinear.retrieve(1)[0])
        self.assertTrue(self.hashTableQuadratic.retrieve(1)[0])
        self.assertTrue(self.hashTableSeperate.retrieve(1)[0])

        self.assertTrue(self.hashTableLinear.insert(102, "filled"))
        self.assertTrue(self.hashTableQuadratic.insert(102, "filled"))
        self.assertTrue(self.hashTableSeperate.insert(102, "filled"))

        self.assertTrue(self.hashTableLinear.retrieve(102)[0])
        self.assertTrue(self.hashTableQuadratic.retrieve(102)[0])
        self.assertTrue(self.hashTableSeperate.retrieve(102)[0])

        self.assertTrue(self.hashTableLinear.delete(1))
        self.assertTrue(self.hashTableQuadratic.delete(1))
        self.assertTrue(self.hashTableSeperate.delete(1))

        self.assertFalse(self.hashTableLinear.retrieve(1)[0])
        self.assertFalse(self.hashTableQuadratic.retrieve(1)[0])
        self.assertFalse(self.hashTableSeperate.retrieve(1)[0])

        self.assertTrue(self.hashTableLinear.retrieve(102))
        self.assertTrue(self.hashTableQuadratic.retrieve(102))
        self.assertTrue(self.hashTableSeperate.retrieve(102))

        self.assertTrue(self.hashTableLinear.insert(203, "filled"))
        self.assertTrue(self.hashTableQuadratic.insert(203, "filled"))
        self.assertTrue(self.hashTableSeperate.insert(203, "filled"))

        self.assertTrue(self.hashTableLinear.retrieve(203)[0])
        self.assertTrue(self.hashTableQuadratic.retrieve(203)[0])
        self.assertTrue(self.hashTableSeperate.retrieve(203)[0])

    def test_delete(self):
        self.assertFalse(self.hashTableLinear.delete(0))
        self.assertFalse(self.hashTableQuadratic.delete(0))
        self.assertFalse(self.hashTableSeperate.delete(0))

        self.assertTrue(self.hashTableLinear.createHashTable())
        self.assertTrue(self.hashTableQuadratic.createHashTable())
        self.assertTrue(self.hashTableSeperate.createHashTable())

        self.assertFalse(self.hashTableLinear.delete(0))
        self.assertFalse(self.hashTableQuadratic.delete(0))
        self.assertFalse(self.hashTableSeperate.delete(0))

        for i in range(0, len(self.hashTableLinear.table)):
            self.assertFalse(self.hashTableLinear.isFull())
            self.assertTrue(self.hashTableLinear.insert(i, "filled"))
        self.assertFalse(self.hashTableLinear.insert(0, "filled"))
        for i in range(0, len(self.hashTableQuadratic.table)):
            self.assertFalse(self.hashTableQuadratic.isFull())
            self.assertTrue(self.hashTableQuadratic.insert(i, "filled"))
        self.assertFalse(self.hashTableQuadratic.insert(0, "filled"))
        for i in range(0, len(self.hashTableSeperate.table)):
            self.assertFalse(self.hashTableSeperate.isFull())
            self.assertTrue(self.hashTableSeperate.insert(i, "filled"))
        self.assertTrue(self.hashTableSeperate.insert(0, "filled"))

        self.assertTrue(self.hashTableLinear.delete(0))
        self.assertFalse(self.hashTableLinear.delete(0))
        self.assertTrue(self.hashTableQuadratic.delete(0))
        self.assertFalse(self.hashTableQuadratic.delete(0))
        self.assertTrue(self.hashTableSeperate.delete(0))
        self.assertTrue(self.hashTableSeperate.delete(0))
        self.assertFalse(self.hashTableSeperate.delete(0))

    def test_destroyHashTable(self):
        self.assertFalse(self.hashTableLinear.destroyHashTable())
        self.assertFalse(self.hashTableQuadratic.destroyHashTable())
        self.assertFalse(self.hashTableSeperate.destroyHashTable())

        self.assertTrue(self.hashTableLinear.createHashTable())
        self.assertTrue(self.hashTableQuadratic.createHashTable())
        self.assertTrue(self.hashTableSeperate.createHashTable())

        self.assertTrue(self.hashTableLinear.destroyHashTable())
        self.assertTrue(self.hashTableQuadratic.destroyHashTable())
        self.assertTrue(self.hashTableSeperate.destroyHashTable())

        self.assertTrue(self.hashTableLinear.createHashTable())
        self.assertTrue(self.hashTableQuadratic.createHashTable())
        self.assertTrue(self.hashTableSeperate.createHashTable())

        for i in range(0, len(self.hashTableLinear.table)):
            self.assertTrue(self.hashTableLinear.insert(i, "filled"))
        for i in range(0, len(self.hashTableQuadratic.table)):
            self.assertTrue(self.hashTableQuadratic.insert(i, "filled"))
        for i in range(0, len(self.hashTableSeperate.table) + 20):
            self.assertTrue(self.hashTableSeperate.insert(i, "filled"))

        self.assertTrue(self.hashTableLinear.destroyHashTable())
        self.assertTrue(self.hashTableQuadratic.destroyHashTable())
        self.assertTrue(self.hashTableSeperate.destroyHashTable())


if __name__ == '__main__':
    unittest.main()
    sys.exit(0)
