import sys
import unittest
from ADT_Christoph.Stack.Stack import Stack


class StackTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(StackTest, self).__init__(*args, **kwargs)
        self.stack = Stack()

    def test_isEmpty(self):
        self.assertTrue(self.stack.isEmpty())
        self.stack.push(5)
        self.assertFalse(self.stack.isEmpty())

    def test_push(self):
        self.stack.push(27)
        self.assertEqual(self.stack.top.data, 27)

    def test_pop(self):
        self.assertFalse(self.stack.pop())
        self.stack.push(15)
        self.stack.push(27)
        self.assertTrue(self.stack.pop())
        self.assertEqual(self.stack.top.data, 15)

    def test_popDisplay(self):
        self.assertFalse(self.stack.popDisplay())
        self.stack.push(15)
        self.stack.push(27)
        self.assertTrue(self.stack.popDisplay())
        self.assertEqual(self.stack.top.data, 15)
        self.assertEqual(self.stack.topData, 27)

    def test_getTop(self):
        self.assertFalse(self.stack.getTop())
        self.stack.push(15)
        self.assertTrue(self.stack.getTop())
        self.assertEqual(self.stack.topData, 15)

    def test_destroyStack(self):
        self.stack.push(15)
        self.stack.push(27)
        self.stack.getTop()
        self.stack.destroyStack()
        self.assertTrue(self.stack.isEmpty())
        self.assertEqual(self.stack.topData, None)


if __name__ == '__main__':
    unittest.main()
    sys.exit(0)