import string


def password_strength(user_password: str) -> str:
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = lowers.upper()

    if len(user_password) < 8:
        return 'Too Weak'
    if all(e in digits for e in user_password) or all(e in lowers for e in user_password) \
            or all(e in uppers for e in user_password):
        return 'Weak'
    if any(e in digits for e in user_password) and any(e in lowers for e in user_password) \
            and any(e in uppers for e in user_password):
        return 'Very good'

    if (any(e in digits for e in user_password) and any(e in lowers for e in user_password)) or \
            (any(e in digits for e in user_password) and any(e in uppers for e in user_password)) or \
            (any(e in uppers for e in user_password) and any(e in lowers for e in user_password)):
        return 'Good'

    return ''


if __name__ == '__main__':
    assert password_strength('') == 'Too Weak'
    assert password_strength('1234567') == 'Too Weak'
    assert password_strength('abcdefg') == 'Too Weak'
    assert password_strength('ABCDEFG') == 'Too Weak'
    assert password_strength('qqAA123') == 'Too Weak'
    assert password_strength('12345678') == 'Weak'
    assert password_strength('1234567891111234') == 'Weak'
    assert password_strength('abcdefgj') == 'Weak'
    assert password_strength('abcdefgjasderf') == 'Weak'
    assert password_strength('ABCDEFGJ') == 'Weak'
    assert password_strength('ABCDEFGJJKUU') == 'Weak'
    assert password_strength('qqqq1234') == 'Good'
    assert password_strength('qqqq1234rty') == 'Good'
    assert password_strength('QQQQ1234') == 'Good'
    assert password_strength('QQQQ1234YYYYU') == 'Good'
    assert password_strength('QQQQabcd') == 'Good'
    assert password_strength('QQQQabcdAFde') == 'Good'
    assert password_strength('QQQ1abcd') == 'Very Good'
    assert password_strength('QQQQWQQQq') == 'Very Good'
    assert password_strength('qqqqqqqWq') == 'Very Good'
    assert password_strength('123456WW1') == 'Very Good'
    assert password_strength('123456ww2') == 'Very Good'
