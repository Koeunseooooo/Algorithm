import sys

input = sys.stdin.readline

n = int(input())
arr = [(0, 0)]
for _ in range(n):
    t, p = map(int, input().strip().split())
    arr.append((t, p))

dp = [0] * (n + 1)

for i in range(len(dp)):
    t, p = arr[i]
    dp[i] = max(dp[i], dp[i - 1])
    if i + t - 1 <= n:
        dp[i + t - 1] = max(dp[i + t - 1], dp[i - 1] + p)

print(dp[-1])
