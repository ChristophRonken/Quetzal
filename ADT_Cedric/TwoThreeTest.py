import sys
import unittest
from ADT_Cedric.TwoThree import Tree, Node

class TwoThreeTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TwoThreeTest, self).__init__(*args, **kwargs)
        self.Tree = Tree()

    def test_createTree(self):
        self.assertTrue(self.Tree.createTree())
        self.assertEqual(self.Tree.root.searchkeys, [(None, None)])

    def test_isEmpty(self):
        self.assertTrue(self.Tree.createTree())
        self.assertTrue(self.Tree.isEmpty())

    def test_treeInsert(self):
        self.assertTrue(self.Tree.createTree())
        self.assertTrue(self.Tree.treeInsert(5, 'item'))
        self.assertTrue(self.Tree.treeInsert(4, 'item'))
        self.assertFalse(self.Tree.treeInsert(5, 'item'))
        self.assertTrue(self.Tree.treeInsert(6, 'item'))
        self.assertTrue(self.Tree.treeInsert(2, 'item'))
        self.assertFalse(self.Tree.hasAllChildren(self.Tree.root))
        self.assertTrue(self.Tree.treeInsert(3, 'item'))
        self.assertTrue(self.Tree.hasAllChildren(self.Tree.root))

    def test_treeRetrieve(self):
        self.assertTrue(self.Tree.createTree())
        self.assertFalse(self.Tree.treeRetrieve(4))
        self.assertTrue(self.Tree.treeInsert(5, 'item'))
        self.assertTrue(self.Tree.treeInsert(4, 'item'))
        self.assertEqual(self.Tree.treeRetrieve(5),(5, 'item'))



if __name__ == '__main__':
    unittest.main()
    sys.exit(0)