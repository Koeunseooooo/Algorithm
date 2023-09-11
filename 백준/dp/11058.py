import sys

input = sys.stdin.readline
n = int(input())
dp = [0] * (n + 1)

for i in range(1, 7):
    if i <= n:
        dp[i] = i

for i in range(7, n + 1):
    for j in range(3, i):
        if i - j > 0:
            dp[i] = max(dp[i], dp[i - j] * (j - 1))

print(dp[n])
