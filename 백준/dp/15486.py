import sys

input = sys.stdin.readline

n = int(input())
arr = []
arr.append((0, 0))
for _ in range(n):
    arr.append(tuple(map(int, input().split())))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    t, p = arr[i]
    dp[i] = max(dp[i], dp[i - 1])
    if i + t - 1 <= n:
        dp[i + t - 1] = max(dp[i + t - 1], dp[i - 1] + p)

print(dp[n])
