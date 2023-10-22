import sys
from collections import deque

input = sys.stdin.readline


field = []

for _ in range(12):
    field.append(list(input().strip()))


def bfs(y, x):
    q = deque()
    d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    q.append((y, x))
    temp.append((y, x))
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            Y = y + dy
            X = x + dx
            if (
                0 <= Y < 12
                and 0 <= X < 6
                and field[Y][X] == field[y][x]
                and visited[Y][X] == 0
            ):
                q.append((Y, X))
                temp.append((Y, X))
                visited[Y][X] = 1


# 아래로 당기는 함수
def gravity():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if field[j][i] != "." and field[k][i] == ".":
                    field[k][i] = field[j][i]
                    field[j][i] = "."
                    break


def delete(temp):
    for y, x in temp:
        field[y][x] = "."


ans = 0
while 1:
    flag = 0
    visited = [[0] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if field[i][j].isalpha() and visited[i][j] == 0:
                visited[i][j] = 1
                temp = []
                bfs(i, j)
                if len(temp) >= 4:
                    flag = 1
                    delete(temp)
    if flag == 0:
        break
    gravity()
    ans += 1

print(ans)
