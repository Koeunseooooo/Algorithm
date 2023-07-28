N, M = map(int,input().split())
r,c,d = map(int,input().split())
arr=[]

# 북, 동, 남, 서
dx = [0,1,0,-1]
dy = [-1,0,1,0]

for _ in range(M):
    line = list(map(int,input().split()))
    arr.append(line)
print(arr)

# 처음 시작하는 곳 방문처리
visited = [[0]* M for _ in range(N)]
# 처음 시작하는 곳 칸의 개수 +1 
cnt=1


def first_step(r,c):
    if arr[r][c] == 0:
        arr[r][c]=2

def check_empty(r,c):
    if arr[r][c] == 0:
        return True
    else:
        return False

def out_of_range(r,c):
    return r<0 or c<0 or r>=N or c>=M

while True:
    for i in range(4):
        nx = r+dx[i]
        ny = c+dy[i]
        # 한번 돌았으면 그 방향으로 작업 시작
        if (not out_of_range(nx,ny)) and arr[nx][ny]==0:
            if visited[nx][ny]==0:
                visited[nx][ny]=1
                cnt+=1
