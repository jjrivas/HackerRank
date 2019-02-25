def validateString(s):
    validators = [False] * 5

    for c in s:
        if(not validators[0] and c.isalnum()):
            validators[0] = True
        if(not validators[1] and c.isalpha()):
            validators[1] = True
        if(not validators[2] and c.isdigit()):
            validators[2] = True
        if(not validators[3] and c.islower()):
            validators[3] = True
        if(not validators[4] and c.isupper()):
            validators[4] = True

    for v in validators:
        print(v)


if __name__ == '__main__':
    s = input()
    validateString(s)

