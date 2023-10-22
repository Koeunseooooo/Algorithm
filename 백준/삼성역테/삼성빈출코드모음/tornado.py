arr = [[0] * 5 for _ in range(5)]


def tornado():
    global arr
    d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    y = len(arr) // 2
    x = len(arr) // 2
    num = 0  # 칸에 채워넣을 값
    dist = 1
    d_idx = 0  # 서 남 동 북 순서
    move_count = 0  # 2가 되면 dist 길이가 1 늘어나고 move_count는 다시 0으로 초기화
    while True:
        for _ in range(dist):
            dy, dx = d[d_idx]
            Y = dy + y
            X = dx + x
            if (Y, X) == (0, -1):  # 0행 -1열이 토네이도가 모두 끝나고 나서의 위치임
                return
            num += 1
            arr[Y][X] = num
            y = Y
            x = X
        move_count += 1
        d_idx = (d_idx + 1) % 4
        if move_count == 2:
            dist += 1
            move_count = 0


# tornado()
# for i in range(5):
#     print(arr[i])

arr = [[0] * 5 for _ in range(5)]


#######
def tornado_reverse():
    global arr
    n = len(arr)
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    y, x = 0, 0
    num = 0  # 칸에 채워넣을 값
    dist = n - 1
    d_idx = 0  # 동 남 서 북 순서
    move_count = 0  # 2가 되면 dist 길이가 1 줄어들고 move_count는 다시 0으로 초기화
    out = 0  # 가장 겉부분은 4번 방향을 바꿔야만 dist길이가 1 줄어들음
    while True:
        for _ in range(dist):
            dy, dx = d[d_idx]
            Y = dy + y
            X = dx + x
            num += 1
            arr[Y][X] = num
            if (Y, X) == (n // 2, n // 2):  # 0행 -1열이 토네이도가 모두 끝나고 나서의 위치임
                return
            y = Y
            x = X
        d_idx = (d_idx + 1) % 4
        if out == 0:
            out += 1
            if out == 4:
                dist -= 1
            out == -1
            continue
        move_count += 1
        if move_count == 2:
            dist -= 1
            move_count = 0


tornado_reverse()
for i in range(5):
    print(arr[i])
