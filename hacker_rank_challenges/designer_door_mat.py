x, y = map(int, input().split())
pr = 1

welcome = (('-' * ((y - 7) // 2)) + ('WELCOME') + ('-' * ((y - 7) // 2)))

for _ in range(x // 2):
    sl = '-' * ((y - (pr * 3)) // 2)
    print(sl + ('.|.' * pr) + sl)
    pr += 2

print(welcome)

for _ in range((x // 2), 0, -1):
    pr -= 2
    sl = '-' * ((y - (pr * 3)) // 2)
    print(sl + ('.|.' * pr) + sl)

