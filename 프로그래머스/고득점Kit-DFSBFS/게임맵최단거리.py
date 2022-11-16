from collections import deque

# 최단거리 -> bfs로
def solution(maps):
    n=len(maps)
    m=len(maps[0])
    
    visited = [False for _ in range(n) for i in range(m)]
    answer = 0
    
    # dx, dy (상,좌,하,우)
    dx=[0,-1,0,1]
    dy=[-1,0,1,0]
    
    def bfs(i,j):
        queue=deque()
        queue.append((i,j))

        while queue:
            x, y=queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                if maps[nx][ny]==1:
                        queue.append((nx,ny))
                        maps[nx][ny]=maps[x][y]+1
            # print(maps)
            
    bfs(0,0)
    answer = maps[n-1][m-1]
    if answer ==1:
        answer = -1
    
    return answer


    
            
            
        
            
    