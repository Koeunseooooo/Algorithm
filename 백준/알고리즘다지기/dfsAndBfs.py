graph = [[0], [2, 5, 9], [1, 3], [2, 4], [3], [1, 6, 8], [5, 7], [6], [5], [10], [9]]
visited = [0] * (10 + 1)

root = 1


def dfs_stack():
    stack = [root]
    while stack:
        n = stack.pop()
        print(n, end=" ")
        for i in graph[n]:
            if not visited[i]:
                stack.append(i)
                visited[i] = 1


dfs_stack()
print()

graph = [[0], [2, 5, 9], [1, 3], [2, 4], [3], [1, 6, 8], [5, 7], [6], [5], [10], [9]]
visited = [0] * (10 + 1)

root = 1


def dfs_recur(n):
    visited[n] = 1
    print(n, end=" ")
    for i in graph[n]:
        if not visited[i]:
            dfs_recur(i)


dfs_recur(root)
print()

# 순서가 다르게 순회되어서 결과값은 다르지만 둘다 dfs 라는 점!
from collections import deque

graph = [[0], [2, 5, 9], [1, 3], [2, 4], [3], [1, 6, 8], [5, 7], [6], [5], [10], [9]]
visited = [0] * (10 + 1)

root = 1


def bfs():
    q = deque()
    q.append(root)
    while q:
        n = q.popleft()
        print(n, end=" ")

        visited[n] = 1
        for i in graph[n]:
            if not visited[i]:
                q.append(i)


bfs()
