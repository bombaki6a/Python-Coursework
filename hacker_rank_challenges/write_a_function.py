def is_leap(year):
    leap = False

    if not (year / 4) % 2:
        leap = True
    elif not (year / 400) % 2:
        leap = True

    return leap

year = int(input())
print(is_leap(year))

