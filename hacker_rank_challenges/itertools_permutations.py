from itertools import permutations

s = input().split(' ')
r = 0

if len(s) < 2:
    r += len(s[0])
else:
    r += int(s[1])

per = list(permutations(s[0], r))
per = sorted([''.join(char) for char in [word for word in per]])

[print(word) for word in per]

