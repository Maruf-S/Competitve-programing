#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(array):
    length = len(array)
    swaps = 0
    for i in range(length):
        #check if sorted
        sorted = False
        for j in range(length-1):
            if(array[j]>array[j+1]):
                array[j], array[j + 1] = array[j + 1], array[j]
                swaps+=1
    print(f'Array is sorted in {swaps} swaps.')
    print(f'First Element: {array[0]}')
    print(f'Last Element: {array[length-1]}')

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
