print(bin(1 << 20))

a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a[:-5])

print("3" * 2)

import sys

input = sys.stdin.readline

n = int(input())

# 계단의 숫자를 초기화 합니다. 1층은 1번째(not 0번째) 인덱스에 저장합니다.
stairs = [0] * 301
for i in range(n):
    stairs[i] = int(input())

# dp 배열을 초기화합니다.
dp = [0] * 301
dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

# 점화식을 계산합니다.
for i in range(3, n):
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

print(dp[n - 1])
