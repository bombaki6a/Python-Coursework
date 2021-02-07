def print_formatted(number):
    len_b = len(str('{:b}'.format(number)))
    st = '{i:{s}d}{i:{s_plus}o}{i:{s_plus}X}{i:{s_plus}b}'

    for i in range(1, number + 1):
        print(st.format(i=i, s=len_b, s_plus=len_b + 1))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

