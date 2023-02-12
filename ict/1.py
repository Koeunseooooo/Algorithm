#!/bin/python3
import math
import os
import random
import re
import sys

from collections import defaultdict


def getGroupedAnagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        anagrams[''.join(sorted(word))].append(word)
    return len(anagrams)


if __name__ == '__main__':

    words_count = int(input().strip())

    words = []

    for _ in range(words_count):
        words_item = input()
        words.append(words_item)

    result = getGroupedAnagrams(words)
