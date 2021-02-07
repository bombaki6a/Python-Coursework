if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    list_of_elemnts = []

    for _x in range(x + 1):
        for _y in range(y + 1):
            for _z in range(z + 1):
                if (_x + _y + _z) != n:
                    list_of_elemnts.append([_x, _y, _z])

    print(list_of_elemnts)

