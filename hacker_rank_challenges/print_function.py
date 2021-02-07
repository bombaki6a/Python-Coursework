def string(_n: int):
    s = ""

    for i in range(1, _n + 1):
        s += str(i)

    return s

if __name__ == '__main__':
    n = int(input())
    print(string(n))

