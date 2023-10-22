# import sys
# import copy

# input = sys.stdin.readline

# n, m, k = map(int, input().strip().split())
# d = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]  # 위 아래 왼쪽 오른쪽

# # sea 배열 기준 상어 위치 정보
# sea = []
# for _ in range(n):
#     sea.append(list(map(int, input().strip().split())))

# s_dir = [0] + list(map(int, input().strip().split()))  # 각 상어의 현재 방향 (인덱스==상어번호)

# smell = [[[0, 0] for _ in range(n)] for _ in range(n)]  # 냄새와 남은 초(k) 저장해두는 배열

# dir = [[]]  # 각 상어의 인접 방향 탐색 우선 순위를 적어놓은 2차원 배열


# for i in range(m):
#     arr = [[]]
#     for j in range(4):
#         tmp = [0] + list(map(int, input().strip().split()))
#         arr.append(tmp)
#     dir.append(arr)


# def move():
#     global out
#     temp = [[[0, 0] for _ in range(n)] for _ in range(n)]
#     for shark in range(1, 5):
#         y, x = -1, -1
#         for j in range(n):
#             for k in range(n):
#                 if sea[j][k] == shark:
#                     y = j
#                     x = k
#         if y == -1 and x == -1:  # 바다에 해당 상어가 없음 -> continue
#             continue
#         is_empty = 4  # 인접 칸 중에 냄새 없는 칸 존재 여부 판단 (false로 초기화)
#         for i in range(1, 5):
#             dy, dx = d[i]
#             Y = y + dy
#             X = x + dx
#             if 0 > Y or n <= Y or 0 > X or n <= X:
#                 is_empty -= 1
#                 continue
#             if smell[Y][X][0] != 0:
#                 is_empty -= 1
#                 continue
#             else:
#                 cur_dir = dir[shark][s_dir[shark]]
#                 for i in range(1, 5):
#                     cur_d_idx = cur_dir[i]
#                     dy, dx = d[cur_d_idx]
#                     Y = y + dy
#                     X = x + dx

#                     if Y < 0 or n <= Y or X < 0 or n <= X:
#                         continue
#                     if smell[Y][X][0] != 0:
#                         continue
#                     # 이동하려는 칸에 이미 상어가 있다면 대소 비교 후 이동
#                     if sea[Y][X] != 0:
#                         if shark > sea[Y][X]:  # (현재)이동 대상이 더 크다면 잡아먹힘
#                             sea[y][x] = 0
#                             out += 1
#                             break

#                     # # 냄새 확장1
#                     temp[Y][X] = [shark, k + 1]
#                     # smell[Y][X] = [shark, k]

#                     # 상어 이동
#                     sea[y][x] = 0  # 기존 위치는 원래대로 두고
#                     sea[Y][X] = shark  # 이동 위치에 자신의 번호를 기록함
#                     # 상어 방향 저장
#                     s_dir[shark] = cur_d_idx
#                     break
#                 break
#         if not is_empty:
#             for d_idx in range(1, 5):
#                 dy, dx = d[d_idx]
#                 Y = y + dy
#                 X = x + dx
#                 if 0 <= Y < n and 0 < X < n:
#                     if smell[Y][X][0] == shark:  # 해당 조건에는 무조건 '한 번' 걸려야 함
#                         # 이동하려는 칸에 이미 상어가 있다면 대소 비교 후 이동
#                         if sea[Y][X] != 0:
#                             if shark > sea[Y][X]:  # (현재)이동 대상이 더 크다면 본인이 잡아먹힘
#                                 sea[y][x] = 0
#                                 out += 1
#                                 continue
#                         # # 냄새 확장2
#                         temp[Y][X] = [shark, k + 1]
#                         # smell[Y][X] = [shark, k]
#                         # 상어 이동
#                         sea[y][x] = 0  # 기존 위치는 0으로 초기화
#                         sea[Y][X] = shark  # 이동 위치에 자신의 번호 기록
#                         # 상어 방향 저장
#                         s_dir[shark] = d_idx
#                         break
#     # 냄새 확장
#     for i in range(len(smell)):
#         for j in range(len(smell)):
#             if temp[i][j][0]:
#                 if sea[i][j] == 0 or sea[i][j] == temp[i][j][0]:  # 본인이거나 아무 상어도 없을 때
#                     smell[i][j] = [temp[i][j][0], k + 1]


# def smell_down():
#     for i in range(len(smell)):
#         for j in range(len(smell)):
#             if smell[i][j][0] != 0:
#                 smell[i][j][1] -= 1
#             if smell[i][j][1] == 0:
#                 smell[i][j] = [0, 0]  # 냄새 사라짐


# time = 0
# out = 0

# # init
# for i in range(n):
#     for j in range(n):
#         if sea[i][j] != 0:
#             smell[i][j] = [sea[i][j], k]

# while True:
#     if time >= 1000:
#         time = -1
#         break
#     if out == m - 1:
#         break
#     move()
#     smell_down()
#     for i in range(len(sea)):
#         print(sea[i])
#     for j in range(len(smell)):
#         print(smell[j])
#     print(s_dir)
#     print("-----")
#     time += 1

# print(time)
# 졌잘싸..

import copy

n, m, k = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(n)]
smell = [[[0, 0] for _ in range(n)] for _ in range(n)]

s_dir = [0] + list(map(int, input().split()))

dir = [[]]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(m):
    array = []
    for j in range(4):
        array.append(list(map(int, input().split())))
    dir.append(array)


def move(sea):
    global out
    s = copy.deepcopy(sea)
    for i in range(n):
        for j in range(n):
            if sea[i][j] == 0:
                continue
            s_n = s[i][j]
            d = s_dir[s_n]
            x, y = i, j
            what = False
            for p in range(4):
                nd = dir[s_n][d - 1][p]
                nx = x + dx[nd - 1]
                ny = y + dy[nd - 1]
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if smell[nx][ny][1] == 0:
                    if s[nx][ny] == 0:
                        s[nx][ny] = sea[x][y]
                        s[x][y] = 0
                    else:
                        if s[nx][ny] > s[x][y]:
                            s[nx][ny] = sea[x][y]
                        out += 1
                        s[x][y] = 0
                    s_dir[s_n] = nd
                    what = True
                    break
            if what:
                continue

            for p in range(4):
                nd = dir[s_n][d - 1][p]
                nx = x + dx[nd - 1]
                ny = y + dy[nd - 1]
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if smell[nx][ny][1] == s_n:
                    s[nx][ny] = sea[x][y]
                    s[x][y] = 0
                    s_dir[s_n] = nd
                    break
    return s


def s_smell(k):
    for i in range(n):
        for j in range(n):
            if sea[i][j] != 0:
                smell[i][j][0], smell[i][j][1] = k, sea[i][j]


def smell_down():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] == 0:
                continue
            if smell[i][j][0] == 1:
                smell[i][j][0], smell[i][j][1] = 0, 0
            else:
                smell[i][j][0] -= 1


count = 0
out = 0
while True:
    if count >= 1000:
        count = -1
        break
    s_smell(k)
    sea = copy.deepcopy(move(sea))
    count += 1
    if out == m - 1:
        break
    smell_down()

print(count)
