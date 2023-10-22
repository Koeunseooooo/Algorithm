from collections import deque

N, M = map(int, input().split())

board = []
result = 0
for _ in range(N):
    board.append(list(map(int, input().split())))

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def getStandartBlock(visited):
    standard = 0
    for i in range(len(visited)):
        for j in range(len(visited)):
            if visited[i][j]:
                if board[i][j] > 0:
                    standard = (i, j)
                    return standard


def getBiggestBlockGroup():
    candidate = []
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                visited = [[0] * N for _ in range(N)]
                q = deque()
                q.append((i, j))
                basic_block = board[i][j]
                visited[i][j] = 1
                rainbow = 0
                while q:
                    y, x = q.popleft()
                    for dy, dx in d:
                        Y = y + dy
                        X = x + dx
                        if 0 <= Y < N and 0 <= X < N and not visited[Y][X]:
                            # print(Y, X)
                            if board[Y][X] == 0:
                                q.append((Y, X))
                                visited[Y][X] = 1
                                rainbow += 1
                            if board[Y][X] == basic_block:
                                q.append((Y, X))
                                visited[Y][X] = 1

                cnt = 0
                for k in range(len(visited)):
                    cnt += visited[k].count(1)
                if cnt >= 2:
                    # visited 중복이 발생하는데 이걸 없앨 수 있는 방법 없을까.
                    y, x = getStandartBlock(visited)
                    candidate.append((cnt, rainbow, y, x, visited))
    if len(candidate) >= 1:
        candidate.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
        # for i in range(len(candidate)):
        #     print(candidate[i])
        return candidate[0]
    else:
        return False


def removeBlockGroup(visited):
    global result
    cnt, _, _, _, visited = visited
    for i in range(len(visited)):
        for j in range(len(visited)):
            if visited[i][j]:
                board[i][j] = -2
    # for i in range(len(board)):
    #     print(board[i])
    result += cnt * cnt
    # print(result)


def gravity():
    global board
    for i in range(N - 2, -1, -1):
        for j in range(N):
            if board[i][j] > -1:
                row = i
                while True:
                    if 0 <= row + 1 < N and board[row + 1][j] == -2:
                        # 인덱스 범위를 만족하면서 빈칸(=-2)이면 아래로 다운
                        board[row + 1][j] = board[row][j]
                        board[row][j] = -2
                        row += 1
                    else:
                        break
    # for i in range(len(board)):
    #     print(board[i])
    # print("---")


def rotate_270():
    global board
    new_board = [[0] * N for _ in range(N)]
    for i in range(len(board)):
        for j in range(len(board)):
            new_board[N - j - 1][i] = board[i][j]
    # board = new_board
    board = new_board[:]
    # for i in range(len(board)):
    #     print(board[i])
    # print("---")


def print_board(num):
    print("#", num)
    for i in range(len(board)):
        print(board[i])


while 1:
    selectedBlockGroup = getBiggestBlockGroup()
    # print_board(1)
    if not selectedBlockGroup:
        break
    # print(selectedBlockGroup)
    removeBlockGroup(selectedBlockGroup)
    # print_board(2)
    gravity()
    # print_board(3)
    rotate_270()
    # print_board(4)
    gravity()
    # print_board(5)


print(result)
