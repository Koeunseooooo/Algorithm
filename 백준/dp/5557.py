import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)
n = int(input().strip())
arr = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(n)]
# dp[idx 번째][현재까지의 수] = 가능한 경우의 수

dp[0][arr[0]] += 1

for i in range(1, n - 1):
    for j in range(21):
        if dp[i - 1][j]:
            if j + arr[i] <= 20:
                dp[i][j + arr[i]] += dp[i - 1][j]
            if j - arr[i] >= 0:
                dp[i][j - arr[i]] += dp[i - 1][j]

print(dp[n - 2][arr[n - 1]])
