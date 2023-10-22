#!/bin/python3
import math
import os
import random
import re
import sys


from collections import Counter


def numWays(words, target):
    dp = [0 for _ in range(len(target) + 1)]
    dp[0] = 1
    for i in range(len(words[0])):
        voca_count = Counter(w[i] for w in words)
        for j in range(len(target)-1, -1, -1):
            print(target[j])
            dp[j+1] += dp[j] * voca_count[target[j]]
            print(dp)

    return dp[-1] % (10**9 + 7)


if __name__ == '__main__':

    words_count = int(input().strip())

    words = []

    for _ in range(words_count):
        words_item = input()
        words.append(words_item)

    target = input()

    result = numWays(words, target)
