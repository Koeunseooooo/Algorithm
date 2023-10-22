# import sys
# from collections import deque

# input = sys.stdin.readline

# n = int(input())
# arr = []
# shark = [0, 0]
# shark_size = 2
# fish_num = 0
# d = [(1, 0), (-1, 0), (0, -1), (0, 1)]  # 상 하 좌 우
# for _ in range(n):
#     arr.append(list(map(int, input().strip().split())))

# for i in range(n):
#     for j in range(n):
#         if arr[i][j] == 9:
#             shark[0] = i  # y축
#             shark[1] = j  # x축
#             arr[i][j] = 0  # 아기 상어 위치 0으로 초기화 잊지 말자 . .

# MAX = 1e9


# # 현재 아기 상어 위치를 기준으로 각 물고기까지의 거리를 반환
# def bfs():
#     global cur_t
#     global shark_size
#     global shark
#     global fish_num
#     visited = [[0] * n for _ in range(n)]
#     q = deque()
#     y, x = shark[0], shark[1]
#     q.append((y, x))
#     visited[y][x] = 1

#     while q:
#         y, x = q.popleft()
#         # 상하좌우 탐색
#         for dy, dx in d:
#             Y = y + dy
#             X = x + dx
#             if (
#                 0 <= Y < n
#                 and 0 <= X < n
#                 and not visited[Y][X]
#                 and arr[Y][X] <= shark_size
#             ):
#                 q.append((Y, X))
#                 visited[Y][X] = visited[y][x] + 1
#                 # if arr[Y][X] != 0 and arr[Y][X] < shark_size:
#                 #     print("!")
#                 #     candidate.append((Y, X))
#                 #     if min_distance == MAX:
#                 #         min_distance = visited[Y][X]  # flag 변수처럼 한 번만 수행해주면 되므로 조건처리

#         # print(visited)
#     return visited


# # 먹을 물고기 찾기
# def solve(visited):
#     y, x = 0, 0
#     min_distance = MAX  # 최단거리 갱신용 변수
#     for i in range(n):
#         for j in range(n):
#             if visited[i][j] != 0 and 1 <= arr[i][j] < shark_size:
#                 if visited[i][j] < min_distance:
#                     min_distance = visited[i][j] - 1
#                     y, x = i, j
#     if min_distance == MAX:
#         return False
#     else:
#         return (y, x, min_distance)


# cur_t = 0
# while True:
#     result = solve(bfs())
#     if not result:
#         print(cur_t)
#         break
#     else:
#         y, x, min_distance = result
#         shark[0] = y
#         shark[1] = x
#         fish_num += 1
#         cur_t += min_distance
#         arr[y][x] = 0
#     if shark_size >= fish_num:
#         fish_num = 0
#         shark_size += 1
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = list(list(map(int, input().split())) for _ in range(N))

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
INF = 1e9
shark_size = 2
now_y, now_x = 0, 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            now_y, now_x = i, j
            graph[i][j] = 0


def bfs():
    q = deque()
    q.append((now_y, now_x))
    # 방문 여부
    visited = [[-1] * N for _ in range(N)]
    visited[now_y][now_x] = 0
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            Y = y + dy
            X = x + dx
            if 0 <= Y < N and 0 <= X < N:
                if shark_size >= graph[Y][X] and visited[Y][X] == -1:
                    visited[Y][X] = visited[y][x] + 1
                    q.append((Y, X))
    return visited


def solve(visited):
    y, x = 0, 0
    min_distance = INF
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            # for i in range(N):
            #     for j in range(N):
            if visited[i][j] != -1 and 1 <= graph[i][j] < shark_size:
                if visited[i][j] < min_distance:
                    min_distance = visited[i][j]
                    y, x = i, j
                elif visited[i][j] == min_distance:
                    y, x = i, j
    if min_distance == INF:
        return False
    else:
        return y, x, min_distance


answer = 0
food_num = 0
while 1:
    result = solve(bfs())
    if not result:
        print(answer)
        break
    else:
        now_y, now_x = result[0], result[1]
        answer += result[2]
        graph[now_y][now_x] = 0
        food_num += 1
    if food_num >= shark_size:
        shark_size += 1
        food_num = 0
