#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    count_array = [0]*100
    for i in arr:
        count_array[i] += 1
    
    # Store the cummulative count
    for i in range(1,100):
        count_array[i] += count_array[i-1]
    output_array = [0]*len(arr)

    for i in arr:
        output_array[count_array[i]-1] = i
    return count_array

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
