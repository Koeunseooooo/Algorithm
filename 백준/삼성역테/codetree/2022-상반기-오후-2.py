N,M,K,C= map(int,input().split())
result=0
board=[] # 나무 & 벽 & 빈칸이 저장되어 있는 2차원 배열
for _ in range(N):
    board.append(list(map(int,input().split())))
herb=[[0]*N for _ in range(N)] # 농약 여부

dd=[(-1,-1),(-1,1),(1,-1),(1,1)] # 대각선 방향
d=[(1,0),(-1,0),(0,-1),(0,1)] # 상하좌우

def grow_tree():
    for i in range(N):
        for j in range(N):
            if board[i][j]>0 : # 나무라면
                for dy, dx in d:
                    Y=i+dy
                    X=j+dx
                    if 0<=Y<N and 0<=X<N and board[Y][X]>0: # 인접한 칸에 나무가 있다면
                        board[i][j]+=1

def print_board():
    for i in range(len(board)):
        print(board[i])
    print('-----')

def breed_tree():
    temp=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j]>0: #나무라면
                cnt=0
                candidate=[]
                for dy, dx in d:
                    Y=i+dy
                    X=j+dx
                    if 0<=X<N and 0<=Y<N and board[Y][X]==0 and herb[Y][X]==0:
                        candidate.append((Y,X))
                        cnt+=1
                if cnt==0:
                    continue
                treeNum=board[i][j]//cnt
                for y,x in candidate:
                    temp[y][x]+=treeNum

    for i in range(N):
        for j in range(N):
            board[i][j]+=temp[i][j]

def select_herb_space():
    max_total=-1
    max_loc=(-1,-1)
    for i in range(N):
        for j in range(N):
            if board[i][j]>0: # 나무라면
                deadTreeNum=board[i][j]
                for dy, dx in dd:
                    y, x = i, j
                    for _ in range(K):
                        Y=dy+y
                        X=dx+x
                        if 0<=Y<N and 0<=X<N and board[Y][X]>0:
                            y=Y
                            x=X
                            deadTreeNum+=board[Y][X]
                        else:
                            break
                if max_total<deadTreeNum:
                    max_total=deadTreeNum
                    max_loc=(i,j)
    return max_loc,max_total

def spray_herb(max_loc,max_total):
    sy,sx=max_loc
    if max_total==-1:
        return
    global result
    result+=max_total
    board[sy][sx]=0 # 본인 나무 먼저 박멸
    herb[sy][sx]=C+1
    for dy, dx in dd:
        y, x = sy, sx
        for _ in range(K):
            Y = dy + y
            X = dx + x
            if 0 <= Y < N and 0 <= X < N :
                if board[Y][X] > 0:
                    board[Y][X]=0 # 나무 박멸
                    herb[Y][X] = C + 1
                    y=Y
                    x=X
                elif board[Y][X]==-1 or board[Y][X]==0:
                    herb[Y][X] = C + 1
                    break
            else:
                break

def remove_herb():
    for i in range(N):
        for j in range(N):
            if herb[i][j]>0:
                herb[i][j]-=1
def print_herb():
    for i in range(N):
        print(herb[i])

for _ in range(M):
    grow_tree()
    # print_board()
    breed_tree()
    # print_board()
    max_loc,max_total=select_herb_space()
    spray_herb(max_loc,max_total)
    # print_board()
    # print_herb()
    remove_herb()

print(result)