def nqueens(level):  # 지금 몇 번째 행을 보고 있는지 확인
    global n, cnt
    if level == n:
        cnt += 1  # 경우의 수 1 증가
        return
    for i in range(n):
        if visited[i] == 1:
            continue
        if rup[level + i] == 1:
            continue
        if rdown[level - i + n - 1] == 1:
            continue

        visited[i] = 1
        rup[level + i] = 1
        rdown[level - i + n - 1] = 1

        nqueens(level + 1)

        visited[i] = 0
        rup[level + i] = 0
        rdown[level - i + n - 1] = 0


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    cnt = 0
    visited = [0] * n  # 행, 열
    rup = [0 for i in range(2 * n - 1)]
    rdown = [0 for i in range(2 * n - 1)]
    nqueens(0)
    print("#{} {}".format(test_case, cnt))
