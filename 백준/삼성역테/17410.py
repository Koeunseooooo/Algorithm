import sys
from collections import defaultdict

input = sys.stdin.readline

r, c, k = map(int, input().strip().split())  # A[r][c]에 들어있는 값이 k가 될 때의 최소시간
r -= 1
c -= 1

arr = []
for _ in range(3):
    arr.append(list(map(int, input().strip().split())))


def rr(arr):
    new_arr = []
    for i in range(len(arr)):
        tar = arr[i]  # 각 행
        dic = defaultdict(int)  # count를 위한 딕셔너리 초기화
        for t in tar:
            if t != 0:
                dic[t] += 1
        li = list(dic.items())
        li.sort(key=lambda x: (x[1], x[0]))
        new = []
        for l in li:
            n, c = l
            new.append(n)
            new.append(c)
        new = new[:100]
        new_arr.append(new)
    max_r = max(map(len, new_arr))
    # 각 행을 가장 긴 열의 길이에 맞게 확장하고 부족한 부분을 0으로 채움
    arr = [row + [0] * (max_r - len(row)) for row in new_arr]
    return arr


t = 0
# max_r = 3
# max_c = 3

for t in range(101):
    if r < len(arr) and c < len(arr[0]):
        if arr[r][c] == k:
            print(t)
            exit()
    if len(arr) >= len(arr[0]):
        arr = rr(arr)
    else:
        _arr = list(map(list, zip(*arr)))
        __arr = rr(_arr)
        arr = list(map(list, zip(*__arr)))
    # for i in range(len(arr)):
    #     print(arr[i])

print(-1)
