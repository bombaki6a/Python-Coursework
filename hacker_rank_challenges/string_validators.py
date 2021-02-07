if __name__ == '__main__':
    s = input()

    num = False
    alpha = False
    digit = False
    low = False
    up = False

    for c in s:
        if c.isalnum():
            num = True
        if c.isalpha():
            alpha = True
        if c.isdigit():
            digit = True
        if c.islower():
            low = True
        if c.isupper():
            up = True

    print(num)
    print(alpha)
    print(digit)
    print(low)
    print(up)

