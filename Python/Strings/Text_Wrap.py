import textwrap

def wrap(s, w):
    t = textwrap.wrap(s, w)
    t = "\n".join(t)
    return t

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)