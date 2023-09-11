# from collections import deque
# import sys

# input = sys.stdin.readline


# m, n = map(int, input().strip().split())
# arr = []
# visited = [[0] * m for _ in range(n)]
# for _ in range(n):
#     arr.append(list(map(int, input().strip().split())))
# d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# q = deque()
# for y in range(n):
#     for x in range(m):
#         if arr[y][x] == 1:
#             q.append((y, x))
#             visited[y][x] = 1
#         elif arr[y][x] == -1:
#             visited[y][x] = 1

# while q:
#     y, x = q.popleft()
#     for dy, dx in d:
#         Y = dy + y
#         X = dx + x
#         if 0 <= Y < n and 0 <= X < m and not visited[Y][X]:
#             arr[Y][X] = arr[y][x] + 1
#             visited[Y][X] = 1
#             q.append((Y, X))


# max = -2
# for y in range(n):
#     for x in range(m):
#         if arr[y][x] == 0:
#             print(-1)
#             exit()
#         else:
#             if max < arr[y][x]:
#                 max = arr[y][x]
# print(max - 1)

from collections import deque
import sys

input = sys.stdin.readline


m, n = map(int, input().strip().split())
arr = []
# visited = [[0] * m for _ in range(n)]
for _ in range(n):
    arr.append(list(map(int, input().strip().split())))
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = deque()
for y in range(n):
    for x in range(m):
        if arr[y][x] == 1:
            q.append((y, x))
            # visited[y][x] = 1
        elif arr[y][x] == -1:
            pass
            # visited[y][x] = 1

while q:
    y, x = q.popleft()
    for dy, dx in d:
        Y = dy + y
        X = dx + x
        if 0 <= Y < n and 0 <= X < m and not arr[Y][X]:
            arr[Y][X] = arr[y][x] + 1
            q.append((Y, X))

max = -2
for y in range(n):
    for x in range(m):
        if arr[y][x] == 0:
            print(-1)
            exit()
        else:
            if max < arr[y][x]:
                max = arr[y][x]
print(max - 1)
