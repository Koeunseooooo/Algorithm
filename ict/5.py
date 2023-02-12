#!/bin/python3
import math
import os
import random
import re
import sys

from itertools import product


def findSchedules(workHours, dayHours, pattern):
    correct = 0
    repeat = 0
    for i in range(len(pattern)):
        cur = pattern[i]
        if cur == '?':
            repeat += 1
        elif cur != '0':
            correct += int(cur)
    workHours -= correct

    L = list(range(0, dayHours+1))
    cases = [list(nums) for nums in product(
        L, repeat=repeat) if sum(nums) == workHours]

    result = []
    for i in range(len(cases)):
        res = []
        for p in pattern:
            if p != '?':
                res.append(p)
            else:
                res.append(str(cases[i].pop(0)))
        result.append(''.join(res))
    return result


if __name__ == '__main__':
    workHours = int(input().strip())

    dayHours = int(input().strip())

    pattern = input()

    result = findSchedules(workHours, dayHours, pattern)
