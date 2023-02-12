#!/bin/python3
import math
import os
import random
import re
import sys

from collections import defaultdict


def deleteProducts(ids, m):
    d = defaultdict(int)
    for _id in ids:
        d[_id] += 1
    c = sorted(d.values())
    for i in range(len(c)):
        if c[i] > 0 and m > 0:
            if c[i] >= m:
                c[i] -= m
                m = 0
            else:
                m -= c[i]
                c[i] = 0
    ans = len([_ for i in c if i != 0])
    return ans


if __name__ == '__main__':
    ids_count = int(input().strip())

    ids = []

    for _ in range(ids_count):
        ids_item = int(input().strip())
        ids.append(ids_item)

    m = int(input().strip())

    result = deleteProducts(ids, m)
