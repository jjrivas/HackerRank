import numpy as np

np.set_printoptions(legacy='1.13')

if __name__ == "__main__":
    N, M = map(int, input().split())
    a = []
    for _ in range(N):
        a.append(np.array(input().split(), int))
    
    print(np.mean(a, axis = 1))
    print(np.var(a, axis = 0))
    print(np.std(a))