import sys
import unittest
from ADT_Christoph.HashTable.HashTable import HashTable, Bucket, HashTableType


class HashTableTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(HashTableTest, self).__init__(*args, **kwargs)
        self.hashTableType1 = HashTable()
        self.hashTableType1.type = HashTableType.Type1
        self.hashTableType2 = HashTable()
        self.hashTableType2.type = HashTableType.Type2
        self.hashTableType3 = HashTable()
        self.hashTableType3.type = HashTableType.Type3

    def test_createHashTable(self):
        for i in range(0, len(self.hashTableType1.table)):
            self.assertEqual(self.hashTableType1.table[i], None)
        for i in range(0, len(self.hashTableType2.table)):
            self.assertEqual(self.hashTableType2.table[i], None)
        for i in range(0, len(self.hashTableType3.table)):
            self.assertEqual(self.hashTableType3.table[i], None)

        self.assertTrue(self.hashTableType1.createHashTable())
        self.assertTrue(self.hashTableType2.createHashTable())
        self.assertTrue(self.hashTableType3.createHashTable())

        for i in range(0, len(self.hashTableType1.table)):
            self.assertEqual(self.hashTableType1.table[i], Bucket())
        for i in range(0, len(self.hashTableType2.table)):
            self.assertEqual(self.hashTableType2.table[i], Bucket())
        for i in range(0, len(self.hashTableType3.table)):
            self.assertEqual(self.hashTableType3.table[i], Bucket())

    def test_isEmpty(self):
        self.assertFalse(self.hashTableType1.isEmpty())
        self.assertFalse(self.hashTableType2.isEmpty())
        self.assertFalse(self.hashTableType3.isEmpty())

        self.assertTrue(self.hashTableType1.createHashTable())
        self.assertTrue(self.hashTableType2.createHashTable())
        self.assertTrue(self.hashTableType3.createHashTable())

        self.assertTrue(self.hashTableType1.isEmpty())
        self.assertTrue(self.hashTableType2.isEmpty())
        self.assertTrue(self.hashTableType3.isEmpty())

        self.assertTrue(self.hashTableType1.insert(1, "filled"))
        self.assertTrue(self.hashTableType2.insert(1, "filled"))
        self.assertTrue(self.hashTableType3.insert(1, "filled"))

        self.assertFalse(self.hashTableType1.isEmpty())
        self.assertFalse(self.hashTableType2.isEmpty())
        self.assertFalse(self.hashTableType3.isEmpty())

    def test_isFull(self):
        self.assertFalse(self.hashTableType1.isFull())
        self.assertFalse(self.hashTableType2.isFull())
        self.assertFalse(self.hashTableType3.isFull())

        self.assertTrue(self.hashTableType1.createHashTable())
        self.assertTrue(self.hashTableType2.createHashTable())
        self.assertTrue(self.hashTableType3.createHashTable())

        for i in range(0, len(self.hashTableType1.table)):
            self.assertFalse(self.hashTableType1.isFull())
            self.assertTrue(self.hashTableType1.insert(i, "filled"))
        self.assertTrue(self.hashTableType1.isFull())
        for i in range(0, len(self.hashTableType2.table)):
            self.assertFalse(self.hashTableType2.isFull())
            self.assertTrue(self.hashTableType2.insert(i, "filled"))
        self.assertTrue(self.hashTableType2.isFull())
        for i in range(0, len(self.hashTableType3.table)):
            self.assertFalse(self.hashTableType3.isFull())
            self.assertTrue(self.hashTableType3.insert(i, "filled"))
        self.assertFalse(self.hashTableType3.isFull())

    def test_insert(self):
        self.assertFalse(self.hashTableType1.insert(0, "failed"))
        self.assertFalse(self.hashTableType2.insert(0, "failed"))
        self.assertFalse(self.hashTableType3.insert(0, "failed"))

        self.assertTrue(self.hashTableType1.createHashTable())
        self.assertTrue(self.hashTableType2.createHashTable())
        self.assertTrue(self.hashTableType3.createHashTable())

        for i in range(0, len(self.hashTableType1.table)):
            self.assertFalse(self.hashTableType1.isFull())
            self.assertTrue(self.hashTableType1.insert(i, "filled"))
        self.assertFalse(self.hashTableType1.insert(0, "filled"))
        for i in range(0, len(self.hashTableType2.table)):
            self.assertFalse(self.hashTableType2.isFull())
            self.assertTrue(self.hashTableType2.insert(i, "filled"))
        self.assertFalse(self.hashTableType2.insert(0, "filled"))
        for i in range(0, len(self.hashTableType3.table)):
            self.assertFalse(self.hashTableType3.isFull())
            self.assertTrue(self.hashTableType3.insert(i, "filled"))
        self.assertTrue(self.hashTableType3.insert(0, "filled"))

    def test_getLength(self):
        self.assertEqual(self.hashTableType1.getLength(), self.hashTableType1.size)
        self.assertEqual(self.hashTableType2.getLength(), self.hashTableType2.size)
        self.assertEqual(self.hashTableType3.getLength(), self.hashTableType3.size)

    def test_retrieve(self):
        self.assertFalse(self.hashTableType1.retrieve(0))
        self.assertFalse(self.hashTableType2.retrieve(0))
        self.assertFalse(self.hashTableType3.retrieve(0))

        self.assertTrue(self.hashTableType1.createHashTable())
        self.assertTrue(self.hashTableType2.createHashTable())
        self.assertTrue(self.hashTableType3.createHashTable())

        self.assertTrue(self.hashTableType1.insert(1, "filled"))
        self.assertTrue(self.hashTableType2.insert(1, "filled"))
        self.assertTrue(self.hashTableType3.insert(1, "filled"))

        self.assertTrue(self.hashTableType1.retrieve(1))
        self.assertTrue(self.hashTableType2.retrieve(1))
        self.assertTrue(self.hashTableType3.retrieve(1))

        self.assertTrue(self.hashTableType1.insert(102, "filled"))
        self.assertTrue(self.hashTableType2.insert(102, "filled"))
        self.assertTrue(self.hashTableType3.insert(102, "filled"))

        self.assertTrue(self.hashTableType1.retrieve(102))
        self.assertTrue(self.hashTableType2.retrieve(102))
        self.assertTrue(self.hashTableType3.retrieve(102))

        self.assertTrue(self.hashTableType1.delete(1))
        self.assertTrue(self.hashTableType2.delete(1))
        self.assertTrue(self.hashTableType3.delete(1))

        self.assertFalse(self.hashTableType1.retrieve(1))
        self.assertFalse(self.hashTableType2.retrieve(1))
        self.assertFalse(self.hashTableType3.retrieve(1))

        self.assertTrue(self.hashTableType1.retrieve(102))
        self.assertTrue(self.hashTableType2.retrieve(102))
        self.assertTrue(self.hashTableType3.retrieve(102))

        self.assertTrue(self.hashTableType1.insert(203, "filled"))
        self.assertTrue(self.hashTableType2.insert(203, "filled"))
        self.assertTrue(self.hashTableType3.insert(203, "filled"))

        self.assertTrue(self.hashTableType1.retrieve(203))
        self.assertTrue(self.hashTableType2.retrieve(203))
        self.assertTrue(self.hashTableType3.retrieve(203))

    def test_delete(self):
        self.assertFalse(self.hashTableType1.delete(0))
        self.assertFalse(self.hashTableType2.delete(0))
        self.assertFalse(self.hashTableType3.delete(0))

        self.assertTrue(self.hashTableType1.createHashTable())
        self.assertTrue(self.hashTableType2.createHashTable())
        self.assertTrue(self.hashTableType3.createHashTable())

        self.assertFalse(self.hashTableType1.delete(0))
        self.assertFalse(self.hashTableType2.delete(0))
        self.assertFalse(self.hashTableType3.delete(0))

        for i in range(0, len(self.hashTableType1.table)):
            self.assertFalse(self.hashTableType1.isFull())
            self.assertTrue(self.hashTableType1.insert(i, "filled"))
        self.assertFalse(self.hashTableType1.insert(0, "filled"))
        for i in range(0, len(self.hashTableType2.table)):
            self.assertFalse(self.hashTableType2.isFull())
            self.assertTrue(self.hashTableType2.insert(i, "filled"))
        self.assertFalse(self.hashTableType2.insert(0, "filled"))
        for i in range(0, len(self.hashTableType3.table)):
            self.assertFalse(self.hashTableType3.isFull())
            self.assertTrue(self.hashTableType3.insert(i, "filled"))
        self.assertTrue(self.hashTableType3.insert(0, "filled"))

        self.assertTrue(self.hashTableType1.delete(0))
        self.assertFalse(self.hashTableType1.delete(0))
        self.assertTrue(self.hashTableType2.delete(0))
        self.assertFalse(self.hashTableType2.delete(0))
        self.assertTrue(self.hashTableType3.delete(0))
        self.assertTrue(self.hashTableType3.delete(0))
        self.assertFalse(self.hashTableType3.delete(0))

    def test_destroyHashTable(self):
        self.assertFalse(self.hashTableType1.destroyHashTable())
        self.assertFalse(self.hashTableType2.destroyHashTable())
        self.assertFalse(self.hashTableType3.destroyHashTable())

        self.assertTrue(self.hashTableType1.createHashTable())
        self.assertTrue(self.hashTableType2.createHashTable())
        self.assertTrue(self.hashTableType3.createHashTable())

        self.assertTrue(self.hashTableType1.destroyHashTable())
        self.assertTrue(self.hashTableType2.destroyHashTable())
        self.assertTrue(self.hashTableType3.destroyHashTable())

        self.assertTrue(self.hashTableType1.createHashTable())
        self.assertTrue(self.hashTableType2.createHashTable())
        self.assertTrue(self.hashTableType3.createHashTable())

        for i in range(0, len(self.hashTableType1.table)):
            self.assertTrue(self.hashTableType1.insert(i, "filled"))
        for i in range(0, len(self.hashTableType2.table)):
            self.assertTrue(self.hashTableType2.insert(i, "filled"))
        for i in range(0, len(self.hashTableType3.table) + 20):
            self.assertTrue(self.hashTableType3.insert(i, "filled"))

        self.assertTrue(self.hashTableType1.destroyHashTable())
        self.assertTrue(self.hashTableType2.destroyHashTable())
        self.assertTrue(self.hashTableType3.destroyHashTable())


if __name__ == '__main__':
    unittest.main()
    sys.exit(0)