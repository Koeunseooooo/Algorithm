import sys

input = sys.stdin.readline

N = int(input())
infos = [[] for _ in range((N * N) + 1)]
classroom = [[0] * N for _ in range(N)]
order = []
for _ in range(N * N):
    num, a, b, c, d = map(int, input().strip().split())
    infos[num] = [a, b, c, d]
    order.append(num)

d = [(0, -1), (0, 1), (1, 0), (-1, 0)]

result = 0
# 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000
satisfaction = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}


def step(i, info):
    global result
    blank = [[0] * N for _ in range(N)]
    likes = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if not classroom[y][x]:
                for dy, dx in d:
                    Y = y + dy
                    X = x + dx
                    if 0 <= Y < N and 0 <= X < N:
                        if classroom[Y][X] == 0:
                            blank[y][x] += 1
                        if classroom[Y][X] in info:
                            likes[y][x] += 1

    # 최댓값 찾기 (위의 for문에서 바로 최댓값을 찾을 순 없을까?)
    MAX = 0
    for y in range(N):
        for x in range(N):
            if MAX < likes[y][x]:
                MAX = likes[y][x]
    max_likes = []
    # 최댓값을 갖는 인덱스 찾기 (이것도 동일)
    for y in range(N):
        for x in range(N):
            if MAX == likes[y][x] and not classroom[y][x]:
                max_likes.append((y, x, blank[y][x]))
    max_likes.sort(key=lambda x: (-x[2], x[0], x[1]))
    y, x, _ = max_likes[0]
    classroom[y][x] = i


def get_satisfaction(classroom):
    global result
    for y in range(len(classroom)):
        for x in range(len(classroom)):
            cnt = 0
            for dy, dx in d:
                Y = y + dy
                X = x + dx
                if 0 <= Y < N and 0 <= X < N:
                    if classroom[Y][X] in infos[classroom[y][x]]:
                        cnt += 1
            result += satisfaction[cnt]
    return result


for i in order:
    info = infos[i]
    step(i, info)
print(get_satisfaction(classroom))
