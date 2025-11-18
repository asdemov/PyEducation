from unittest import TestCase, main
from RusPython.my_package.calc import calculator as calc


class Calculator(TestCase):
    def test_plus(self):
        self.assertEqual(calc('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calc('2-2'), 0)

    def test_div(self):
        self.assertEqual(calc('5/2'), 2.5)

    def test_mul(self):
        self.assertEqual(calc('2*4'), 8)


if __name__ == '__main__':
    main()
