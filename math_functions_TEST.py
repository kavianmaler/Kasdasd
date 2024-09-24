import unittest
import sys
# sys.path.append('C:/Users/am-user338/Desktop/Data_Olaf_Piltz/KW 39/Python_Unitest')
from KW_39.Python_Unitest.mmath_stuff import calculate_mean, squared_error


class TestMathFunctions(unittest.TestCase):

    # Tests for calculate_mean
    def test_calculate_mean_valid(self):
        self.assertEqual(calculate_mean([2, 4, 6]), 4)
        self.assertAlmostEqual(calculate_mean([1.5, 3.5, 5.5]), 3.5)

    def test_calculate_mean_invalid_empty_list(self):
        with self.assertRaises(ValueError) as context:
            calculate_mean([])
        self.assertEqual(str(context.exception), "Input must be a non-empty list.")

    def test_calculate_mean_invalid_non_numeric(self):
        with self.assertRaises(ValueError) as context:
            calculate_mean([1, 2, 'a'])
        self.assertEqual(str(context.exception), "All elements in the list must be numbers.")

    # Tests for squared_error
    def test_squared_error_valid(self):
        self.assertEqual(squared_error(4, 2), 4)
        self.assertAlmostEqual(squared_error(2.5, 1.5), 1.0)

    def test_squared_error_invalid(self):
        with self.assertRaises(ValueError) as context:
            squared_error(4, "a")
        self.assertEqual(str(context.exception), "Both inputs must be numbers.")


if __name__ == '__main__':
    unittest.main()