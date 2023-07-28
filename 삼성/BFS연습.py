# 배열의 (r,c) 위치에서 동서남북 4방향(또는 대각선 포함 8방향)으로 값을 탐색하는 경우
from collections import deque
# 좌, 하, 우 상
dx = [-1,0,1,0]
dy = [0,1,0,-1]

N=3

def out_of_range(y,x):
    return y<0 or x<0 or y>=N or x>=N

def bfs(y,x):
    q=deque()
    visited = [ False * N for _ in range(N)]
    q.append((y,x))
    visited[y][x]= True
    while q:
        sy, sx = q.popleft()
        for i in range(4):
            ny = sy + dy[i]
            nx = sx + dx[i]

            if out_of_range(ny,nx) or visited[ny][nx]:
                continue
            else:
                # do_anything()
                q.append((ny,nx))
                visited[ny][nx] = True

bfs()


