def merge_the_tools(_string, _k):
    for i in range(0, len(_string), _k):
        string = ''
        for j in _string[i : i + _k]:
            if j not in string:
                string += j          
        print(string)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

