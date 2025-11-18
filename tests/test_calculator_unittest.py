from unittest import TestCase, main
from RusPython.my_package.calc import calculator as calc


class Calculator(TestCase):
    def test_plus(self):
        self.assertEqual(calc('2+17'), 19)

    def test_minus(self):
        self.assertEqual(calc('7-5'), 2)

    def test_div(self):
        self.assertEqual(calc('12/3'), 4)

    def test_mul(self):
        self.assertEqual(calc('8*9'), 72)

    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calc('22')
        # проверка текста исключения. Не всегда обязательно
        self.assertEqual('Выражение должно содержать хотя бы один из знаков (+-/*)!', e.exception.args[0])

    def test_two_signs(self):
        with self.assertRaises(ValueError) as e:
            calc('2-2-2')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак!', e.exception.args[0])

    def test_many_signs(self):
        with self.assertRaises(ValueError) as e:
            calc('2-2*10')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак!', e.exception.args[0])

    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:
            calc('2.4*5.2')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак!', e.exception.args[0])

    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            calc('a+b')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак!', e.exception.args[0])
