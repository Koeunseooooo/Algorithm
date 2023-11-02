from collections import deque


def haveKey(cur_key, door):
    value = cur_key & (1 << (ord(door) - ord("A")))
    return True if value else False


def bfs(y, x):
    q = deque()
    q.append((y, x, 0, 0))  # 현재 위치 y, x, 갖고 있는 키(비트로 관리), 거리
    visited = [[[False] * (1 << 6) for _ in range(50)] for _ in range(50)]
    visited[y][x][0] = True

    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while q:
        y, x, cnt, key = q.popleft()
        if board[y][x] == "1":
            return cnt

        for dy, dx in d:
            Y = y + dy
            X = x + dx
            if 0 <= Y < n and 0 <= X < m:
                if not visited[Y][X][key]:
                    if board[Y][X] == "." or board[Y][X] == "1":
                        visited[Y][X][key] = True
                        q.append((Y, X, cnt + 1, key))
                    elif "a" <= board[Y][X] <= "f":
                        temp_key = key | (1 << (ord(board[Y][X]) - ord("a")))
                        visited[Y][X][temp_key] = True
                        q.append((Y, X, cnt + 1, temp_key))
                    elif "A" <= board[Y][X] <= "Z":
                        if haveKey(key, board[Y][X]):
                            visited[Y][X][key] = 1
                            q.append((Y, X, cnt + 1, key))
    return -1


n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(input().rstrip()))
for i in range(n):
    for j in range(m):
        if board[i][j] == "0":
            sy, sx = i, j
            board[i][j] = "."

print(bfs(sy, sx))
