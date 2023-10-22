import sys

input = sys.stdin.readline

board = []
for _ in range(5):
    board.append(list(map(int, input().strip().split())))

speak = []
for _ in range(5):
    speak.append(list(map(int, input().strip().split())))

bingo = [[0] * 5 for _ in range(5)]


def check_row():
    res = 0
    for i in range(5):
        cnt = 0
        for j in range(5):
            if bingo[i][j] == 1:
                cnt += 1
        if cnt == 5:
            res += 1
    return res


def check_col():
    res = 0
    for i in range(5):
        cnt = 0
        for j in range(5):
            if bingo[j][i] == 1:
                cnt += 1
        if cnt == 5:
            res += 1
    return res


def check_dia():
    res = 0
    # 오->왼
    cnt = 0
    for i in range(5):
        if bingo[i][5 - i - 1] == 1:
            cnt += 1
    if cnt == 5:
        res += 1
    # 왼->오
    cnt = 0
    for i in range(5):
        if bingo[i][i] == 1:
            cnt += 1
    if cnt == 5:
        res += 1
    return res


cnt = 0
for i in range(5):
    for j in range(5):
        s = speak[i][j]
        for y in range(5):
            for x in range(5):
                if board[y][x] == s:
                    cnt = 0
                    bingo[y][x] = 1
                    # 가로, 세로, 대각선 확인해서 카운팅 (중복 방지?-시간초과...)
                    cnt += check_row()  # 가로
                    cnt += check_col()  # 세로
                    cnt += check_dia()  # 대각선
                    if cnt >= 3:
                        print(
                            i * 5 + j + 1
                        )  # 굳이 이렇게 안하고 사회자가 몇 번 부르는지 체크용 변수를 따로 만들어도 상관없을 것 같다.
                        exit()  # 실제 코테에서는 exit 사용 x. 함수화 시켜서 return 하는 것을 권장


# 오.. 세로 빙고 확인할 때 아래와 같이 할 수 도 있음
def sero(visited):  # 세로 빙고만 확인
    cnt = 0
    temp = list(map(list, zip(*visited)))[::-1]  # zip을 사용한 시계 방향 회전
    for col in temp:  # 이를 통해 가로 빙고 확인할 때처럼 쉽게 확인 가능
        if sum(col) == 5:
            cnt += 1
    return cnt
