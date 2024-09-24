import unittest
import sys
# sys.path.append('C:/Users/am-user338/Desktop/Data_Olaf_Piltz/KW 39/Python_Unitest')
from KW_39.Python_Unitest.mmath_stuff import add_numbers


class TestAddNumbers(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -4), -6)

    def test_add_positive_and_negative_numbers(self):
        self.assertEqual(add_numbers(7, -3), 4)

    def test_add_float_numbers(self):
        self.assertAlmostEqual(add_numbers(2.5, 4.1), 6.6)

    def test_add_invalid_input(self):
        with self.assertRaises(TypeError):
            add_numbers(3, "a")

        with self.assertRaises(TypeError):
            add_numbers("a", "b")

        with self.assertRaises(TypeError):
            add_numbers([1, 2], 3)


if __name__ == '__main__':
    unittest.main()

#if __name__ == '__main__':
#    unittest.main(defaultTest='TestAddNumbers.test_add_invalid_input')
