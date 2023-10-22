# 백트래킹 다시 공부해
# 순열 permutations 순서 상관 있음

array = [1, 2, 3, 4, 5]
k = 2
used = [0 for i in range(len(array))]


def permutations(arr):
    if len(arr) == k:
        return arr
    for i in range(len(array)):
        if not used[i]:
            used[i] = 1
            permutations(used[i] + arr)
            used[i] = 0
