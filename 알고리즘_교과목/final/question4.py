
vertex=['s','t','y','x','z']
graph = [[0, 3, 5, 0, 0], # 's'정점에서 인접한 정점들 
        [0, 2, 0, 6, 0,], # 순서는 vertex리스트 나열된 기준
        [0, 1, 0, 4, 6,], # 0은 자기자신 또는 무한대를 의미
        [0, 0, 0, 0, 2,],
        [3, 0, 0, 7, 0,],
        ]

# 경로 추척 및 출력하는 함수
def convert_index_to_vertex(to_vertex,parent,idx):
    # 인덱스넘버로 경로가 출력되므로, 이를 vertex 이름에 매칭하여 바꿔줌
    ver=vertex[idx]
    if parent[idx] == -1 :
        print(ver,end='->')
        return
    convert_index_to_vertex(to_vertex,parent , parent[idx],)
    if (ver==to_vertex):
        print(ver,end='')
    else:
        print(ver,end='->')

# 최단 거리 계산
def compute_min_distance(distance,queue):
    INF = float("Inf")
    min_index = -1
        
    for i in range(len(distance)):
        if distance[i] < INF and i in queue:
            INF = distance[i]
            min_index = i
    return min_index

def print_dijkstra(dist, parent, to_vertex):
    idx=vertex.index(to_vertex)
    print("%s-> %s | path : "%('s', to_vertex),end='')
    convert_index_to_vertex(to_vertex,parent,idx)
    print(" | total_costs : %d"%(dist[idx]))
    

def dijkstra(graph, source_vertex):
    source_vertex=vertex.index(source_vertex)

    graph_len = len(graph)
    distance = [float("Inf")] * graph_len # 처음은 모든 거리가 모두 무한대
    distance[source_vertex] = 0 # 시작 vertax의 최단거리는 0 (의미 없음)

    path_order= [-1] * graph_len # 경로 추척을 위한 리스트

    q = [] # 큐 구현

    for i in range(graph_len):
        q.append(i)
            
    while q:
        m = compute_min_distance(distance,q)
        q.remove(m)

        for i in range(graph_len):
            if i in q and graph[m][i]:
                if  distance[i] > distance[m] + graph[m][i] :
                    distance[i] = distance[m] + graph[m][i]
                    path_order[i] = m

    return distance, path_order


distance,paths = dijkstra(graph,'s')
print_dijkstra(distance,paths,'y')
print_dijkstra(distance,paths,'z')
 