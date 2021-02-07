def minion_game(_s: str):
    kevin_point = 0
    stuart_point = 0
    vowels = ['A', 'E', 'I', 'O', 'U']

    for i in range(len(_s)):
        if _s[i] in vowels:
            kevin_point += len(_s) - i
        else:
            stuart_point += len(_s) - i

        if stuart_point < kevin_point:
            print('Kevin', kevin_point)
        elif stuart_point > kevin_point:
            print('Stuart', stuart_point)
        else:
            print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)

