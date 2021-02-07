#!/bin/python3

def even_or_odd(_n: int):
    return n % 2


if __name__ == '__main__':
    n = int(input())
    w_or_not = str

    if not even_or_odd(n):
        if (n >= 2) and (n <= 5):
            w_or_not = "Not Weird"
        elif (n >= 6) and (n <= 20):
            w_or_not = "Weird"
        else:
            w_or_not = "Not Weird"
        else:
            w_or_not = "Weird"

        print(w_or_not)

