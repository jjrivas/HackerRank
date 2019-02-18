def main():
    l = list()
    n_cmds = int(input())

    for _ in range(n_cmds):
        c = input().split()
        cmd = c[0]
        if(cmd == "insert"):
            loc = int(c[1])
            val = int(c[2])
            l.insert(loc, val)
        elif(cmd == "remove"):
            val = int(c[1])
            try:
                l.remove(val)
            except:
                continue
        elif(cmd == "print"):
            print(l)
        elif(cmd == "append"):
            val = int(c[1])
            l.append(val)
        elif(cmd == "sort"):
            l.sort()
        elif(cmd == "pop"):
            l.pop()
        elif(cmd == "reverse"):
            l = l[::-1]

if __name__ == "__main__":
    main()

# Discussion Board Answer
# n = input()
# l = []

# for _ in range(n):
#     s = input().split()
#     cmd = s[0]
#     args = s[1:]
#     if cmd !="print":
#         cmd += "("+ ",".join(args) +")"
#         eval("l."+cmd)
#     else:
#         print l