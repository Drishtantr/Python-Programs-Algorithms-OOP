#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    pdi=[]
    sdi=[]
    a=arr
    sa=0
    sb=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                pdi.append(arr[i][j])
    for i in range(len(arr)):
        for j in range(len(arr)):
            a[j][i]=a[i][j]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                sdi.append(a[i][j])
    
    for i in range(len(arr)):
            sa+=pdi[i]
            sb+=sdi[i]
    d=abs(sa-sb)
    return d
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
