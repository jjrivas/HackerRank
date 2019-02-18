from collections import Counter

def merge_the_tools(string, k):
    l = ""

    for i in range(len(string)):
        if string[i] not in l:
            l += string[i]

        if (i +  1) % k == 0:
            print(l)
            l = ''

if __name__ == '__main__':
    string, k = input(), int(input())

    if(len(string) % k):
        exit("Invalid inpuit")

    merge_the_tools(string, k)