import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)



        

if __name__ == "__main__":
    unittest.main()



# The test results from Test.py to __init__.py was 1 test was ran and it passed successfully. The test case tested the sum function with a list of integers and verified that the result was correct.
#First it ran 1 test to check if the fucntions in _init__.py were working correctly. 
# Next it came back with an "OK" which means that the test was passed.