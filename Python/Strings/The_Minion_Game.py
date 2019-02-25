def minion_game(string):
    vowels = 'AEIOU'
    stuart = 0
    kevin = 0

    for i in range(len(string)):
        if(s[i] in vowels):
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    if(kevin == stuart):
        print("Draw")
    elif(stuart > kevin):
        print('Stuart', stuart)
    else:
        print('Kevin', kevin)




if __name__ == '__main__':
    s = input()
    minion_game(s)