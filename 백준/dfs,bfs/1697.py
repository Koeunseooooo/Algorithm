import sys
from collections import deque

input = sys.stdin.readline


n, k = map(int, input().split())

visited = [0] * 100001


def bfs():
    q = deque()
    q.append(n)
    visited[n] = 0

    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        if 0 <= x - 1 <= 100000 and visited[x - 1] == 0:
            q.append(x - 1)
            visited[x - 1] = visited[x] + 1
        if 0 <= x + 1 <= 100000 and visited[x + 1] == 0:
            q.append(x + 1)
            visited[x + 1] = visited[x] + 1
        if 0 <= 2 * x <= 100000 and visited[2 * x] == 0:
            q.append(x * 2)
            visited[x * 2] = visited[x] + 1


bfs()
