import pytest
from RusPython.ImportTasks.div import division


def test_division_int():
    assert division() == 1
