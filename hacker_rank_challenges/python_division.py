def int_deff(_a: int, _b: int):
    return _a // _b

def float_deff(_a: int, _b: int):
    return _a / _b


if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(int_deff(a, b))
    print(float_deff(a, b))

