graph = {
    'r': ['s','v'],
    's': ['r','w'],
    'v': ['r'],
    'w': ['s','t','x'],
    't': ['w', 'x','u'],
    'x': ['w','t','u','y'],
    'y': ['u','x'],
    'u': ['t','x','y'],
}

def dfs(graph, source_vertex):
    visit = []
    stack = []
    pi=[None,]
    d=[]
    depth=0

    stack.append(source_vertex)

    while stack:
        node = stack.pop()
        if node not in visit:
            if node in graph[source_vertex]:
                depth=1
            visit.append(node)
            stack.extend(graph[node])
            d.append(depth)
            depth=depth+1

    for i in range(len(visit)-1):
        if visit[i+1] in graph['s']:
            pi.append(source_vertex)
        else:
            pi.append(visit[i])

    for i in range(len(visit)):
        print("vertax: %s | d: %d | 𝜋: %s"%(visit[i],d[i],pi[i]))

dfs(graph,'s')