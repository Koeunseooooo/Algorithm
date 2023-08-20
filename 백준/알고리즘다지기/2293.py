n, k = map(int, input().strip().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [0 for i in range(k + 1)]
dp[0] = 1

for i in arr:
    for j in range(i, k + 1):  # 현재 갖고 있는 동전 i를 기준으로 i 미만의 값은 갱신될리 없으므로 i부터 시작.
        dp[j] += dp[j - i]

print(dp[k])
