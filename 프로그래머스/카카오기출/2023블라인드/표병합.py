def solution(commands):
    answer = []
    merged = [[(i, j) for j in range(50)] for i in range(50)]
    board = [["EMPTY"] * 50 for _ in range(50)]
    for command in commands:
        command = command.split(" ")
        if command[0] == "UPDATE":
            if len(command) == 4:
                r, c, value = int(command[1]) - 1, int(command[2]) - 1, command[3]
                x, y = merged[r][c]
                board[x][y] = value
            elif len(command) == 3:
                value1, value2 = command[1], command[2]
                for i in range(50):
                    for j in range(50):
                        if board[i][j] == value1:
                            board[i][j] = value2
        elif command[0] == "MERGE":
            r1, c1, r2, c2 = (
                int(command[1]) - 1,
                int(command[2]) - 1,
                int(command[3]) - 1,
                int(command[4]) - 1,
            )
            x1, y1 = merged[r1][c1]
            x2, y2 = merged[r2][c2]
            if board[x1][y1] == "EMPTY":
                board[x1][y1] = board[x2][y2]
            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x2, y2):
                        merged[i][j] = (x1, y1)
        elif command[0] == "UNMERGE":
            r, c = int(command[1]) - 1, int(command[2]) - 1
            x, y = merged[r][c]
            tmp = board[x][y]
            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x, y):
                        merged[i][j] = (i, j)
                        board[i][j] = "EMPTY"
            board[r][c] = tmp
        elif command[0] == "PRINT":
            r, c = int(command[1]) - 1, int(command[2]) - 1
            x, y = merged[r][c]
            answer.append(board[x][y])
    return answer


from collections import deque

UPDATE = "UPDATE"
MERGE = "MERGE"
UNMERGE = "UNMERGE"
PRINT = "PRINT"
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

""" 
아래는 본인이 푼 코드

초기 접근 방식 : 
merge에 대한 정보를 group이란 2차원 배열에서 관리한다
병합==그룹핑하는 과정이라고 봐서 처음엔 모두 0으로 초기화하고
새롭게 병합을 할 때마다 식별자인 id를 부여해서 관리했는데 로직 과정에서 잘못 된 부분이 있는 듯하다.

다른 사람들의 풀이는 group 배열을 초기화할 때 자기 좌표로 하고, merge하면 기준이 되는 좌표로 갱신되는 형태다
다른 사람들의 풀이를 보니까 union-find 유형이라는 게 바로 와닿았다. (왜냐하면 기준이 되는 좌표로 갱신된다는 말이 곧 부모노드를 찾는 과정과 똑같기 때문)
입력크기가 작다고 해서 무조건 완탐, for문이라고 생각하지 말고 어떻게 해야 효율적으로 풀이할 지 한 번은 더 생각해봐야겠다.

def solution(commands):
    answer = []
    n = 50
    cells = [[""] * 51 for _ in range(51)]
    group = [[0] * 51 for _ in range(51)]
    group_id = 1
    for c in commands:
        c = c.split()
        if c[0] == UPDATE:
            if len(c) == 4:
                _, r, c, value = c
                r = int(r)
                c = int(c)
                if group[r][c] == 0:
                    cells[r][c] = value
                else:
                    for i in range(1, n + 1):
                        for j in range(1, n + 1):
                            if group[i][j] == group[r][c]:
                                cells[i][j] = value
            else:
                _, v1, v2 = c
                for i in range(1, n + 1):
                    for j in range(1, n + 1):
                        if cells[i][j] == v1:
                            cells[i][j] = v2

        elif c[0] == MERGE:
            r1, c1, r2, c2 = map(int, c[1:])
            if group[r1][c1] != 0 and group[r1][c1] == group[r2][c2]:
                continue

            if len(cells[r1][c1]) > 0 and len(cells[r2][c2]) > 0:
                if group[r1][c1]:
                    temp_group_id = group[r1][c1]
                else:
                    temp_group_id = group_id
                    group_id += 1
                if group[r2][c2] == 0:
                    group[r1][c1] = temp_group_id
                    group[r2][c2] = temp_group_id
                    cells[r2][c2] = cells[r1][c1]
                else:
                    check_id = group[r2][c2]
                    for i in range(1, n + 1):
                        for j in range(1, n + 1):
                            if group[i][j] == check_id:
                                cells[i][j] = cells[r1][c1]
                                group[i][j] = temp_group_id
            else:
                if len(cells[r1][c1]) > 0:
                    cells[r2][c2] = cells[r1][c1]
                    if group[r1][c1]:
                        group[r2][c2] = group[r1][c1]
                    else:
                        group[r1][c1] = group_id
                        group[r2][c2] = group_id
                        group_id += 1
                else:
                    cells[r1][c1] = cells[r2][c2]
                    if group[r2][c2]:
                        group[r1][c1] = group[r2][r2]
                    else:
                        group[r1][c1] = group_id
                        group[r2][c2] = group_id
                        group_id += 1

        elif c[0] == UNMERGE:
            r, c = map(int, c[1:3])
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if group[i][j] == group[r][c]:
                        if not (i == r and j == c):
                            group[i][j] = 0
                            cells[i][j] = ""
        elif c[0] == PRINT:
            r, c = map(int, c[1:])
            if cells[r][c] == "":
                answer.append("EMPTY")
            else:
                answer.append(cells[r][c])

    return answer
"""
