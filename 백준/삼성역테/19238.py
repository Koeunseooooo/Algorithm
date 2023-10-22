import sys
from collections import deque
import copy

input = sys.stdin.readline

n, m, oil = map(int, input().strip().split())
board = []

for _ in range(n):
    board.append(list(map(int, input().strip().split())))

# 1을 -1로 바꿈 (벽으로 가정)
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == 1:
            board[i][j] = -1

driver_y, driver_x = map(int, input().strip().split())  # 차례로 y,x 좌표
driver = [driver_y - 1, driver_x - 1]

departures = copy.deepcopy(board)
arrivals = copy.deepcopy(board)


# d - departures(출발지)
# a - arrivals(도착지)
people = [[]]
for i in range(1, m + 1):
    d_y, d_x, a_y, a_x = map(int, input().strip().split())
    people.append([a_y - 1, a_x - 1])
    departures[d_y - 1][d_x - 1] = i
    arrivals[a_y - 1][a_x - 1] = 1

"""
백준이 태울 승객을 고를 때는 현재 위치에서 최단거리가 가장 짧은 승객을 고른다. 
그런 승객이 여러 명이면 그중 행 번호가 가장 작은 승객을, 그런 승객도 여러 명이면 그중 열 번호가 가장 작은 승객을 고른다. 
택시와 승객이 같은 위치에 서 있으면 그 승객까지의 최단거리는 0이다. 
연료는 한 칸 이동할 때마다 1만큼 소모된다. 
한 승객을 목적지로 성공적으로 이동시키면, 그 승객을 태워 이동하면서 소모한 연료 양의 두 배가 충전된다. 
이동하는 도중에 연료가 바닥나면 이동에 실패하고, 그 날의 업무가 끝난다. 
승객을 목적지로 이동시킨 동시에 연료가 바닥나는 경우는 실패한 것으로 간주하지 않는다.
"""

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def count_passenger():
    global departures
    cnt = 0
    for i in range(n):
        for j in range(n):
            if departures[i][j] > 0:
                cnt += 1
    return cnt


def debug_departures():
    print("디버깅 시작")
    for i in range(n):
        print(departures[i])
    print("디버깅 종료")


def choice_passenger():
    # 현재 남아있는 승객 계산
    # debug_departures()
    m = count_passenger()
    global driver
    q = deque()
    y, x = driver
    visited = [[-1] * n for _ in range(n)]
    q.append((y, x))
    visited[y][x] = 0
    distance = []
    while q:
        y, x = q.popleft()
        if departures[y][x] > 0:
            distance.append((visited[y][x], y, x))
        for dy, dx in d:
            Y = y + dy
            X = x + dx
            if (
                0 <= Y < n
                and 0 <= X < n
                and departures[Y][X] != -1
                and visited[Y][X] == -1
            ):
                visited[Y][X] = visited[y][x] + 1
                q.append((Y, X))

    if len(distance) < m:
        return False
    distance.sort(key=lambda x: (x[0], x[1], x[2]))
    choice = distance[0]
    return choice


def move_to_departures(choice):
    global oil
    global driver
    cost, y, x = choice
    oil -= cost
    if oil < 0:
        return False
    else:
        _choice = departures[y][x]
        departures[y][x] = 0
        driver = [y, x]
        return _choice


def move_to_arrivals(choice):
    global driver
    global oil
    q = deque()
    y, x = driver
    visited = [[-1] * n for _ in range(n)]
    q.append((y, x))
    visited[y][x] = 0
    distance = []

    while q:
        y, x = q.popleft()
        if arrivals[y][x] > 0 and people[choice] == [y, x]:
            distance = [visited[y][x], y, x]
            break
        for dy, dx in d:
            Y = y + dy
            X = x + dx
            if (
                0 <= Y < n
                and 0 <= X < n
                and arrivals[Y][X] != -1
                and visited[Y][X] == -1
            ):
                visited[Y][X] = visited[y][x] + 1
                q.append((Y, X))
    if len(distance) == 0:
        return False
    cost, y, x = distance
    oil -= cost  # 여기서 oil은 무조건 1이상 존재
    if oil < 0:
        return False
    driver = [y, x]
    oil += cost * 2
    return True


while 1:
    m = count_passenger()
    if m == 0:
        break
    choice = choice_passenger()
    # print("choice", choice)
    if not choice:
        print(-1)
        exit()
    _choice = move_to_departures(choice)
    # print("_choice", _choice)
    if not _choice:
        print(-1)
        exit()
    final = move_to_arrivals(_choice)
    # print("final", final)
    if not final:
        print(-1)
        exit()
print(oil)
