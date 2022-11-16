''' 
졌잘싸 코드.... 
물론 잘 안돌아가긴 하지만(정답이긴 함) dfs/bfs 적용시키려고 했던 수고가 
정석적인 풀이와 그렇게 빗겨나가진 않았음 !
'''


def solution(n, computers):
    answer = 0
    graph=[[],]
    visited = [False]*(n+1)
    for i in range(n):
        tmp=[]
        for j in range(n):
            if j!=i and computers[i][j]:
                tmp.append(j+1)
        graph.append(tmp)
    
    # print(visited[1:],22)
    while True:
        if all(visited[1:]):
            break
        else:
            for i in range(1,len(visited)):
                if visited[i]==False:
                    dfs(graph,i,visited)
                    answer+=1
    return answer

def dfs(graph,v,visited):
    visited[v]=True
    print(visited)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

