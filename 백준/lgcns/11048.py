""" bfs (정답)
import sys

input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))

score = [[-1 for i in range(m)] for j in range(n)]
score[0][0] = mat[0][0]

dx = [1, 0]
dy = [0, 1]


def bfs(y, x):
    q = deque()
    q.append([y, x])
    while q:
        y, x = q.popleft()
        for i in range(2):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < m and 0 <= ny < n:
                if score[ny][nx] < score[y][x] + mat[ny][nx]:
                    score[ny][nx] = score[y][x] + mat[ny][nx]
                    q.append([ny, nx])


bfs(0, 0)
print(score[-1][-1])
"""

# # dfs (정답)
# import sys

# input = sys.stdin.readline
# from collections import deque

# n, m = map(int, input().split())

# board = []
# for i in range(n):
#     board.append(list(map(int, input().split())))

# dp = [[-1 for i in range(m)] for j in range(n)]
# d = [(0, 1), (1, 0), (1, 1)]


# def dfs(y, x):
#     if y == n - 1 and x == m - 1:
#         return dp[y][x]
#     if dp[y][x] == -1:
#         res = board[y][x]
#     else:
#         res = dp[y][x]
#     for dy, dx in d:
#         Y = y + dy
#         X = x + dx
#         if 0 <= Y < n and 0 <= X < m:
#             dp[Y][X] = max(dfs(Y, X) + board[y][x], dp[Y][X])
#     return res


# dfs(0, 0)
# print(dp[-1][-1])


"""dp (1)

import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())
board = []

for _ in range(n):
    board.append(list(map(int, input().strip().split())))


def check_range(y, x):
    return 0 <= y < n and 0 <= x < m


dp = [[0] * m for _ in range(n)]
dp[0][0] = board[0][0]
d = [(0, -1), (-1, 0), (-1, -1)]
for y in range(n):
    for x in range(m):
        for dy, dx in d:
            if check_range(y + dy, x + dx):
                dp[y][x] = max(dp[y][x], dp[y + dy][x + dx] + board[y][x])
print(dp[n - 1][m - 1])
"""

"""dp (2) - 더 빠른 방법

input = sys.stdin.readline

N, M = map(int, input().split())
maze = [[0 for _ in range(M + 1)]]
dp = [[0 for _ in range(M + 1)] for __ in range(N + 1)]


for i in range(1, N + 1):
    maze.append([0] + list(map(int, input().split())))


for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + maze[i][j]

print(dp[N][M])
"""

import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


# DFS 풀이
def dfs(x, y, candy, visited):
    global Max
    if x == n - 1 and y == m - 1:
        candy += graph[x][y]
        if Max < candy:
            Max = candy
        return
    if 0 <= x < n and 0 <= y < m and visited[x][y] == 0:
        visited[x][y] = 1
        dfs(x + 1, y, candy + graph[x][y], visited)
        dfs(x, y + 1, candy + graph[x][y], visited)
        dfs(x + 1, y + 1, candy + graph[x][y], visited)


Max = 0
candy = 0
visited = [[0] * m for _ in range(n)]
dfs(0, 0, candy, visited)
print(Max)
