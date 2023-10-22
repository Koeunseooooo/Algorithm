# import sys

# input = sys.stdin.readline
# from collections import defaultdict

# # 물고기의 정보는 두 정수 ai, bi로 이루어져 있고, ai는 물고기의 번호, bi는 방향을 의미한다.
# # 방향 bi는 8보다 작거나 같은 자연수를 의미하고, 1부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗
# # 반시계 방향으로 움직임
# d = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
# arr = [[0] * 4 for _ in range(4)]
# fishes = []
# shark = []
# result = 0
# for i in range(4):
#     a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().strip().split())
#     a = [a1, a2, a3, a4]
#     b = [b1 - 1, b2 - 1, b3 - 1, b4 - 1]
#     for j in range(4):
#         if i == 0 and j == 0:
#             shark = [i, j, b[j]]
#             result += a[j]
#             arr[i][j] = 0  # 안 해도 무방
#             fishes.append([a[j], b[j], 0])
#         else:
#             arr[i][j] = a[j]
#             fishes.append([a[j], b[j], 1])

# # 딕셔너리로 만들어서 key 값을 기준으로 sort하는 게 시간 복잡도가 더 빠를까?
# fishes.sort(key=lambda x: x[0])

# while 1:
#     # 물고기 이동
#     for p in range(len(fishes)):
#         num, d_idx, live = fishes[p]
#         if not live:
#             continue
#         y, x = 0, 0
#         for i in range(4):
#             for j in range(4):
#                 if arr[i][j] == num:
#                     y = i
#                     x = j
#         start = d_idx
#         for k in range(start, start + 9):
#             dy, dx = d[k % 8]
#             Y = dy + y
#             X = dx + x
#             if (
#                 0 <= Y < 4
#                 and 0 <= X < 4
#                 and arr[Y][X] >= 0
#                 and not (Y == shark[0] and X == shark[1])
#             ):
#                 tmp = arr[Y][X]
#                 arr[Y][X] = arr[y][x]
#                 arr[y][x] = tmp
#                 fishes[p][1] = k % 8  # 방향 바꿔줘야하는데..
#                 break

#     # 상어 이동
#     y, x, d_idx = shark
#     dy, dx = d[d_idx]
#     possible = []
#     while 1:
#         Y = dy + y
#         X = dx + x
#         if 0 <= Y < 4 and 0 <= X < 4:
#             if arr[Y][X] != 0:
#                 possible.append(
#                     [Y, X, fishes[arr[Y][X] - 1][0], fishes[arr[Y][X] - 1][1]]
#                 )
#             y = Y
#             x = X
#         else:
#             break

#     if len(possible) == 0:
#         break
#     else:
#         target = max(possible, key=lambda x: x[2])
#         y, x, n, dd = target
#         arr[y][x] = 0
#         shark = [y, x, dd]
#         result += n
#         fishes[n - 1][2] = 0

#     print("hello")
#     for i in range(len(arr)):
#         print(arr[i])
# print(result)

# 슬프지만 위 코드는 나에 사랑스러운 코드이니 나라도 품자 . .
# 청소년 상어 - BOJ 19236
# DFS+구현
import copy

board = [[] for _ in range(4)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    data = list(map(int, input().split()))
    fish = []
    for j in range(4):
        # 물고기 번호, 방향
        fish.append([data[2 * j], data[2 * j + 1] - 1])
    board[i] = fish


max_score = 0


def dfs(sx, sy, score, board):
    global max_score
    score += board[sx][sy][0]
    max_score = max(max_score, score)
    board[sx][sy][0] = 0

    # 물고기 움직임
    for f in range(1, 17):
        f_x, f_y = -1, -1
        for x in range(4):
            for y in range(4):
                if board[x][y][0] == f:
                    f_x, f_y = x, y
                    break
        if f_x == -1 and f_y == -1:
            continue
        f_d = board[f_x][f_y][1]

        for i in range(8):
            nd = (f_d + i) % 8
            nx = f_x + dx[nd]
            ny = f_y + dy[nd]
            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                continue
            board[f_x][f_y][1] = nd
            board[f_x][f_y], board[nx][ny] = board[nx][ny], board[f_x][f_y]
            break

    # 상어 먹음
    s_d = board[sx][sy][1]
    for i in range(1, 5):
        nx = sx + dx[s_d] * i
        ny = sy + dy[s_d] * i
        if (0 <= nx < 4 and 0 <= ny < 4) and board[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(board))


dfs(0, 0, 0, board)
print(max_score)
