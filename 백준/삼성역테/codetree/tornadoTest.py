def solution(n):
    if n == 1:
        return [[1]]

    answer = [[0 for j in range(n)] for i in range(n)]  # 배열 초기화

    x = 0
    y = 0
    d_idx=0

    for i in range(n * n):
        answer[x][y] = i + 1
        if d_idx == 0:
            y += 1
            if y == n - 1 or answer[x][y + 1] != 0:  # 맨 끝에 도달했거나 가려는 곳에 이미 값이 있으면 방향 전환
                d_idx = 1
        elif d_idx == 1:
            x += 1
            if x == n - 1 or answer[x + 1][y] != 0:
                d_idx = 2
        elif d_idx == 2:
            y -= 1
            if y == 0 or answer[x][y - 1] != 0:
                d_idx = 3
        elif d_idx == 3:
            x -= 1
            if x == n - 1 or answer[x - 1][y] != 0:
                d_idx = 0

    return answer


arr=solution(5)
for i in range(len(arr)):
    print(arr[i])
