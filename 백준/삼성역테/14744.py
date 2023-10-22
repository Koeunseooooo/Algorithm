import sys

input = sys.stdin.readline

r, c, t = map(int, input().strip().split())
arr = []
for _ in range(r):
    arr.append(list(map(int, input().strip().split())))

cur_t = 0
d = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 상 우 하 좌 (반시계)
robot = []
for i in range(r):
    for j in range(c):
        if arr[i][j] == -1:
            robot.append((i, j))


def diff(y, x, diff_arr):
    cnt = 0  # 확산된 방향의 개수
    for dy, dx in d:
        Y = y + dy
        X = x + dx
        if 0 <= Y < r and 0 <= X < c and arr[Y][X] != -1:
            dust = arr[y][x] // 5
            diff_arr[Y][X] += dust
            cnt += 1
    arr[y][x] -= (arr[y][x] // 5) * cnt


def air_up(arr):
    d = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 우 상 좌 하
    d_idx = 0
    y, x = robot[0]
    x += 1
    up = y
    prev = 0  # 일종의 버퍼 변수라고 생각
    while 1:
        dy, dx = d[d_idx]
        Y = y + dy
        X = x + dx
        if x == 0 and y == up:  # 원점으로 돌아옴
            break
        if 0 <= Y < r and 0 <= X < c:
            arr[y][x], prev = prev, arr[y][x]
            y, x = Y, X
        else:
            d_idx += 1


def air_down(arr):
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우 하 좌 상
    d_idx = 0
    y, x = robot[1]
    down = y
    x += 1
    prev = 0  # 일종의 버퍼 변수라고 생각
    while 1:
        dy, dx = d[d_idx]
        Y = y + dy
        X = x + dx
        if x == 0 and y == down:  # 원점으로 돌아옴
            break
        if 0 <= Y < r and 0 <= X < c:
            arr[y][x], prev = prev, arr[y][x]
            y, x = Y, X
        else:
            d_idx += 1


while 1:
    if cur_t == t:
        break
    diff_arr = [[0] * c for _ in range(r)]
    # 1. 미세먼지가 확산된다.
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                diff(i, j, diff_arr)
    for i in range(r):
        for j in range(c):
            if diff_arr[i][j] != 0:
                arr[i][j] += diff_arr[i][j]
    # 2. 공기청정기가 작동한다.
    air_up(arr)
    air_down(arr)
    cur_t += 1


answer = 0
for i in range(r):
    answer += sum(arr[i])
print(answer + 2)
