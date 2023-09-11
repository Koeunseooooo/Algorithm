import sys

input = sys.stdin.readline

n, s = map(int, input().strip().split())

arr = list(map(int, input().strip().split()))

cnt = 0


def backtracking(idx, sub_sum):
    global cnt
    if idx >= n:
        return

    sub_sum += arr[idx]

    if sub_sum == s:
        cnt += 1
    backtracking(idx + 1, sub_sum)
    backtracking(idx + 1, sub_sum - arr[idx])


backtracking(0, 0)

print(cnt)
# from itertools import combinations

# n, s = map(int, input().strip().split())

# arr = list(map(int, input().strip().split()))

# cnt = 0
# for n in range(1, len(arr) + 1):
#     for com in combinations(arr, n):
#         if sum(com) == s:
#             cnt += 1

# print(cnt)
