# import sys
# from collections import deque

# input = sys.stdin.readline


# # 세로, 가로
# n, m = map(int, input().strip().split())
# board = [list(input().strip()) for _ in range(n)]

# s = []
# for i in range(n):
#     for j in range(m):
#         if board[i][j] == "o":
#             s.append((i, j))

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]


# def bfs():
#     q = deque()
#     q.append((s[0][0], s[0][1], s[1][0], s[1][1], 0))  # 동전1 좌표, 동전2좌표, 현재 카운트
#     while q:
#         x1, y1, x2, y2, cnt = q.popleft()

#         if cnt >= 10:
#             return -1

#         for i in range(4):
#             X1 = x1 + dx[i]
#             Y1 = y1 + dy[i]
#             X2 = x2 + dx[i]
#             Y2 = y2 + dy[i]
#             if 0 <= X1 < n and 0 <= Y1 < m and 0 <= X2 < n and 0 <= Y2 < m:
#                 if board[X1][Y1] == "#":
#                     X1 = x1
#                     Y1 = y1
#                 if board[X2][Y2] == "#":
#                     X2 = x1
#                     Y2 = y2
#                 q.append((X1, Y1, X2, Y2, cnt + 1))
#             elif 0 <= X1 < n and 0 <= Y1 < m:  # coin2가 떨어진 경우
#                 return cnt + 1
#             elif 0 <= X2 < n and 0 <= Y2 < m:  # coin1이 떨어진 경우
#                 return cnt + 1
#             else:
#                 continue  # 둘 다 떨어진 경우는 무시
#     return -1


# print(bfs())
from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs():
    while coin:
        x1, y1, x2, y2, cnt = coin.popleft()

        if cnt >= 10:
            return -1

        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]

            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m:
                # 벽이라면
                if board[nx1][ny1] == "#":
                    nx1, ny1 = x1, y1
                if board[nx2][ny2] == "#":
                    nx2, ny2 = x2, y2
                coin.append((nx1, ny1, nx2, ny2, cnt + 1))
            elif 0 <= nx1 < n and 0 <= ny1 < m:  # coin2가 떨어진 경우
                return cnt + 1
            elif 0 <= nx2 < n and 0 <= ny2 < m:  # coin1가 떨어진 경우
                return cnt + 1
            else:  # 둘 다 빠진 경우 무시
                continue

    return -1


if __name__ == "__main__":
    n, m = map(int, input().split())

    coin = deque()
    board = []
    temp = []
    for i in range(n):
        board.append(list(input().strip()))
        for j in range(m):
            if board[i][j] == "o":
                temp.append((i, j))

    coin.append((temp[0][0], temp[0][1], temp[1][0], temp[1][1], 0))

    print(bfs())
