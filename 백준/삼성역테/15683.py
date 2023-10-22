import sys
import copy

input = sys.stdin.readline


n, m = map(int, input().strip().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().strip().split())))
cctv = []
wall = []
for i in range(n):
    for j in range(m):
        if arr[i][j] in range(1, 6):
            cctv.append([arr[i][j], i, j])

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
# mode : cctv 종류별 바라볼 수 있는 방향의 경우의 수에 대한 리스트
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 3], [1, 3], [1, 2], [0, 2]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]


def fill(y, x, _m, arr):
    for d_idx in _m:
        dy, dx = d[d_idx]
        Y = y + dy
        X = x + dx
        while 1:
            if 0 <= Y < n and 0 <= X < m:
                if arr[Y][X] == 6:
                    break
                elif arr[Y][X] == 0:
                    arr[Y][X] = 1
                    Y += dy
                    X += dx
                else:  # 다른 cctv거나 이미 감시된 칸
                    Y += dy
                    X += dx
                    continue
            else:
                break


def dfs(depth, arr):  # depth: cctv idx, arr: 현재 arr
    global min_value
    if depth == len(cctv):
        count = 0
        for i in range(n):
            count += arr[i].count(0)
        min_value = min(min_value, count)
        return
    temp = copy.deepcopy(arr)
    cctvNum, y, x = cctv[depth]

    for m in mode[cctvNum]:
        fill(y, x, m, temp)  # 채워넣고
        dfs(depth + 1, temp)  # dfs끝나면
        temp = copy.deepcopy(arr)  # 다시원래대로


min_value = int(1e9)
dfs(0, arr)
print(min_value)
