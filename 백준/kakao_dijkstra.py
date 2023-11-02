from collections import deque
import heapq

INF = 1e9


def solution(n, s, a, b, fares):
    answer = INF
    dis = [[INF] * n for _ in range(n)]
    graph = [[] for _ in range(n)]

    # 그래프에 간선 정보 기입
    for fare in fares:
        c, d, f = fare
        graph[c - 1].append((d - 1, f))
        graph[d - 1].append((c - 1, f))

    def dijkstra(i):
        q = []
        dis[i][i] = 0
        heapq.heappush(q, (0, i))
        while q:
            dist, cur_node = heapq.heappop(q)
            for _next in graph[cur_node]:
                next_node, next_cost = _next
                if dis[i][next_node] > dist + next_cost:
                    dis[i][next_node] = dist + next_cost
                    heapq.heappush(q, (dis[i][next_node], next_node))

    for i in range(n):
        dijkstra(i)

    for i in range(n):
        answer = min(answer, dis[s - 1][i] + dis[i][b - 1] + dis[i][a - 1])

    return answer
