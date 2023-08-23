import sys
from collections import deque

input = sys.stdin.readline

c = int(input().strip())
e = int(input().strip())

arr = [[] for _ in range(c + 1)]
visited = [0] * (c + 1)
for _ in range(e):
    a, b = map(int, input().strip().split())
    arr[a].append(b)
    arr[b].append(a)


def bfs():
    q = deque()
    q.append(1)
    visited[1] = 1
    cnt = 0
    while q:
        n = q.popleft()
        cnt += 1
        for i in arr[n]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
    return cnt


print(bfs() - 1)
