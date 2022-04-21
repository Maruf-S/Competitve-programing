#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
# []


def insertionSort1(n, arr): # Traverse from left to right
    for i in range(n):
        current = arr[i]
        j = i-1 # Compare to immediate left // Since we're traversing to the left
        while (j>=0 and arr[j]>current): # Till the first element 
            arr[j+1]= arr[j] # Shift the bigger element to the right
            j = j-1
            print(*arr)
    print(*arr)
