if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)
    for i in arr:
        if i < arr[0]:
            print(i)
            break

