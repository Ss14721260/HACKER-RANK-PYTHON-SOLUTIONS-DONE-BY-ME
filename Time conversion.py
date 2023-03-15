#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s[8:10]=='PM':
        x=int(s[0:2])
        if int(s[0:2])!=12:
            x=int(s[0:2])+12
        return str(x)+s[2:len(s)-2]
    else:
        x=int(s[0:2])
        if x==12:
            return str('00')+s[2:8]
        else:
            return s[0:8]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
    print("hello frinends")
#hello friends i am facing some issue in uploading this moment of time.
