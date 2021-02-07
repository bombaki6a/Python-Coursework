x = int(input())
shoes_list = list(map(int, input().split(' ')))

n = int(input())
price = 0

for i in range(n):
    size_price = list(map(int, input().split(' ')))
    if size_price[0] in shoes_list:
        price += size_price[1]
        shoes_list.remove(size_price[0])

print(price)

