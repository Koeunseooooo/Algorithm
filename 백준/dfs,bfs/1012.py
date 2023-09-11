import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)


t = int(input().strip())

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]


answer = []
for _ in range(t):
    m, n, k = map(int, input().strip().split())  # 가로, 세로, 배추가 심어져있는 위치의 개수

    arr = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().strip().split())
        arr[y][x] = 1

    def dfs(y, x):
        arr[y][x] = -1

        for dy, dx in d:
            Y = y + dy
            X = x + dx
            if 0 <= Y < n and 0 <= X < m and arr[Y][X] == 1:
                dfs(Y, X)

    cnt = 0
    for y in range(n):
        for x in range(m):
            if arr[y][x] == 1:
                dfs(y, x)
                cnt += 1
    answer.append(cnt)


for a in answer:
    print(a)
