from second.utils import mul


def calc(a, b):
    try:
        a = mul(a, b)
    except TypeError:
        return 'Bad data!'
    return a + b


if __name__ == '__main__':
    assert calc(3, 4) == 16
    assert calc(0, 4) == 4
    assert calc(0, 0) == 0
    assert calc(4, 0) == 0
    assert calc(-3, 4) == -8
    assert calc(-3, -4) == 8
    assert calc(3, -4) == -16
    assert calc(3.0, -4) == -16.0
    assert calc(-3.0, 4) == -8.0
    assert calc(-3.0, -4.0) == 8.0
    assert calc(3.0, 4.0) == 16.0
    assert calc('a', 'b') == 'Bad data!'
