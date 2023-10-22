def rotate_180(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]  # 정사각형이라고 가정

    for r in range(N):
        for c in range(N):
            ret[N - 1 - r][N - 1 - c] = m[r][c]
    return ret


a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(rotate_180(a))


def rotate_90_origin(m):
    n = len(m)
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[j][n - 1 - i] = m[i][j]
    return result


print(rotate_90_origin(a))


def rotate_90_zip(m):
    temp = zip(*m[::-1])
    return [list(t) for t in temp]


print(rotate_90_zip(a))
