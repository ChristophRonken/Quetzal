import sys
import unittest
from ADT_Cedric.BinarySearchTree import BinarySearchTree, Node

class BinarySearchTreeTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(BinarySearchTreeTest, self).__init__(*args, **kwargs)
        self.BST = BinarySearchTree()

    def test_create_search_tree(self):
        self.assertTrue(self.BST.is_empty())
        self.assertTrue(self.BST.create_search_tree(Node(4)))
        self.assertFalse(self.BST.is_empty())

    def test_search_tree_insert(self):
        self.assertTrue(self.BST.create_search_tree(Node(4)))
        self.assertTrue(self.BST.search_tree_insert(Node(5)))
        self.assertTrue(self.BST.search_tree_insert(Node(6)))
        self.assertFalse(self.BST.search_tree_insert(Node(5)))
        self.assertFalse(self.BST.search_tree_insert(Node(4)))

    def test_search_tree_retrieve(self):
        self.assertTrue(self.BST.create_search_tree(Node(4)))
        self.assertTrue(self.BST.search_tree_insert(Node(5)))
        self.assertTrue(self.BST.search_tree_insert(Node(6)))
        self.assertTrue(self.BST.search_tree_retrieve(4))
        self.assertFalse(self.BST.search_tree_retrieve(7))

    def test_get_size(self):
        self.assertTrue(self.BST.create_search_tree(Node(4)))
        self.assertTrue(self.BST.search_tree_insert(Node(5)))
        self.assertTrue(self.BST.search_tree_insert(Node(6)))
        self.assertEqual(self.BST.get_size(), 3)


if __name__ == '__main__':
    unittest.main()
    sys.exit(0)