n, k = map(int, input().strip().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [100001 for i in range(k + 1)]
dp[0] = 0

for coin in arr:
    for i in range(coin, k + 1):  # 현재 갖고 있는 동전 i를 기준으로 i 미만의 값은 갱신될리 없으므로 i부터 시작.
        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])


# import sys
# from itertools import combinations

# n = int(sys.stdin.readline())

# nums = list()  # 모든 감소하는 수
# for i in range(1, 11):  #  1~10개의 조합 만들기 (0~9개니깐)
#     for comb in combinations(range(0, 10), i):  # 0~9로 하나씩 조합 만들기
#         comb = list(comb)
#         comb.sort(reverse=True)  # 해당 조합을 감소하는 수로 변경
#         nums.append(int("".join(map(str, comb))))

# print(nums)
# nums.sort()  # 오름차순
# print(nums)

# try:
#     print(nums[n])
# except:  # 인덱스가 넘어가는 경우 -1 출력. 마지막 수 9876543210
#     print(-1)
