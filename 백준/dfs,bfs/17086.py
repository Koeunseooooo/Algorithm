import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

shark = deque()
for i in range(n):
    temp = list(map(int, input().split()))
    for t in range(m):
        if temp[t] == 1:
            shark.append((i, t))
    arr.append(temp)

mx = [-1, -1, -1, 0, 1, 0, 1, 1]
my = [-1, 0, 1, 1, 1, -1, 0, -1]


def bfs():
    while shark:
        x, y = shark.popleft()
        for k in range(8):
            dx = x + mx[k]
            dy = y + my[k]
            if 0 <= dx < n and 0 <= dy < m:
                if arr[dx][dy] == 0:
                    shark.append((dx, dy))
                    arr[dx][dy] = arr[x][y] + 1
    return


bfs()
safe_dist = 0
for i in range(n):
    for j in range(m):
        safe_dist = max(safe_dist, arr[i][j])

print(safe_dist - 1)
# """
# 내 풀이
# 각 원소 기준으로 bfs풀이
# 3초 걸림
# """
# import sys
# from collections import deque

# input = sys.stdin.readline

# n, m = map(int, input().strip().split())

# arr = [list(map(int, input().split())) for _ in range(n)]


# # 인접 방향(대각선 포함)
# d = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]


# def bfs(y, x):
#     q = deque()
#     q.append((y, x))
#     visited = [[0] * m for _ in range(n)]
#     isShark = 0  # flag
#     while q:
#         y, x = q.popleft()
#         for dy, dx in d:
#             Y = y + dy
#             X = x + dx
#             if 0 <= X < m and 0 <= Y < n and visited[Y][X] == 0:
#                 if arr[Y][X] == 0:
#                     q.append((Y, X))
#                     visited[Y][X] = visited[y][x] + 1
#                 else:
#                     ans = visited[y][x] + 1
#                     isShark = 1
#         if isShark:
#             break

#     return ans


# ans = 0
# for y in range(n):
#     for x in range(m):
#         if arr[y][x] != 1:
#             if ans < bfs(y, x):
#                 ans = bfs(y, x)

# print(ans)

# """
# 다른 사람 풀이
# 상어 기준으로 bfs풀이
# 0.076초 걸림
# """
# from collections import deque

# n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]

# # 8가지 이동방향
# d = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
# q = deque()


# def bfs():
#     while q:
#         x, y = q.popleft()
#         for dx, dy in d:
#             nx = x + dx
#             ny = y + dy
#             # 맵에서 벗어나는 경우
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue

#             # 상어가 없는 지점 or 미탐색 지점인지 확인
#             if not graph[nx][ny]:
#                 # 새로운 지점의 거리 정보 업데이트
#                 graph[nx][ny] = graph[x][y] + 1
#                 # 새로운 지점의 좌표를 큐에 삽입
#                 q.append((nx, ny))


# # 상어의 위치에서부터 탐색 시작
# for i in range(n):
#     for j in range(m):
#         # 상어 위치일 경우
#         if graph[i][j]:
#             # 상어 위치를 큐에 삽입
#             q.append((i, j))

# bfs()

# # 정답 출력
# print(max(map(max, graph)) - 1)


"""시간 더 걸림
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().strip().split())

arr = [list(map(int, input().split())) for _ in range(n)]


# 인접 방향(대각선 포함)
d = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]


def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited = [[0] * m for _ in range(n)]
    isShark = 0  # flag
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            Y = y + dy
            X = x + dx
            if 0 <= X < m and 0 <= Y < n and visited[Y][X] == 0:
                if arr[Y][X] == 0:
                    q.append((Y, X))
                    visited[Y][X] = visited[y][x] + 1
                else:
                    ans = visited[y][x] + 1
                    isShark = 1
        if isShark:
            break

    return ans


ans = 0
for y in range(n):
    for x in range(m):
        if arr[y][x] != 1:
            if ans < bfs(y, x):
                ans = bfs(y, x)

print(ans)
"""
