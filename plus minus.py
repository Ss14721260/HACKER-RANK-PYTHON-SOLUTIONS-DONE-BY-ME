#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    x=y=z=0
    l=len(arr)
    for i in arr:
        if i>0:
            x+=1
        elif i<0:
            y+=1
        else:
            z+=1
    print(x/l)
    print(y/l)
    print(z/l)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
