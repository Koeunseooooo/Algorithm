# 6
# 10
# 20
# 15
# 25
# 10
# 20
import sys

input = sys.stdin.readline
n = int(input())
stairs = [0] * 300
for i in range(n):
    stairs[i] = int(input())

dp = [0] * 300  # 이렇게 하면 n이 2 이하일 경우 아래 구문들에서 인덱스 에러남

dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]  # 사실 이건 당연히 전자로 선택되게 됨
dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for i in range(3, n):
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

print(dp[n - 1])
