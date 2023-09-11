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
    fin_date = i + t - 1
    if fin_date <= n:
        dp[fin_date] = max(dp[fin_date], dp[i - 1] + p)

print(dp[n])
