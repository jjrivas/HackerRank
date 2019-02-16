import numpy as np

# transpose reverses the axes
if __name__ == "__main__":
    N, M = map(int, input().split())
    A = np.array([input().split() for _ in range(N)], int)
    print(np.transpose(A))
    print(A.flatten())