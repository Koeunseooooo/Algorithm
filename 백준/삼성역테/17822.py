import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().strip().split())


arr = [deque(int(x) for x in input().split()) for _ in range(n)]

comm = []

for _ in range(k):
    comm.append(list(map(int, input().strip().split())))


def is_adjacent(arr):
    # 바로 0으로 바꿔주면 안되었던 거였다..
    have_to_remove = []
    # 가로(= 같은 원 내에서 인접한 애들) 확인
    for i in range(n):
        for j in range(m):
            c_value = arr[i][j]
            next_idx = (j + 1) % m  # 인덱스가 리스트 길이를 벗어나지 않도록 순환
            next_value = arr[i][next_idx]
            if next_value != 0 and c_value != 0 and c_value == next_value:
                flag = 1
                have_to_remove.append((i, j))
                have_to_remove.append((i, next_idx))
                # arr[i][j] = 0
                # arr[i][next_idx] = 0

    # 세로(= 옆은 원 내에서 인접한 애들) 확인
    # arr = list(map(list, zip(*arr)))
    for j in range(m):
        for i in range(n - 1):
            c_value = arr[i][j]
            next_value = arr[i + 1][j]
            if next_value != 0 and c_value != 0 and c_value == next_value:
                have_to_remove.append((i, j))
                have_to_remove.append((i + 1, j))

    # 중복 제거 및 수 지우기
    have_to_remove = list(set(have_to_remove))

    for i in range(len(have_to_remove)):
        x, y = have_to_remove[i]
        arr[x][y] = 0

    if len(have_to_remove) == 0:
        # 인접하면서 수가 같은 것이 없다.
        cnt = 0
        total_sum = 0
        # 이차원 배열 합 구하는 거 더 간단히 할 수 없을까?
        for i in range(n):
            total_sum += sum(arr[i])
            cnt += arr[i].count(0)
        total_avg = total_sum / (n * m - cnt)
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    continue
                if arr[i][j] > total_avg:
                    arr[i][j] -= 1
                elif arr[i][j] < total_avg:
                    arr[i][j] += 1
    # print("-----")
    # for i in range(len(arr)):
    #     print(arr[i])
    return arr


for c in comm:
    x, d, k = c
    # 회전하기
    result = 0
    for i in range(n):
        result += sum(arr[i])
        if (i + 1) % x == 0:
            if d == 0:
                arr[i].rotate(k)
            else:
                arr[i].rotate(-k)
    if result != 0:
        # 인접한 수를 찾는다
        arr = is_adjacent(arr)
    else:
        break

total_sum = sum(sum(row) for row in arr)
print(total_sum)
