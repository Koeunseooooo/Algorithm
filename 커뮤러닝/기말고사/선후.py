from heapq import heappush, heappop
from collections import defaultdict


def solution(s1, s2, k):

    # 전체 그래프 생성
    graph = defaultdict(list)

    for X, Y in zip(s1, s2):
        graph[Y].append(X)
    # print(graph)
    answer, leafs = [], []

    # K에 관련된 그래프 생성 즉, k와 무관한 관계는 graph_k그래프에 담기지 않음
    stack = [k]
    visited = set([k])
    graph_k = defaultdict(list)
    indegrees = defaultdict(int)

    while stack:
        node = stack.pop()
        if graph[node]:
            for prev in graph[node]:
                indegrees[node] += 1
                graph_k[prev].append(node)
                if prev not in visited:
                    stack.append(prev)
                    visited.add(prev)
        else:
            # 단말노드를 heap에 입력 (여기서 단말노드란 진입차수가 0인 노드를 의미함)
            heappush(leafs, node)
    # print(graph_k)
    # print(leafs)
    # 위상정렬
    while leafs:  # 더 이상 제거할 간선이 없는 노드에 접근할 때까지(진출차수가 없을때까지)
        node = heappop(leafs)
        answer.append(node)
        for next_node in graph_k[node]:
            indegrees[next_node] -= 1
            if indegrees[next_node] == 0:
                heappush(leafs, next_node)
        print(leafs)
    return answer


s1 = ["A", "E", "B", "D", "B", "H", "F", "H", "C"]
s2 = ["G", "C", "G", "F", "J", "E", "B", "F", "B"]
k = "B"

print(solution(s1, s2, k))
