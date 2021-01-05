import unittest
import hello
## VScode says this import does not work, but then the calls below
## work completely fine and the tests work as they should
## based on the code in hello.py

##TODO research PATH stuff, its all new and I think I need more
##background to actually understand whats going on here

class testSuite(unittest.TestCase):
    def test_hi(self):
        ##why would this work if the import is failing
        ##i dont understand at all
        self.assertEqual(hello.hi, 'hi')
    def test_not_hi(self):
        self.assertNotEqual(hello.hi, 'hi')

if __name__ == '__main__':
    print('testing')
    unittest.main()