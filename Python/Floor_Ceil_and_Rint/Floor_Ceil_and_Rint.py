import numpy

# floor() returns the floor of the input element-wise
# ceil() returns the ceiling of the input element-wise
# rint() rounds to the nearest integer of input element-wise

numpy.set_printoptions(sign=' ')

if __name__ == "__main__":

    numpy.set_printoptions(sign=' ')

    A = numpy.array(input().split(), float)
    print(numpy.floor(A))
    print(numpy.ceil(A))
    print(numpy.rint(A))