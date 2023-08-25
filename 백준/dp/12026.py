import sys

input = sys.stdin.readline

INF = 1e9
n = int(input())
blocks = list(input())
dp = [INF] * n
dp[0] = 0


def getPrev(x):
    if x == "O":
        return "B"
    elif x == "J":
        return "O"
    elif x == "B":
        return "J"


for i in range(1, n):
    for j in range(i):
        prev = getPrev(blocks[i])
        if blocks[j] == prev:
            dp[i] = min(dp[i], dp[j] + (j - i) * (j - i))

# print(dp)

if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])
