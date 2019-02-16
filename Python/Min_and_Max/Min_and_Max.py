import numpy as np


if __name__ == "__main__":
    N, M = map(int, input().split())
    A = np.array([input().split() for _ in range(N)], int)

    print(np.max(np.min(A, axis = 1)))
