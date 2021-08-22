#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def hourglassSum(arr):
    sum = 0
    max_sum = -63
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr) - 1):
            print(arr[i][j])
            sum += arr[i-1][j-1]
            sum += arr[i-1][j]
            sum += arr[i-1][j+1]
            sum += arr[i][j]
            sum += arr[i+1][j-1]
            sum += arr[i+1][j]
            sum += arr[i+1][j+1]
            if sum > max_sum:
                max_sum = sum
            sum=0
    return max_sum


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     arr = []

#     for _ in range(6):
#         arr.append(list(map(int, input().rstrip().split())))
arr=[[1, 1 ,1 ,0, 0, 0],[
0 ,1, 0 ,0 ,0, 0],[
1 ,1 ,1 ,0 ,0 ,0],[
0 ,0 ,2 ,4 ,4 ,0],[
0 ,0 ,0 ,2 ,0 ,0],[
0, 0, 1, 2, 4, 0]]

arr1 = [[1, 1, 1, 0, 0, 0 ],
        [0 ,1, 0, 0, 0, 0 ],
        [1, 1 ,1 ,0, 0, 0 ],
        [0 ,9 ,2 ,- 4 ,- 4 ,0 ],
        [0 ,0 ,0 ,- 2 ,0 ,0 ],
        [0 ,0 ,- 1 ,- 2 ,- 4 ,0]]
result = hourglassSum(arr1)

    #fptr.write(str(result) + '\n')

    #fptr.close()
