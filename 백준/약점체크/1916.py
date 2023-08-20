# 다익스트라 알고리즘
import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)  # 10억
n = int(input().strip())
m = int(input().strip())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(1, m + 1):
    a, b, c = map(int, input().strip().split())
    # a번 노드에서 b로 가는 비용이 c라는 의미
    graph[a].append((b, c))

# 모든 간선 정보 입력
start, end = map(int, input().strip().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # (비용(거리)), 노드 번호)
    distance[start] = 0
    # 방문하지 않은 노드 중 최단거리가 가장 짧은 노드를 선택
    while q:
        curCost, curNode = heapq.heappop(q)
        # distance[curNode]보다 curCost가 크다면 방문한 노드임
        if distance[curNode] < curCost:
            # 다익스트라 알고리즘은 특정 노드(start)를 기준으로 모든 노드에 대한 최단 거리를 구하지만,
            # 문제에서는 모든 노드가 아닌 end 인덱스를 가진 노드에 대한 최단 거리만 요하므로 해당 값을 구하면 바로 break 처리
            if curNode == end:
                break
            else:
                continue
        for i in graph[curNode]:
            cost = curCost + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

print(distance[end])
