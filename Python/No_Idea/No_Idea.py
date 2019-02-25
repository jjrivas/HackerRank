def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    A, B = set(map(int, input().split())), set(map(int, input().split()))
    
    happiness = 0

    for i in arr:
        if(i in A):
            happiness += 1
        elif(i in B):
            happiness -= 1
        else:
            continue
    
    print(happiness)

if __name__ == '__main__':
    main()
    