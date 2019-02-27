# Polar coordinates are an alternative way of representing Cartesian
# coordinates or Complex Numbers
# A complex number z: z = x + yj
import cmath

if __name__ == '__main__':
    print(*cmath.polar(complex(input())), sep='\n')
    