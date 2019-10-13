from unittest import TestCase
from unittest.mock import patch
from src.calculator import Calculator

class TestCalculator(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum_without_mocking(self):
        calculator = Calculator()
        actual = calculator.sum(2, 4)
        self.assertEqual(6, actual)

    @patch('src.calculator.Calculator')
    def test_sum_with_mocking(self, MockCalculator):
        calculator = MockCalculator()  # create a mock object of Calculator class. This will help to customize output of class methods

        '''
        mock the sum() method of Calculator class to return value '1'. Noth that since we have mocked/stubbed the
        sum method, it will not execute the actual logic whenever called and just return 1 irrespective of input.
        '''
        calculator.sum.return_value = 1  

        actual = calculator.sum(2, 4)   # calling the sum method but the mocked version will actually get called
        expected = 1   # expected is 1 because we are expecting 1 as output from sum method even though sum of 2 & 4 is 6.
        
        self.assertEqual(expected, actual)

        # now override the mocked sum method to return 10
        calculator.sum.return_value = 10
        actual = calculator.sum(1, 1)
        expected = 10
        self.assertEqual(expected, actual)