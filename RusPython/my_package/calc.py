def calculator(expression: str) -> float:
    allowed = '+-/*'
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'Выражение должно содержать хотя бы один из знаков {allowed}!')

    for sign in allowed:
        if sign in expression:
            try:
                left, right = [int(item.strip()) for item in expression.split(sign)]
                if sign == '+':
                    return left + right
                elif sign == '-':
                    return left - right
                elif sign == '/':
                    return left / right
                else:
                    return left * right
            except (ValueError, TypeError):
                raise ValueError('Выражение должно содержать 2 целых числа и 1 знак!')


if __name__ == '__main__':
    print(calculator('ф * 2'))






