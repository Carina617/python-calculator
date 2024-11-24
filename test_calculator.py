import unittest
import calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, -3), -5)
    
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-5, -3), -2)
    
    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(multiply(-4, -3), 12)
    
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
    
    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)
        with self.assertRaises(ZeroDivisionError):
            modulo(10, 0)

if __name__ == "__main__":
    unittest.main()
