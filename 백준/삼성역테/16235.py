import sys

input = sys.stdin.readline
from collections import deque


n, m, k = map(int, input().strip().split())
bita = []
for _ in range(n):
    bita.append(list(map(int, input().strip().split())))  # 겨울에 쓰는 양분
tree = []
for _ in range(m):
    y, x, z = map(int, input().strip().split())  # (y,x)는 나무의 위치, 마지막은 나무의 나이
    tree.append([y - 1, x - 1, z])
arr = [[5] * n for _ in range(n)]


def spring(arr, tree):
    tree.sort(key=lambda x: (x[0], x[1], x[2]))
    spring_q = deque(tree)
    dead = []  # 죽은 나무가 있다면 여기에 저장
    while spring_q:
        y, x, z = spring_q.popleft()
        # 양분 먹을 때
        if arr[y][x] >= z:
            arr[y][x] -= z
            tree.remove([y, x, z])
            tree.append([y, x, z + 1])
        else:
            dead.append([y, x, z])
            tree.remove([y, x, z])
    return dead, arr, tree


def summer(arr, dead):
    for d in dead:
        y, x, z = d
        new = z // 2
        arr[y][x] += new
    return arr


# (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)
d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def autumm(tree):
    for t in tree:
        y, x, z = t
        if z % 5 == 0:
            for dy, dx in d:
                Y = y + dy
                X = x + dx
                if 0 <= Y < n and 0 <= X < n:
                    tree.append([Y, X, 1])
    return tree


def winter(arr):
    for i in range(n):
        for j in range(n):
            arr[i][j] += bita[i][j]
    return arr


cur_y = 0  # 현재 년도를 나타냄
tree_num = 0  # 현재 살아있는 나무의 개수
while 1:
    if cur_y == k:
        break
    dead, arr, tree = spring(arr, tree)
    arr = summer(arr, dead)
    tree = autumm(tree)
    arr = winter(arr)
    cur_y += 1


print(len(tree))
