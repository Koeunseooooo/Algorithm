# 효율성 0점
def solution(board, skill):
    answer = 0
    for t, r1, c1, r2, c2, d in skill:
        flag = 1
        if t == 1:
            flag = -1
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                board[i][j] += d * flag
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1
    return answer


# 2차원 배열 누적합
# 참고 : https://kimjingo.tistory.com/155
def solution(board, skill):
    answer = 0
    temp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for t, r1, c1, r2, c2, d in skill:
        temp[r1][c1] += d if t == 2 else -d
        temp[r1][c2 + 1] += -d if t == 2 else d
        temp[r2 + 1][c1] += -d if t == 2 else d
        temp[r2 + 1][c2 + 1] += d if t == 2 else -d

    for i in range(len(temp) - 1):
        for j in range(len(temp[0]) - 1):
            temp[i][j + 1] += temp[i][j]

    for j in range(len(temp[0]) - 1):
        for i in range(len(temp) - 1):
            temp[i + 1][j] += temp[i][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += temp[i][j]
            if board[i][j] > 0:
                answer += 1
    # print(board)

    return answer
