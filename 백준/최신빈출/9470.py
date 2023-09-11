from collections import deque
import sys

input = sys.stdin.readline

t = int(input().strip())
answer = []
for _ in range(t):
    k, m, p = map(int, input().strip().split())  # 테스트 케이스 번호 k, 노드의 수 m, 간선의 수 p
    order = [0] * (m + 1)  # visited
    indegree = [[0, 0, 0] for _ in range(m + 1)]
    graph = [[] for i in range(m + 1)]

    for _ in range(p):
        a, b = map(int, input().strip().split())
        graph[a].append(b)
        indegree[b][0] += 1

    def topological_sort():
        q = deque()
        for i in range(1, m + 1):
            if indegree[i][0] == 0:
                q.append(i)
                indegree[i][1] = 1

        while q:
            now = q.popleft()
            for i in graph[now]:
                indegree[i][0] -= 1
                if indegree[i][1] < indegree[now][1]:
                    indegree[i][1] = indegree[now][1]
                    indegree[i][2] = 1
                elif indegree[i][1] == indegree[now][1]:
                    indegree[i][2] += 1

                # 진입하수 0일경우 큐에 삽입
                if indegree[i][0] == 0:
                    if indegree[i][2] > 1:
                        indegree[i][1] += 1
                    q.append(i)

        answer.append((k, indegree[m][1]))

    topological_sort()

for k, order in answer:
    print(k, order)
