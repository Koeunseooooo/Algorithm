import sys

input = sys.stdin.readline

t = int(input())

arr = [int(input()) for _ in range(t)]

dp = [1] * (max(arr) + 1)


for j in range(2, 4):
    for i in range(1, len(dp)):
        if i >= j:
            dp[i] = dp[i] + dp[i - j]


for a in arr:
    print(dp[a])
