def division(a, b):
    try:
        return int(a / b)
    except TypeError as e:
        print(e)
