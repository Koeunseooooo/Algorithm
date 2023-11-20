# from collections import deque

# n, m = map(int, input().split())  # n이 y축

# arr = []
# for _ in range(n):
#     arr.append(list(map(int, input().split())))

# d = [(0, -1), (0, 1), (1, 0), (-1, 0)]


# def bfs():
#     q = deque()
#     q.append((0, 0))
#     visited[0][0] = 1
#     cheese = []
#     while q:
#         y, x = q.popleft()
#         for dy, dx in d:
#             Y = y + dy
#             X = x + dx
#             if 0 <= Y < n and 0 <= X < m and not visited[Y][X]:
#                 visited[Y][X] = 1
#                 if arr[Y][X] == 0:
#                     q.append((Y, X))
#                 else:  # 공기와 맞닿은 치즈가 있다면
#                     cheese.append((Y, X))
#     # 끝나고 공기와 맞닿은 치즈 없애주기
#     for y, x in cheese:
#         arr[y][x] = 0
#     return len(cheese)


# meltCnt = 0
# for i in range(n):
#     meltCnt += sum(arr[i])  # 치즈 총 개수

# time = 0
# while True:
#     visited = [[0] * m for _ in range(n)]
#     cnt = bfs()
#     meltCnt -= cnt
#     time += 1
#     if meltCnt == 0:
#         print(time)
#         print(cnt)
#         break


def change_num(n):
    if n == 0:
        return ""
    return change_num(n // 3) + str(n % 3)


print(change_num(437674))
