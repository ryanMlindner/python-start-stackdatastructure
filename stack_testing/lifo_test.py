import sys

print (sys.path)

import unittest
import lifoStack

##TODO answer why 'import lifoStack' does not work, pushing
##code for now for transparency and how
##i track this problem for the future

##week later, i got nothing. REF basic_test.py

class testSuite(unittest.TestCase):
    def setUp(self):
        self.stack = lifoStack.stack()
        self.stack.push("data1")
        self.stack.push("data2")
    def test_stack_empty(self):
        ## stack is empty
        self.assertTrue(self.stack.peek())
    def test_peek_works(self):
        ## comparing top value to expected
        self.assertEqual(self.stack.peek(), "data2", "success")
    def test_pop_works(self):
        ## popping data2 and seeing data1 on top
        self.stack.pop()
        self.assertEqual(self.stack.peek(), "data1")
    def tearDown(self):
        while self.stack.storage:
            self.stack.pop()
        self.assertFalse(self.stack.storage)
print('check')
if __name__ == '__main__':
    print("running")
    unittest.main()
