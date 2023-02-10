n = int(input())

graph = [[] for i in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)

arr = []
print(graph)


def dfs(s):
    # print(graph[s])
    for i in graph[s]:
        if visited[i] == 0:
            visited[i] = s
            print(visited)
            dfs(i)


dfs(1)

for x in range(2, n+1):
    print(visited[x])
