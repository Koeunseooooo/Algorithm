# n, m, k = map(int, input().split())
#
# board = []
# for _ in range(n):
#     board.append(list(map(int, input().split())))
#
# peoples = []
# for i in range(m):
#     y, x = map(int, input().split())
#     peoples.append((y - 1, x - 1))
#
# y, x = map(int, input().split())
# exit = (y - 1, x - 1)
# # 회전의 구현을 편하게 하기 위해 2차원 배열을 하나 더 정의
# new_board=[[0]*n for _ in range(n)]
# # 회전해야 하는 최소 정사각형을 찾아 기록해 줌
# sy,sx, square_size = 0, 0, 0
#
#
# # 모든 참가자를 이동시킵니다.
# def move_all_traveler():
#     global exit, result
#
#     # m명의 모든 참가자들에 대해 이동을 진행합니다.
#     for i in range(m):
#         # 이미 출구에 있는 경우 스킵합니다.
#         if peoples[i] == exit:
#             continue
#
#         tx, ty = peoples[i]
#         ex, ey = exit
#
#         # 행이 다른 경우 행을 이동시켜봅니다.
#         if tx != ex:
#             nx, ny = tx, ty
#
#             if ex > nx:
#                 nx += 1
#             else:
#                 nx -= 1
#
#             # 벽이 없다면 행을 이동시킬 수 있습니다.
#             # 이 경우 행을 이동시키고 바로 다음 참가자로 넘어갑니다.
#             if not board[nx][ny]:
#                 peoples[i] = (nx, ny)
#                 result += 1
#                 continue
#
#         # 열이 다른 경우 열을 이동시켜봅니다.
#         if ty != ey:
#             nx, ny = tx, ty
#
#             if ey > ny:
#                 ny += 1
#             else:
#                 ny -= 1
#
#             # 벽이 없다면 행을 이동시킬 수 있습니다.
#             # 이 경우 열을 이동시킵니다.
#             if not board[nx][ny]:
#                 peoples[i] = (nx, ny)
#                 result += 1
#                 continue
#     print(peoples)
#
# def print_board():
#     global board
#     for i in range(len(board)):
#         print(board[i])
#
# def print_sqaure_info():
#     print('정사각형 좌표',sy,sx)
#     print('정사각형 사이즈',square_size)
#
#
# d = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상,하,좌,우
# result=0 # 모든 참가자들의 이동 거리 합
#
# def move_peoples():
#     global peoples, exit,result
#     e_y, e_x = exit
#     for i in range(len(peoples)):
#         y,x=peoples[i]
#         if (y,x)==(e_y,e_x):
#             continue
#             # peoples.remove((y,x)) # 피드백 : 굳이 제거하려 들지 않아도 됨. 괜히 인덱스 에러 날 위험 있음
#         candidate = []
#         # 출구와 현재 칸 비교
#         # 피드백 : 간단한 로직이니 그냥 조건문 안에서 바로 바로 처리해도 됨
#         if y > e_y:
#             candidate.append(0)
#         elif y < e_y:
#             candidate.append(1)
#         if x > e_x:
#             candidate.append(2)
#         elif x < e_x:
#             candidate.append(3)
#         if len(candidate)==0:
#             continue
#         if len(candidate)>1:
#             candidate.sort()
#             # 피드백 : 굳이 candidate 선언할 필요 없음. 좌우보다 상하가 더 우선이기 때문에 continue 잘 써면 됨
#         d_idx=candidate[0]
#         dy,dx=d[d_idx]
#         Y=y+dy
#         X=x+dx
#         if 0<=Y<n and 0<=X<n and board[Y][X]==0: # 0 : 빈 칸
#             y=Y
#             x=X
#             peoples[i]=(y,x)
#             result+=1 # 한 칸씩 움직이므로 1 증가
#     print(peoples)
# def find_smallest_sqare():
#     global exit,sy,sx,square_size
#     ey,ex=exit
#
#     # 가장 작은 정사각형부터 모든 정사각형을 만들어보자
#     for sz in range(2,n+1):
#         # 가장 좌상단 r 좌표가 작은 것 부터 하나씩
#         for y1 in range(0,n-sz+1): # n-sz : r 좌표의 최댓값은 n에서 현재 정사각형 사이즈를 뺀 만큼임
#             for x1 in range(0,n-sz+1): # 위의 주석 설명과 동일함
#                 y2=y1+sz-1
#                 x2=x1+sz-1
#                 # 출구 포함하지 않는다면 skip
#                 if not(y1<=ey<=y2 and x1<=ex<=x2):
#                     continue
#
#                 # 참가자가 한 명도 없다면 skip
#                 is_people=False
#                 for ty,tx in peoples:
#                     if y1<=ty<=y2 and x1<=tx<x2:
#                         # 주의 : 출구에 있는 참가자는 이미 탈출한 참가자이므로 격자에서 탈출한 것이므로 제외
#                         if not (ty==ey and tx==ex):
#                             is_people=True
#                 if is_people:
#                     sy=y1
#                     sx=x1
#                     square_size=sz
#                     return
#
# # 선택한 정사각형은 시계방향으로 90도 회전하며, 회전된 벽은 내구도가 1씩 감소
#
# # 정사각형 내부의 벽을 회전시킵니다.
# def rotate_square():
#     global new_board
#     # 우선 정사각형 안에 있는 벽들을 1 감소시킵니다.
#     for x in range(sx, sx + square_size):
#         for y in range(sy, sy + square_size):
#             if board[x][y]:
#                 board[x][y] -= 1
#
#     # 정사각형을 시계방향으로 90' 회전합니다.
#     for x in range(sx, sx + square_size):
#         for y in range(sy, sy + square_size):
#             # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환을 진행합니다.
#             ox, oy = x - sx, y - sy
#             # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1)가 됩니다.
#             rx, ry = oy, square_size - ox - 1
#             # Step 3. 다시 (sx, sy)를 더해줍니다.
#             new_board[rx + sx][ry + sy] = board[x][y]
#
#     # next_board 값을 현재 board에 옮겨줍니다.
#     for x in range(sx, sx + square_size):
#         for y in range(sy, sy + square_size):
#             board[x][y] = new_board[x][y]
#
# def rotate_90_square():
#     global sy,sx,square_size,new_board,ey,ex
#     new_board = [[0] * n for _ in range(n)] # 초기화
#     # 우선 정사각형 안에 있는 벽들을 1 감소
#     for y in range(sy,sy+square_size):
#         for x in range(sx,sx+square_size):
#             if board[y][x]>0:
#                 board[y][x]-=1
#     # 정사각형을 시계 방향으로 90도 회전
#     for i in range(square_size):
#         for j in range(square_size):
#             new_board[sx+j][square_size+sy-i-1]=board[sy+i][sx+j]
#             # 피드백 : 정사각형 돌리면서 동시에 참가자와 출구 좌표까지 업데이트 하기 힘드므로 함수를 나누어보자
#             # for i in range(len(peoples)):
#             #     ty,tx=peoples[i]
#             #     if sy+i==ty and sx+j==tx:
#             #         if not ty==ey and tx==ex:
#     for i in range(len(new_board)):
#         print(new_board[i])
#     print('위는 새로운 보드')
#     # newboard를 board에 옮겨준다
#     for i in range(square_size):
#         for j in range(square_size):
#             board[sy+i][sx+j]=new_board[sy+i][sx+j]
#     print_board()
# def rotate_90_travler_exit():
#     global exit,peoples,sy,sx,square_size
#     # 먼저 m명의 참가자들을 모두 확인한다
#     # m명의 참가자들을 모두 확인합니다.
#     for i in range(m):
#         tx, ty = peoples[i]
#         # 해당 참가자가 정사각형 안에 포함되어 있을 때에만 회전시킵니다.
#         if sy <= tx and tx < sy + square_size and sx <= ty and ty < sx + square_size:
#             # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환을 진행합니다.
#             ox, oy = tx - sy, ty - sx
#             # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1)가 됩니다.
#             rx, ry = oy, square_size - ox - 1
#             # Step 3. 다시 (sx, sy)를 더해줍니다.
#             peoples[i] = (rx + sy, ry + sx)
#     print(peoples)
#     # 출구에도 회전을 진행한다
#     ex, ey = exit
#     if sy <= ex and ex < sy + square_size and sx <= ey and ex < sy + square_size:
#         # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환을 진행합니다.
#         ox, oy = ex - sy, ey - sx
#         # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1)가 됩니다.
#         rx, ry = oy, square_size - ox - 1
#         # Step 3. 다시 (sx, sy)를 더해줍니다.
#         exit = (rx + sy, ry + sx)
#
# for _ in range(k):
#     # 모든 참가자 이동
#     move_all_traveler()
#     # 모든 사람이 출구로 탈출했는지 판단
#     is_all_escaped=True
#     for i in range(m):
#         if peoples[i]!=exit:
#             is_all_escaped=False
#     if is_all_escaped:
#         break
#     # 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 찾는다
#     find_smallest_sqare()
#     print_sqaure_info()
#     # 정사각형 내부의 벽을 회전시킨다
#     rotate_square()
#     # 모든 참가자들 및 출구를 회전시킨다
#     rotate_90_travler_exit()
#     print('-----')
#
#
# print(result)
# ey,ex=exit
# print(ey,ex)

n, m, k = tuple(map(int, input().split()))
# 모든 벽들의 상태를 기록해줍니다.
board = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

for i in range(1, n + 1):
    board[i] = [0] + list(map(int, input().split()))

# 회전의 구현을 편하게 하기 위해 2차원 배열을 하나 더 정의해줍니다.
next_board = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

# 참가자의 위치 정보를 기록해줍니다.
traveler = [(-1, -1)] + [
    tuple(map(int, input().split()))
    for _ in range(m)
]

# 출구의 위치 정보를 기록해줍니다.
exits = tuple(map(int, input().split()))

# 정답(모든 참가자들의 이동 거리 합)을 기록해줍니다.
ans = 0

# 회전해야 하는 최소 정사각형을 찾아 기록해줍니다.
sx, sy, square_size = 0, 0, 0


# 모든 참가자를 이동시킵니다.
def move_all_traveler():
    global exits, ans

    # m명의 모든 참가자들에 대해 이동을 진행합니다.
    for i in range(1, m + 1):
        # 이미 출구에 있는 경우 스킵합니다.
        if traveler[i] == exits:
            continue

        tx, ty = traveler[i]
        ex, ey = exits

        # 행이 다른 경우 행을 이동시켜봅니다.
        if tx != ex:
            nx, ny = tx, ty

            if ex > nx:
                nx += 1
            else:
                nx -= 1

            # 벽이 없다면 행을 이동시킬 수 있습니다.
            # 이 경우 행을 이동시키고 바로 다음 참가자로 넘어갑니다.
            if not board[nx][ny]:
                traveler[i] = (nx, ny)
                ans += 1
                continue

        # 열이 다른 경우 열을 이동시켜봅니다.
        if ty != ey:
            nx, ny = tx, ty

            if ey > ny:
                ny += 1
            else:
                ny -= 1

            # 벽이 없다면 행을 이동시킬 수 있습니다.
            # 이 경우 열을 이동시킵니다.
            if not board[nx][ny]:
                traveler[i] = (nx, ny)
                ans += 1
                continue


# 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 찾습니다.
def find_minimum_square():
    global exits, sx, sy, square_size
    ex, ey = exits

    # 가장 작은 정사각형부터 모든 정사각형을 만들어봅니다.
    for sz in range(2, n + 1):
        # 가장 좌상단 r 좌표가 작은 것부터 하나씩 만들어봅니다.
        for x1 in range(1, n - sz + 2):
            # 가장 좌상단 c 좌표가 작은 것부터 하나씩 만들어봅니다.
            for y1 in range(1, n - sz + 2):
                x2, y2 = x1 + sz - 1, y1 + sz - 1

                # 만약 출구가 해당 정사각형 안에 없다면 스킵합니다.
                if not (x1 <= ex and ex <= x2 and y1 <= ey and ey <= y2):
                    continue

                # 한 명 이상의 참가자가 해당 정사각형 안에 있는지 판단합니다.
                is_traveler_in = False
                for l in range(1, m + 1):
                    tx, ty = traveler[l]
                    if x1 <= tx and tx <= x2 and y1 <= ty and ty <= y2:
                        # 출구에 있는 참가자는 제외합니다.
                        if not (tx == ex and ty == ey):
                            is_traveler_in = True

                # 만약 한 명 이상의 참가자가 해당 정사각형 안에 있다면
                # sx, sy, square_size 정보를 갱신하고 종료합니다.
                if is_traveler_in:
                    sx = x1
                    sy = y1
                    square_size = sz

                    return


# 정사각형 내부의 벽을 회전시킵니다.
def rotate_square():
    # 우선 정사각형 안에 있는 벽들을 1 감소시킵니다.
    for x in range(sx, sx + square_size):
        for y in range(sy, sy + square_size):
            if board[x][y]:
                board[x][y] -= 1

    # 정사각형을 시계방향으로 90' 회전합니다.
    for x in range(sx, sx + square_size):
        for y in range(sy, sy + square_size):
            # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환을 진행합니다.
            ox, oy = x - sx, y - sy
            # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1)가 됩니다.
            rx, ry = oy, square_size - ox - 1
            # Step 3. 다시 (sx, sy)를 더해줍니다.
            next_board[rx + sx][ry + sy] = board[x][y]

    # next_board 값을 현재 board에 옮겨줍니다.
    for x in range(sx, sx + square_size):
        for y in range(sy, sy + square_size):
            board[x][y] = next_board[x][y]


# 모든 참가자들 및 출구를 회전시킵니다.
def rotate_traveler_and_exit():
    global exits

    # m명의 참가자들을 모두 확인합니다.
    for i in range(1, m + 1):
        tx, ty = traveler[i]
        # 해당 참가자가 정사각형 안에 포함되어 있을 때에만 회전시킵니다.
        if sx <= tx and tx < sx + square_size and sy <= ty and ty < sy + square_size:
            # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환을 진행합니다.
            ox, oy = tx - sx, ty - sy
            # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1)가 됩니다.
            rx, ry = oy, square_size - ox - 1
            # Step 3. 다시 (sx, sy)를 더해줍니다.
            traveler[i] = (rx + sx, ry + sy)

    # 출구에도 회전을 진행합니다.
    ex, ey = exits
    if sx <= ex and ex < sx + square_size and sy <= ey and ey < sy + square_size:
        # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환을 진행합니다.
        ox, oy = ex - sx, ey - sy
        # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) . (y, square_n - x - 1)가 됩니다.
        rx, ry = oy, square_size - ox - 1
        # Step 3. 다시 (sx, sy)를 더해줍니다.
        exits = (rx + sx, ry + sy)


for _ in range(k):
    # 모든 참가자를 이동시킵니다.
    move_all_traveler()

    # 모든 사람이 출구로 탈출했는지 판단합니다.
    is_all_escaped = True
    for i in range(1, m + 1):
        if traveler[i] != exits:
            is_all_escaped = False

    # 만약 모든 사람이 출구로 탈출했으면 바로 종료합니다.
    if is_all_escaped:
        break

    # 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 찾습니다.
    find_minimum_square()

    # 정사각형 내부의 벽을 회전시킵니다.
    rotate_square()
    # 모든 참가자들 및 출구를 회전시킵니다.
    rotate_traveler_and_exit()

print(ans)

ex, ey = exits
print(ex, ey)