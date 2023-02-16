#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxEnergy' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY mat as parameter.
#

# 이동할 3가지 방향 정의
dx = [1, 1, 1]
dy = [1, 0, -1]

case = []
visited = [[0]*4 for i in range(4)]


def valid(x):
    return 0 <= x < 4


def maxEnergy(mat):

    # Write your code here
    cost = -400
    for c1 in range(4):
        for c2 in [c1-1, c1, c1+1]:
            if not valid(c2):
                continue
            for c3 in [c2-1, c2, c2+1]:
                if not valid(c3):
                    continue
                for c4 in [c3-1, c3, c3+1]:
                    if not valid(c4):
                        continue
                    cost = max(cost, 100 - mat[0][c1] - mat[1][c2] -
                               mat[2][c3] - mat[3][c4])
    print(cost)
    return cost


if __name__ == '__main__':

    mat_rows = int(input().strip())
    mat_columns = int(input().strip())

    mat = []

    for _ in range(mat_rows):
        mat.append(list(map(int, input().rstrip().split())))

    result = maxEnergy(mat)
