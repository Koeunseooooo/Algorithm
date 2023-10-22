d=[(-1,0),(0,-1),(1,0),(0,1)]
temp=[]
def dfs(x,y,dep,cnt,visit):
    global max_eat, shark,eat,d
    if dep==3:
        if max_eat < cnt :
            max_eat=cnt
            shark=(x,y)
            eat=visit[:]
            return
    for dx , dy in d:
        nx=x+dx
        ny=y+dy
        if 0<=nx<4 and 0<=ny<4:
            if (nx,ny) not in visit:
                visit.append((nx,ny))
                dfs(nx,ny,dep+1,cnt+len(temp[nx][ny]),visit)
                visit.pop()
            else:
                dfs(nx,ny,dep,cnt,visit)