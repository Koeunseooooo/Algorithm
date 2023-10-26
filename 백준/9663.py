n = int(input())

board = [[0] * n for _ in range(n)]

cnt = 0


def backtracking(num, board):
    global n
    if num == n:
        cnt += 1
        return


backtracking(0, board)
