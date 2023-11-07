import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = [0] * (n + 1)  # 데이터 업데이트 할 때 원본 배열 과의 diff를 구할 때만 사용됨
tree = [0] * (n + 1)


def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= i & -i
    return result


def update(i, diff):
    while i < n + 1:
        tree[i] += diff
        i += i & -i


def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start - 1)  # -1 유의


for i in range(1, n + 1):
    x = int(input())
    arr[i] = x
    update(i, x)  # tree 배열 초기 업데이트

for i in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:  # 업데이트인 경우
        update(b, c - arr[b])
        arr[b] = c
    else:
        print(interval_sum(b, c))
