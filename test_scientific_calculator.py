import unittest
import math
from scientific_calculator import sin, cos, tan, sqrt, log, exp

class TestScientificCalculator(unittest.TestCase):

    def test_sin(self):
        
        self.assertAlmostEqual(sin(90), 1, places=5)
        self.assertAlmostEqual(sin(-90), -1, places=5)
        self.assertAlmostEqual(sin(0), 0, places=5)
        with self.assertRaises(ValueError):
            sin("hello")

    def test_cos(self):
       
        self.assertAlmostEqual(cos(0), 1, places=5)
        self.assertAlmostEqual(cos(90), 0, places=5)
        self.assertAlmostEqual(cos(-90), 0, places=5)
        with self.assertRaises(ValueError):
            cos("world")

    def test_tan(self):
        
        self.assertAlmostEqual(tan(0), 0, places=5)
        self.assertAlmostEqual(tan(45), 1, places=5)
        self.assertAlmostEqual(tan(-45), -1, places=5)
        with self.assertRaises(ValueError):
            tan("python")

    def test_sqrt(self):
        
        self.assertAlmostEqual(sqrt(4), 2, places=5)
        self.assertAlmostEqual(sqrt(0), 0, places=5)
        with self.assertRaises(ValueError):
            sqrt(-4)
        with self.assertRaises(ValueError):
            sqrt("sqrt")

    def test_log(self):
        
        self.assertAlmostEqual(log(1), 0, places=5)
        self.assertAlmostEqual(log(math.e), 1, places=5)
        with self.assertRaises(ValueError):
            log(0)
        with self.assertRaises(ValueError):
            log(-1)
        with self.assertRaises(ValueError):
            log("logarithm")

    def test_exp(self):
        # Test cases for exp function
        self.assertAlmostEqual(exp(0), 1, places=5)
        self.assertAlmostEqual(exp(1), math.e, places=5)
        with self.assertRaises(ValueError):
            exp("exponential")

if __name__ == '__main__':
    unittest.main()
