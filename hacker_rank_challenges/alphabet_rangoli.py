def print_rangoli(size):
    off_size = (((size - 1) + size) * 2) - 1

    if size > 1:
        for i in range(size - 1):
            str1 = '-'.join(chr(ord('a') + size - 1 - j) for j in range(i))
            str2 = '-'.join(reversed([chr(ord('a') + size - 1 - j) for j in range(i + 1)]))
            print('{s:-^{si}}'.format(s = '-'.join([str1, str2]), si = off_size))

        for i in range(size - 1, -1, -1):
            str1 = '-'.join(chr(ord('a') + size - 1 - j) for j in range(i))
            str2 = '-'.join(reversed([chr(ord('a') + size - 1 - j) for j in range(i + 1)]))
            print('{s:-^{si}}'.format(s = '-'.join([str1, str2]), si = off_size))
    else:
        print('a')


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

