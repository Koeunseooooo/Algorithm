import sys
from collections import defaultdict

input = sys.stdin.readline
t = int(input().strip())

for _ in range(t):
    res = 1
    n = int(input().strip())
    # clothes = {}
    clothes = defaultdict(int)
    for _ in range(n):
        _, case = input().strip().split()
        clothes[case] += 1
    for v in clothes.values():
        res *= v + 1
    print(res - 1)
