import sys

input = sys.stdin.readline
n = int(input())


d = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 시계방향


def check_area(pts):
    min_x = min(pts, key=lambda x: x[0])[0]
    max_x = max(pts, key=lambda x: x[0])[0]
    min_y = min(pts, key=lambda x: x[1])[1]
    max_y = max(pts, key=lambda x: x[1])[1]
    return (max_x - min_x) * (max_y - min_y)


for _ in range(n):
    commands = input()
    # FFLF
    x, y = 0, 0
    cur_idx = 0  # 방향 0:북 1:동 2:서 3:남
    pts = [(x, y)]
    for c in commands:
        if c == "F":
            x = x + d[cur_d][1]
            y = y + d[cur_d][0]
            pts.append((x, y))
        elif c == "B":
            x = x - d[cur_d][1]
            y = y - d[cur_d][0]
            pts.append((x, y))
        elif c == "L":
            cur_d = (cur_d + 3) % 4
        elif c == "R":
            cur_d = (cur_d + 1) % 4

    # print(pts)
    print(check_area(pts))
