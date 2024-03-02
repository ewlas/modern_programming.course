import unittest
from fun import add, multiply, subtract


class MathTest(unittest.TestCase):
    def test_math(self):
        self.assertEqual(4, add(2, 2))
        self.assertEqual(3, subtract(6, 3))
        self.assertEqual(10, multiply(5, 2))

    def test_negative_number(self):
        self.assertEqual(1, add(-1, 2))
        self.assertEqual(0, subtract(-2, -2))

    def test_negative(self): 
        self.assertFalse(0, multiply(3, 2)) 
        self.assertFalse(2 == add(1, 3))


if __name__ == "__main__":
    unittest.main()