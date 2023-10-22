import sys

input = sys.stdin.readline

n, m, x, y, k = map(int, input().strip().split())
# 0<=x<n-1
# 0<=y<m-1

d = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # y,x 기준 차례대로 동,서,북,남
maps = []
for _ in range(n):
    maps.append(list(map(int, input().strip().split())))

cmds = list(map(int, input().strip().split()))

dice = [0, 0, 0, 0, 0, 0]


def update_dice(d, dice):  # 방향, 주사위
    one, two, three, four, five, six = (
        dice[0],
        dice[1],
        dice[2],
        dice[3],
        dice[4],
        dice[5],
    )
    if d == 0:  # 동쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = (
            four,
            two,
            one,
            six,
            five,
            three,
        )
    elif d == 1:  # 서쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = (
            three,
            two,
            six,
            one,
            five,
            four,
        )
    elif d == 2:  # 북쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = (
            five,
            one,
            three,
            four,
            six,
            two,
        )
    else:  # 남쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = (
            two,
            six,
            three,
            four,
            one,
            five,
        )


for c in cmds:
    c -= 1  # 명령 방향
    dx, dy = d[c]
    x = x + dx
    y = y + dy
    if 0 <= x < n and 0 <= y < m:
        update_dice(c, dice)
        if maps[x][y] != 0:
            dice[5] = maps[x][y]
            maps[x][y] = 0
        else:
            maps[x][y] = dice[5]
        print(dice[0])
    else:
        #  만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.
        x = x - dx
        y = y - dy
