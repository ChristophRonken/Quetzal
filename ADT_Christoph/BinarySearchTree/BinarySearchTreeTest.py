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
        self.assertTrue(self.BST.insert(self.BST.root, 5, "test0"))
        self.assertFalse(self.BST.isEmpty())

    def test_createSearchTree(self):
        self.assertTrue(self.BST.createSearchTree())
        self.assertEqual(self.BST.root, Node(None, None))
        self.assertFalse(self.BST.createSearchTree())

    def test_insert(self):
        self.assertFalse(self.BST.insert(self.BST.root, 5, "test0"))
        self.assertTrue(self.BST.createSearchTree())
        self.assertTrue(self.BST. insert(self.BST.root, 5, "test0"))
        self.assertTrue(self.BST.insert(self.BST.root, 7, "test1"))
        self.assertTrue(self.BST.insert(self.BST.root, 4, "test2"))
        self.assertTrue(self.BST.insert(self.BST.root, 6, "test3"))
        self.assertFalse(self.BST.insert(self.BST.root, 4, "test4"))

    def test_findNode(self):
        self.assertFalse(self.BST.findNode(self.BST.root, 5))
        self.assertTrue(self.BST.createSearchTree())
        self.assertFalse(self.BST.findNode(self.BST.root, 5))
        self.assertTrue(self.BST.insert(self.BST.root, 5, "test0"))
        self.assertTrue(self.BST.insert(self.BST.root, 7, "test1"))
        self.assertTrue(self.BST.insert(self.BST.root, 4, "test2"))
        self.assertEqual(self.BST.findNode(self.BST.root, 5), self.BST.root)
        self.assertEqual(self.BST.findNode(self.BST.root, 7), self.BST.root.rchild)
        self.assertEqual(self.BST.findNode(self.BST.root, 4), self.BST.root.lchild)

    # def deleteNode(self):


if __name__ == '__main__':
    unittest.main()
    sys.exit(0)
