import pytest
from RusPython.ImportTasks.div import division


def test_division_int():
    assert division(1, 1) == 1


def test_division_int_float():
    with pytest.raises(TypeError) as error:
        division(1, '1.0')

