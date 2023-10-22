N,M,K= map(int,input().split())
board=[]
for _ in range(N):
    board.append(list(map(int,input().split())))
# 회전의 구현을 편하게 하기 위해 2차원 배열을 하나 더 정의해줍니다.
next_board = [
    [0] * (N)
    for _ in range(N)
]
people=[]
for _ in range(M):
    y,x=map(int,input().split())
    people.append((y,x))

ey,ex=map(int,input().split())
exit=(ey,ex)

result=0 # 모든 참가자들의 이동 거리의 합

sy, sx, sz = 0, 0,0 # 회전해야 하는 최소 정사각형을 찾아서 기록해 줌

def move_all_traveler():
    global exit, result
    for i in range(M):
        # 이미 출구에 있는 경우 스킵
        if people[i]==exit:
            continue
        py,px=people[i]
        ey,ex=exit

        # 행이 다른 경우 행을 이동 시킨다
        if py != ey:
            PY,PX=py,px
            if ey> PY:
                PY+=1
            else:
                PY-=1

            # 벽이 없어야만 행을 이동시킬 수 있습니다.
            # 이 경우 행을 이동시키고 바로 다음 참가자로 넘어갑니다.
            if not board[PY][PX]:
                people[i]=(PY,PX)
                result+=1
                continue

        # 열이 다른 경우 열을 이동 시킨다
        if px!=ex:
            PY,PX=py,px
            if ex>PX:
                PX+=1
            else:
                PX-=1

            if not board[PY][PX]:
                people[i]=(PY,PX)
                result+=1
                continue

def find_minimum_square():
    global exit, sy, sx, sz
    ey,ex=exit
    # 가장 작은 정사각형(2x2)부터 모든 정사각형(nxn까지)을 만들어 봄
    for szz in range(2,N+1):
        for y1 in range(N-szz+1):
            for x1 in range(N-szz+1):
                y2=y1+szz-1
                x2=x1+szz-1
                # 해당 범위 안에 출구가 있다면 첫번째 관문 통과
                # 해당 범위 안에 참가자가 있다면 최종 관문 통과
                is_people = False
                if x1<=ex<=x2 and y1<=ey<=y2:
                    for i in range(M):
                        py,px=people[i]
                        if y1<=py<=y2 and x1<=px<x2:
                            if (py,px)!=exit :
                                is_people=True
                if is_people:
                    sy=y1
                    sx=x1
                    sz=szz
                    # 여기까지 오면 우선순위가 제일 높은 정사각형을 찾았단 뜻이므로 바로 return
                    return


def rotate_square():
    global board,sy,sx,sz


    for y in range(sy,sy+sz):
        for x in range(sx,sx+sz):
            if board[y][x]:
                board[y][x]-=1

    for y in range(sy,sy+sz):
        for x in range(sx,sx+sz):
            oy,ox=y-sy,x-sx
            ry,rx=ox,sz-oy-1
            next_board[ry+sy][rx+sx]=board[y][x]

    # 다시 board에 옮겨주기
    for y in range(sy,sy+sz):
        for x in range(sx,sx+sz):
            board[y][x]=next_board[y][x]

def rotate_traveler_and_exit():
    global exit,sy,sz,sx
    for i in range(M):
        # 여기선 탈출구에 있는 참가자도 움직여주어야 탈출구랑 함께 좌표를 이동해 다닐 수 있음
        py,px=people[i]
        if sy<=py<sy+sz and sx<=px<sx+sz:
            oy,ox=py-sy,px-sx
            ry,rx=ox,sz-oy-1
            people[i]=(ry+sy,rx+sx)
    # 탈출구도 똑같이!
    ey,ex=exit
    # 아래 조건은 사실 정사각형을 찾는 함수를 호출했을 때 이미 검증된 조건이긴 함 (이중조건 느낌? == 불필요한 것 아닐까 그치만 무서우니까 그냥 두자)
    if sy<=ey<sy+sz and sx<=ex<sx+sz:
        oy, ox = ey - sy, ex - sx
        ry, rx = ox, sz - oy - 1
        exit = (ry + sy, rx + sx)

for _ in range(K):
    # 모든 참가자를 이동시킨다
    move_all_traveler()

    # 모든 사람이 출구로 탈출했는지 판단합니다.
    is_all_escaped = True
    for i in range(M):
        if people[i] != exit:
            is_all_escaped = False
    if is_all_escaped:
        break

    # 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 찾습니다.
    find_minimum_square()

    # 정사각형 내부의 벽을 회전시킵니다.
    rotate_square()
    # 모든 참가자들 및 출구를 회전시킵니다.
    rotate_traveler_and_exit()

print(result)
ey,ex=exit
print(ey,ex)
