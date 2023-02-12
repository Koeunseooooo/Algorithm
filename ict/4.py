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
        # tar의 문자를 뒤에서부터 앞으로 접근하면서 매칭되는 voca가 있는 지 확인
        for j in range(len(target)-1, -1, -1):
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
