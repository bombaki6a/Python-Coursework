import textwrap

def wrap(string, max_width):
    w = textwrap.TextWrapper(max_width)
    return '\n'.join(w.wrap(text=string))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
