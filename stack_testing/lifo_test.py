import unittest
import lifoStack

##TODO answer why 'import lifoStack' does not work, pushing
##code for now for transparency and how
##i track this problem for the future

##week later, i got nothing. REF basic_test.py

stack = lifoStack.stack()
stack.push("data1")
stack.push("data2")

class testSuite(unittest.TestCase):      
    def test_stack_empty(self):
        ## stack is empty
        self.assertTrue(stack.peek())
    def test_peek_works(self):
        ## comparing top value to expected
        self.assertEqual(stack.peek(), "data2", "success")
    def test_pop_works(self):
        ## popping data2 and seeing data1 on top
        stack.pop()
        self.assertEqual(stack.peek(), "data1")
    def tearDown(self):
        while stack.storage:
            stack.pop()
        self.assertFalse(stack.storage)

if __name__ == '__main__':
    print("running")
    unittest.main()
