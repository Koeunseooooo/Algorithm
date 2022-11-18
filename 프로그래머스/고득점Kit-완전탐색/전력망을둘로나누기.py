# 완탐 유형이지만 bfs로 풀었음
from collections import deque
def solution(n, wires):
    answer = -1
    result=[]
    tree=[[] for _ in range(n+1)] # 인덱스 0은 무시
    
    # 전선을 입력받아 tree 만들기 -> 이중리스트 만들기
    for wire in wires:
        tree[wire[0]].append(wire[1])
        tree[wire[1]].append(wire[0])
        
    def bfs(start,tree,visited,wire):
        queue=deque()
        queue.append(start)
        visited[start]=True
        cnt=1

        while queue:
            v=queue.popleft()
            for i in tree[v]:
                if not ((v == wire[0] and i == wire[1]) or (v == wire[1] and i == wire[0])):
                    if not visited[i]:
                        queue.append(i)
                        visited[i]=True
                        cnt+=1
        return cnt

    for wire in wires:
        visited = [False for _ in range(n+1)]
        tmp=[]
        for i in range(1,len(visited)):
            if not visited[i]:
                cnt=bfs(i,tree,visited,wire)
                tmp.append(cnt)
        tmp_res=abs(tmp[0]-tmp[1])
        result.append(tmp_res)
        
    answer=min(result)
    return answer

        


