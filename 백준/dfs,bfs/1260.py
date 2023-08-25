from collections import deque

n, m, v = map(int, input().split())
# n 정점의 개수
# m 간선의 개수
# v 탐색을 시작할 번호

graph = [[] for _ in range(n + 1)]
visited_dfs = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()


def dfs(n):
    visited_dfs[n] = 1
    print(n, end=" ")
    for i in graph[n]:
        if not visited_dfs[i]:
            dfs(i)


dfs(v)
print()

visited_bfs = [0] * (n + 1)


def bfs():
    q = deque()
    q.append(v)
    visited_bfs[v] = 1
    while q:
        n = q.popleft()
        print(n, end=" ")
        visited_bfs[n] = 1
        for i in graph[n]:
            if not visited_bfs[i]:
                q.append(i)
                # visited_bfs[i] = 1


bfs()
