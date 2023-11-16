T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    result = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            sy, sx = i, j
            temp = 0
            for mi in range(m):
                for mj in range(m):
                    my = sy + mi
                    mx = sx + mj
                    temp += arr[my][mx]
            if result < temp:
                result = temp
    print("#{} {}".format(test_case, result))
