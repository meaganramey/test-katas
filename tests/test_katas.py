import unittest
import random
import importlib

PKG_NAME = 'katas'


class TestKatas(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Performs module import when tests are ran."""
        cls.module = importlib.import_module(PKG_NAME)

    def setUp(self):
        self.a = random.randint(1, 100)
        self.b = random.randint(1, 100)
        self.c = random.randint(1, 100)
        self.d = random.randint(1, 100)
        self.e = random.randint(-100, -1)
        self.f = random.randint(-100, -1)
        self.g = random.randint(1, 100) + random.random()
        self.h = random.randint(1, 100) + random.random()
        self.i = random.random()

    def test_add(self):
        """Check if add function is working"""
        add = self.module.add
        self.assertEqual(add(self.a, self.b), self.a+self.b)  # pass
        self.assertEqual(add(self.c, self.d), self.c+self.d)  # pass
        self.assertEqual(add(self.e, self.f), self.e+self.f)  # pass neg
        self.assertEqual(add(self.g, self.h), self.g+self.h)  # pass float

    def test_multiply(self):
        """Check if multiply function is working"""
        multiply = self.module.multiply
        self.assertEqual(multiply(self.a, self.b), self.a*self.b)  # pass
        self.assertEqual(multiply(self.c, self.d), self.c*self.d)  # pass
        self.assertEqual(multiply(self.e, self.f), self.e*self.f)  # pass neg
        self.assertAlmostEqual(multiply(self.g, self.d),
                               self.g*self.d, places=2)  # pass float

    def test_power(self):
        """Check if power function is working"""
        power = self.module.power
        self.assertEqual(power(self.a, self.b), self.a**self.b)  # pass
        self.assertEqual(power(self.c, self.d), self.c**self.d)  # pass
        self.assertEqual(power(self.e, self.b), self.e**self.b)  # pass neg
        self.assertRaises(ValueError, power, self.c, self.e)  # pass n < 0
        self.assertRaises(ValueError, power, self.c, self.i)  # pass 0 < n < 1

    def test_factorial(self):
        """Check if factorial function is working"""
        fac_list = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800,
                    39916800, 479001600, 6227020800, 87178291200,
                    1307674368000]
        factorial = self.module.factorial
        self.assertEqual(factorial(0), fac_list[0])  # pass
        self.assertEqual(factorial(5), fac_list[5])  # pass
        self.assertEqual(factorial(10), fac_list[10])  # pass
        self.assertRaises(ValueError, factorial, -1)  # pass
        self.assertRaises(ValueError, factorial, -100)

    def test_fibonacci(self):
        """Check if fibonacci function is working"""
        choice = random.randrange(0, 30)
        fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,
                    610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657,
                    46368, 75025, 121393, 196418, 317811, 514229, 832040]
        fibonacci = self.module.fibonacci
        self.assertEqual(fibonacci(0), fib_list[0])  # pass
        self.assertEqual(fibonacci(14), fib_list[14])  # pass
        self.assertEqual(fibonacci(choice), fib_list[choice])  # pass
        self.assertRaises(ValueError, fibonacci, -choice)


if __name__ == '__main__':
    unittest.main()
