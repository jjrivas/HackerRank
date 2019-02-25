if __name__ == '__main__':
    A = set(input().split())
    n = int(input())
    for _ in range(n):
        B = set(input().split())
        if(A.issuperset(B)):
            continue
        else:
            print(False)
            exit()
            
    
    print(True)