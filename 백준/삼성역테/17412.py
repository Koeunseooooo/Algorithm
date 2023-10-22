import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().strip().split())
wall_cnt = 0
arr = []
for _ in range(n):
    arr.append(list(map(int, input().strip().split())))

v = []
# 0은 빈 칸, 1은 벽, 2는 비활성 바이러스의 위치
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            wall_cnt += 1
        if arr[i][j] == 2:  # 비활성화 바이러스라면
            v.append((i, j))


d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
MAX = 1e9


def bfs(cur_arr):
    q = deque()
    visited = [[-1] * n for _ in range(n)]
    for c in cur_arr:
        y, x = c
        q.append((y, x))
        visited[y][x] = 0
    result = 0
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            Y = dy + y
            X = dx + x
            if 0 <= Y < n and 0 <= X < n:
                if visited[Y][X] == -1 and arr[Y][X] != 1:
                    visited[Y][X] = visited[y][x] + 1
                    q.append((Y, X))
                    if arr[Y][X] == 0:
                        result = max(result, visited[Y][X])
    # 비활성화 바이러스가 있는 지 확인
    if list(sum(visited, [])).count(-1) != wall_cnt:
        return MAX
    return result


ans = MAX


def combinations(cur_arr, cur_idx):
    global ans
    if len(cur_arr) == m:
        ans = min(ans, bfs(cur_arr))
    for next_idx in range(cur_idx, len(v)):
        combinations(cur_arr + [v[next_idx]], next_idx + 1)


if list(sum(arr, [])).count(0) == 0:
    print(0)
    exit()
combinations([], 0)
if ans == MAX:
    print(-1)
else:
    print(ans)

# a = [[1, 2, 3], [2, 3, 4], [5, 6, 7]]
# result = [element for sublist in a for element in sublist]
# print(result)

# sum(visited, []) <- itertools 대신 간단하게 2차원 배열을 1차원 배열로 바꾸는 방법임
