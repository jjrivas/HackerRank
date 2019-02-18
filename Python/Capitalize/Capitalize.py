#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    l = ''
    prior_space = True

    for x in s:
        if(prior_space and x.isalpha()):
            l += x.upper()
            prior_space = False

        elif(x.isspace()):
            prior_space = True
            l += x
            
        else:
            prior_space = False
            l += x

    return l

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)

    #fptr.write(result + '\n')

    #fptr.close()
