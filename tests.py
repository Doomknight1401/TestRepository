import unittest
import main

class TestCalc(unittest.TestCase):

    def test_AddNumbers(self):
        self.assertEqual(main.Add(5, 8, 2), 15)
        self.assertEqual(main.Add(-1, 1), 0)
        self.assertEqual(main.Add(-1, -1), -2)

    def test_SubtractNumbers(self):
        self.assertEqual(main.Subtract(5, 10), -5)

    def test_DivideNumbers(self):
        self.assertEqual(main.Divide(10, 2), 5)

        with self.assertRaises(ValueError):
            main.Divide(5, 0)

    def test_MultiplyNumbers(self):
        self.assertEqual(main.Multiply(5, 10), 50)
        self.assertEqual(main.Multiply(64, 0), 0)

if __name__ == '__main__':
    unittest.main()