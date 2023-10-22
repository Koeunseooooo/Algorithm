from collections import deque
import copy
N,M,k=map(int,input().split())
d=[(0,1),(1,0),(0,-1),(-1,0)]
d_8=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

board=[]
for _ in range(N):
    board.append(list(map(int,input().split())))
history=[[0]*M for _ in range(N)] # 최근 공격 시간 기록
t=1
# 1: 1초전 2: 2초전 즉, 숫자가 클수록 공격한지 오래된 포탑이라고 가정
attacker=(-1,-1)
target=(-1,-1)

def print_board():
    global board
    for i in range(N):
        print(board[i])
    print('----')

# def get_attacker():
#     global board,history,attacker
#     MIN=5001
#     candidate=[]
#     for i in range(len(board)):
#         for j in range(len(board)):
#             if board[i][j]!=0:
#                 if MIN>board[i][j]:
#                     candidate=[]
#                     candidate.append((i,j,history[i][j]))
#                     MIN=board[i][j]
#                 elif MIN==board[i][j]:
#                     candidate.append((i,j,history[i][j]))
#     if len(candidate) >1:
#         candidate.sort(key=lambda x:(-x[2],-(x[0]+x[1]),-x[0]))
#     ay,ax,_=candidate[0]
#     attacker=(ay,ax)

def get_attacker():
    global attacker
    power = 5001
    global attacker
    ay,ax = attacker
    for y in range(N):
        for x in range(M):
            if board[y][x] == 0:  continue
            if board[y][x] < power:
                power = board[y][x]
                # print(power,'?',y,x)
                ay,ax = y,x
            elif board[y][x] == power: # 여기서부터는 우선순위 비교 들어감
                if history[y][x] > history[ay][ax]:
                    ay,ax=y,x
                elif history[y][x] == history[ay][ax]:
                    if y+x > ay+ax:
                       ay,ax=y,x
                    elif x + y == ax + ay:
                        if x > ax:
                            ay,ax=y,x
    attacker=(ay,ax)


# def get_attack_target():
#     global board, history, attacker,target
#     MAX = 0
#     candidate = []
#     for i in range(N):
#         for j in range(M):
#             if board[i][j] != 0 and attacker!=(i,j):
#                 if MAX < board[i][j]:
#                     candidate=[]
#                     candidate.append((i, j, history[i][j]))
#                     MAX = board[i][j]
#                 elif MAX==board[i][j]:
#                     candidate.append((i, j, history[i][j]))
#     if len(candidate) > 1:
#         candidate.sort(key=lambda x: (x[2], x[0] + x[1], x[0]))
#     ty, tx, _ = candidate[0]
#     target=(ty,tx)
def get_attack_target():
    global history

    power = -1
    global target
    ty,tx=target
    for y in range(N):
        for x in range(M):
            if board[y][x] == 0:  continue
            if x == ax and y == ay: continue
            if board[y][x] > power:
                power = board[y][x]
                ty,tx=y,x
            elif board[y][x] == power:
                if history[y][x] < history[ty][tx]:
                    ty,tx=y,x
                elif history[y][x] == history[ty][tx]:
                    if x + y < tx + ty:
                        ty,tx=y,x
                    elif x + y == tx + ty:
                        if x<tx:
                            ty,tx=y,x
    target=(ty,tx)


def laser_attack():
    global attacker,target
    ax,ay= attacker
    tx,ty=target
    '''
    경로 체크하기 위해 q 에 리스트 요소 정의
    '''
    q = deque()
    q.append((ax, ay, []))  # x, y, route
    visited = [[False] * M for _ in range(N)]
    visited[ax][ay] = True

    while q:
        x, y, route = q.popleft()
        for dx,dy in d:

            nx = (x + dx) % N
            ny = (y + dy) % M
            if visited[nx][ny]: continue
            if board[nx][ny] == 0: continue

            # 타겟에 도달한 경우
            if nx == tx and ny == ty:
                board[nx][ny] -= point
                for rx, ry in route:  # 경로 추적
                    board[rx][ry] -= half_point
                    attack[rx][ry] = True
                return True

            # 경로 체크
            tmp_route = route[:]
            tmp_route.append((nx, ny))
            visited[nx][ny] = True
            q.append((nx, ny, tmp_route))

    # 타겟이 도달하지 못하는 경우
    return False


def shell_attack():
    global attacker,target
    ax,ay=attacker
    tx,ty=target
    board[tx][ty] -= point
    for dx,dy in d_8:
        nx = (tx + dx) % N
        ny = (ty + dy) % M
        if nx == ax and ny == ay:   continue
        board[nx][ny] -= half_point
        attack[nx][ny] = True


def remove_top():
    for i in range(N):
        for j in range(M):
            if board[i][j]<0:
                board[i][j]=0

def max_check():
    return max([max(line) for line in board])
def maintain_top():
    turret = []
    turret_cnt = 0
    for x in range(N):
        for y in range(M):
            if board[x][y] == 0:  continue
            turret_cnt += 1
            if attack[x][y]:    continue
            turret.append((x, y))

    if turret_cnt == 1:
        print(max_check())
        exit(0)
    for x, y in turret:
        board[x][y] += 1
# def check_top():
#     global board
#     cnt=0
#     for i in range(N):
#         for j in range(M):
#             if board[i][j]!=0:
#                 cnt+=1
#     return cnt
def get_strongest_top():
    MAX=0
    for i in range(N):
        for j in range(M):
            if MAX<board[i][j]:
                MAX=board[i][j]
    return MAX


for i in range(k):
    attack = [[0] * M for _ in range(N)]

    # print_board()
    get_attacker()
    ay,ax=attacker
    attack[ay][ax]=1
    history[ay][ax]=t
    t += 1
    board[ay][ax]+=(N+M)
    # print('공격자',attacker)

    get_attack_target()
    ty, tx = target
    attack[ty][tx] = 1
    # print_board()
    # print('공격대상',target)
    point = board[ay][ax]
    half_point = point // 2
    if not laser_attack():
        shell_attack()
    # print_board()
    remove_top()
    # print_board()
    maintain_top()
    # print_board()
    # print('1 turn 완료')

print(max_check())
