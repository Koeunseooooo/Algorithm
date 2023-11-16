T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]

    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    y, x = 0, 0
    cur = 1
    cur_d = 0
    while True:
        arr[y][x] = cur
        cur += 1
        dy, dx = d[cur_d]
        Y = y + dy
        X = x + dx
        if 0 <= Y < n and 0 <= X < n:
            if arr[Y][X] != 0:
                cur_d = (cur_d + 1) % 4
                dy, dx = d[cur_d]
                y = y + dy
                x = x + dx
            else:
                y = Y
                x = X
        else:
            cur_d = (cur_d + 1) % 4
            dy, dx = d[cur_d]
            y = y + dy
            x = x + dx

        flag = 0
        for i in range(n):
            for j in range(n):
                if arr[i][j] == 0:
                    flag = 1
                    break
        if not flag:
            break
    print("#{}".format(test_case))
    for a in arr:
        a = map(str, a)
        print(" ".join(a))
