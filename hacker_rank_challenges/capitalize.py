#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = s.split(' ')
    s = [c + ' ' if len(c) > 0 else ' ' for c in s]
    s = [c.lower() for c in s if len(c) > 0]
    s = [c[0].upper() + c[1:] for c in s if len(c) > 0]
    return ''.join(s)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

