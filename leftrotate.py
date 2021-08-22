#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#


def rotateLeft(d, arr):
    for i in range(0, d):
        t = arr[0]
        for j in range(0, len(arr)-1):
            arr[j] = arr[j + 1]
        arr[len(arr)-1]=t
    print(arr)
    # for x in range(0,d):
    #     t=arr[0]
    #     for x in range(0,len(arr)-1):
    #         arr[x]=arr[x+1]
    #     arr[len(arr)-1]=t
    # return (arr)
    # if(d > len(arr)):
    #     d = d % len(arr)
    # t = arr[d-1]
    # #arr[0] = t
    # x=d
    # while x >=0:
    #     arr[x - 1] = arr[x - 2]
    #     x-=1
    # arr[d] = t
    # print(arr)
    # Write your code here



# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     d = int(first_multiple_input[1])

#     arr = list(map(int, input().rstrip().split()))
result = rotateLeft(10, [41, 73, 89, 7 , 10, 1, 59 , 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10 , 86 , 51])
#[1 ,2 ,3 ,4 ,5])
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
