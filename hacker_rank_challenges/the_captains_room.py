k = int(input())
room_list = list(map(int, input().split(' ')))

room_set = set(room_list)
captain = ((sum(room_set) * k) - (sum(room_list))) // (k - 1)

print(captain)

