import LIFOstack
import unittest

stack = LIFOstack.stack()
stack.push("data1")
stack.push("data2")

class testStack(unittest.TestCase):
    def test_stack_empty(self):
        ## stack is empty
        self.assertTrue(stack.isEmpty())
    def test_peek_works(self):
        ## comparing top value to expected
        self.assertEqual(stack.peek(), "data2")
    def test_pop_works(self):
        ## popping data2 and seeing data1 on top
        stack.pop()
        self.assertEqual(stack.peek(), "data1")
    def test_pop_empty_stack(self):
        while stack.storage:
            stack.pop()
        self.assertFalse(stack.storage)

if __name__ == '__main__' :
    unittest.main()
