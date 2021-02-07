def sum_nums(_a: int, _b: int):
    return _a + _b

def diff(_a: int, _b: int):
    return _a - _b

def prod(_a: int, _b: int):
    return _a * _b

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(sum_nums(a, b))
    print(diff(a, b))
    print(prod(a, b))

