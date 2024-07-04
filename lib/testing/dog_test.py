import io
import sys
import unittest
from dog import Dog

class TestDog(unittest.TestCase):
    
    def test_name_not_empty(self):
        '''prints "Name must be string between 1 and 25 characters." if empty string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Dog(name="", breed="Beagle")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Name must be string between 1 and 25 characters.\n")

if __name__ == "__main__":
    unittest.main()

