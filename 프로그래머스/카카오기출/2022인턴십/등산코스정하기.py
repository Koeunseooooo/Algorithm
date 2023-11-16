import heapq


def solution(n, paths, gates, summits):
    answer = []
    graph = [[] for _ in range(n + 1)]
    for path in paths:
        i, j, c = path
        graph[i].append((c, j))
        graph[j].append((c, i))

    INF = int(1e9)
    distance = [INF] * (n + 1)

    summits.sort()
    summits_set = set(summits)

    q = []
    for gate in gates:
        distance[gate] = 0
        heapq.heappush(q, (0, gate))

    while q:
        intensity, node = heapq.heappop(q)
        if distance[node] < intensity or node in summits_set:
            continue
        for next_intensity, next_node in graph[node]:
            new_intensity = max(next_intensity, intensity)
            if distance[next_node] > new_intensity:
                distance[next_node] = new_intensity
                heapq.heappush(q, (distance[next_node], next_node))
    min_intensity = [0, INF]
    for summit in summits:
        if distance[summit] < min_intensity[1]:  # 같다면 어짜피 업데이트를 안하므로
            min_intensity[0] = summit
            min_intensity[1] = distance[summit]
    return min_intensity
