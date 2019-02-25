if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        _, A = int(input()), set(map(int, input().split()))
        _, B = int(input()), set(map(int, input().split()))
        print(A.issubset(B))