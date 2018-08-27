import sys
import unittest
from ADT_Christoph.BinarySearchTree.BinarySearchTree import BinarySearchTree, Node


class BinarySearchTreeTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(BinarySearchTreeTest, self).__init__(*args, **kwargs)
        self.BST = BinarySearchTree()

    def test_exists(self):
        self.assertFalse(self.BST.exists())
        self.assertTrue(self.BST.createSearchTree())
        self.assertTrue(self.BST.exists())

    def test_isEmpty(self):
        self.assertFalse(self.BST.isEmpty())
        self.assertTrue(self.BST.createSearchTree())
        self.assertTrue(self.BST.isEmpty())
        self.assertTrue(self.BST.insert(5, "test0"))
        self.assertFalse(self.BST.isEmpty())

    def test_createSearchTree(self):
        self.assertTrue(self.BST.createSearchTree())
        self.assertEqual(self.BST.root, Node(None, None))
        self.assertFalse(self.BST.createSearchTree())

    def test_insert(self):
        self.assertFalse(self.BST.insert(5, "test0"))
        self.assertTrue(self.BST.createSearchTree())
        self.assertTrue(self.BST. insert(5, "test0"))
        self.assertTrue(self.BST.insert(7, "test1"))
        self.assertTrue(self.BST.insert(4, "test2"))
        self.assertTrue(self.BST.insert(6, "test3"))
        self.assertFalse(self.BST.insert(4, "test4"))

    def test_findNode(self):
        self.assertFalse(self.BST.findNode(5))
        self.assertTrue(self.BST.createSearchTree())
        self.assertFalse(self.BST.findNode(5))
        self.assertTrue(self.BST.insert(5, "test0"))
        self.assertTrue(self.BST.insert(7, "test1"))
        self.assertTrue(self.BST.insert(4, "test2"))
        self.assertEqual(self.BST.findNode(5), self.BST.root)
        self.assertEqual(self.BST.findNode(7), self.BST.root.rchild)
        self.assertEqual(self.BST.findNode(4), self.BST.root.lchild)

    def test_retrieve(self):
        self.assertFalse(self.BST.retrieve(5)[0])
        self.assertTrue(self.BST.createSearchTree())
        self.assertFalse(self.BST.findNode(5))
        self.assertTrue(self.BST.insert(5, "test0"))
        self.assertTrue(self.BST.insert(7, "test1"))
        self.assertTrue(self.BST.insert(4, "test2"))
        self.assertTrue(self.BST.retrieve(5)[0])
        self.assertTrue(self.BST.retrieve(7)[0])
        self.assertTrue(self.BST.retrieve(4)[0])

    def test_delete(self):
        self.assertFalse(self.BST.retrieve(5)[0])
        self.assertTrue(self.BST.createSearchTree())
        self.assertFalse(self.BST.findNode(5))
        self.assertTrue(self.BST.insert(5, "test0"))
        self.assertTrue(self.BST.insert(7, "test1"))
        self.assertTrue(self.BST.insert(4, "test2"))
        self.assertTrue(self.BST.insert(8, "test3"))
        self.assertTrue(self.BST.insert(6, "test4"))
        self.assertTrue(self.BST.insert(9, "test5"))
        self.assertTrue(self.BST.insert(13, "test6"))
        self.assertTrue(self.BST.insert(10, "test7"))
        self.assertTrue(self.BST.insert(11, "test8"))
        self.BST.inOrder()
        self.assertTrue(self.BST.delete(9))
        self.assertTrue(self.BST.delete(5))
        self.assertTrue(self.BST.delete(4))
        self.assertTrue(self.BST.delete(11))
        self.assertTrue(self.BST.delete(8))

    def test_destroyTree(self):
        self.BST.destroySearchTree()
        self.assertTrue(self.BST.createSearchTree())
        self.assertFalse(self.BST.findNode(5))
        self.assertTrue(self.BST.insert(5, "test0"))
        self.assertTrue(self.BST.insert(7, "test1"))
        self.assertTrue(self.BST.insert(4, "test2"))
        self.assertTrue(self.BST.insert(8, "test3"))
        self.assertTrue(self.BST.insert(6, "test4"))
        self.assertTrue(self.BST.insert(9, "test8"))
        self.BST.destroySearchTree()
        self.assertEqual(self.BST.root, None)




if __name__ == '__main__':
    unittest.main()
    sys.exit(0)
