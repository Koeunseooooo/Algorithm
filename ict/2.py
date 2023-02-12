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


def maxEnergy(mat):
    min = -500

    def dfs(x, y, stack, visited, energy):
        print(x, y)
        energy = max(min, energy-mat[x][y])

        for i in range(3):
            tmp_x = x+dx[i]
            tmp_y = y+dy[i]
            if tmp_x < 0 or tmp_x >= 4 or tmp_y < 0 or tmp_y >= 4:
                continue
            dfs(tmp_x, tmp_y, stack, visited, energy)

        return energy

    for i in range(4):
        dfs(0, i, [], visited, 100)
        print("___")


if __name__ == '__main__':

    mat_rows = int(input().strip())
    mat_columns = int(input().strip())

    mat = []

    for _ in range(mat_rows):
        mat.append(list(map(int, input().rstrip().split())))

    result = maxEnergy(mat)
