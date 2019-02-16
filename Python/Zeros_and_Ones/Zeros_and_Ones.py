import numpy as np

if __name__ == "__main__":
    dims = list(map(int, input().split()))

    print(np.zeros((dims), dtype = np.int16))
    print(np.ones((dims), dtype = np.int16))