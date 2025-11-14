import pytest
from RusPython.my_package.calc import calculator


def test_plus():
    assert calculator('2+2') == 4


def test_minus():
    assert calculator('4-2') == 2


def test_division():
    assert calculator('3/3') == 1


def test_no_signs():
    with pytest.raises(ValueError) as e:
        calculator('222')
    assert 'Выражение должно содержать хотя бы один из знаков (+-/*)!' == e.value.args[0]


def test_two_signs():
    with pytest.raises(ValueError) as e:
        calculator('2+2+2')
    assert 'Выражение должно содержать 2 целых числа и 1 знак!' == e.value.args[0]


def test_two_signs_near():
    with pytest.raises(ValueError) as e:
        calculator('2--2')
    assert 'Выражение должно содержать 2 целых числа и 1 знак!' == e.value.args[0]


if __name__ == '__main__':
    pytest.main()
