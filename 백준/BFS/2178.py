from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))


def bfs(x, y):
    # 이동할 4가지 방향 정의 (상,하,좌,우)
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append((x, y))
    # print(queue)

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            tmp_x = x+dx[i]
            tmp_y = y+dy[i]
            if tmp_x >= 0 and tmp_x < n and tmp_y >= 0 and tmp_y < m:
                if graph[tmp_x][tmp_y] == 1:
                    graph[tmp_x][tmp_y] = graph[x][y]+1
                    queue.append((tmp_x, tmp_y))

    return graph[n-1][m-1]


print(bfs(0, 0))
