import numpy


if __name__ == "__main__":
    a = input().split()
    a = numpy.array(a, int)
    print(numpy.reshape(a, (3, 3)))
    print(a.shape)