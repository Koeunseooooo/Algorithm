import copy
from collections import deque
N=int(input())
board=[]
for _ in range(N):
    board.append(list(map(int,input().split())))

group=[[[0,0,0] for _ in range(N)] for _  in range(N)] # groupNum, 해당 그룹을 이루고 있는 숫자 값, 전체 변의 개수

d=[(0,-1),(0,1),(1,0),(-1,0)]
def bfs(i,j,groupNum,visited,boardNum):
    coordinate=[]
    q=deque()
    q.append((i,j))
    visited[i][j]=1
    coordinate.append((i,j))
    while q:
        y,x = q.popleft()
        for dy, dx in d:
            Y=dy+y
            X=dx+x
            if 0<=Y<N and 0<=X<N and not visited[Y][X] and board[Y][X]==boardNum:
                visited[Y][X]=1
                q.append((Y,X))
                coordinate.append((Y,X))
    cnt=len(coordinate)
    for y,x in coordinate:
        group[y][x]=[groupNum,boardNum,cnt]




comb=[]
def combinations(n, new_arr, cur_idx,origin):
    # 순서 상관 X, 중복 X
    if len(new_arr) == n:
        comb.append(new_arr)
        return
    for i in range(cur_idx, len(origin)):
        combinations(n, new_arr + [origin[i]], i + 1,origin)

total_points=0
def checkGroupLine(group1Num,group2Num):
    global total_points
    q = deque()
    group1Info=[]
    group2Info=[]
    lineNum = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if group[i][j][0]==group1Num: # 조건 닿으면 바로 함수 return
                group1Info=group[i][j]
                # 그룹 간 인접한 변을 찾기 위한 bfs 수행 시작
                q.append((i,j))
                visited[i][j]=1
                while q:
                    y,x = q.popleft()
                    for dy, dx in d:
                        Y=y+dy
                        X=x+dx
                        if 0<=Y<N and 0<=X<N and not visited[Y][X]:
                            if group[Y][X][0]==group1Num:
                                visited[Y][X]=1
                                q.append((Y,X))
                            elif group[Y][X][0]==group2Num:
                                group2Info=group[Y][X]
                                # visited[Y][X] = 1
                                lineNum+=1
                if lineNum>0:
                    total_points+=(group1Info[2]+group2Info[2])*group1Info[1]*group2Info[1]*lineNum
                return
def getPoints():
    global groupNum,comb
    arr=[i for i in range(1,groupNum+1)]
    # 그룹 조합을 찾는다
    comb=[]
    combinations(2,[],0,arr)
    for c in comb:
        group1,group2=c
        checkGroupLine(group1,group2)

def plus_rotate(): # 십자가 모양 반시계 방향 회전

    for i in range(N):
        for j in range(N):
            if i == half:
                arr[i][j] = board[j][i]
            if j == half:
                arr[i][j] = board[N-j-1][N-i-1]


def square_rotate(x, y, l): # 부분 정사각형 회전

    for i in range(x, x+l):
        for j in range(y, y+l):
            ox, oy = i - x, j - y # (0, 0)으로 변환

            rx, ry = oy, l - ox - 1 # 시계 방향 회전 규칙

            arr[rx + x][ry + y] = board[i][j] # 다시 (x,y)를 더해줌


for _ in range(4):
    visited=[[0]*N for _ in range(N)]
    groupNum=0
    # bfs 돌면서 그룹 생성 및 그룹 별 정보를 group 배열에 담기
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                groupNum+=1
                bfs(i,j,groupNum,visited,board[i][j])
    getPoints()

    arr = [[0] * N for _ in range(N)]  # 배열 회전하기 위해 만든 빈 배열
    half = N // 2

    plus_rotate()

    square_rotate(0, 0, half)
    square_rotate(0, half + 1, half)
    square_rotate(half + 1, 0, half)
    square_rotate(half + 1, half + 1, half)

    board=copy.deepcopy(arr)
print(total_points)
