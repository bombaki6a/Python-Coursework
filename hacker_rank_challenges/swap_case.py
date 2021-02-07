def swap_case(s):
    new_s = ''

    for c in s:
        if c.islower():
            new_s += c.upper()
        elif c.isupper():
            new_s += c.lower()
        else:
            new_s += c

    return new_s


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

