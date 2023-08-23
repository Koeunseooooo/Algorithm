import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().strip().split())

arr = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]  # 시간 갱신
move = [[0] * m for _ in range(n)]  # 칸 수 맞는지 확인

y_1, x_1, y_2, x_2 = map(int, input().strip().split())

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs():
    cnt = 1
    q = deque()
    move = 0
    q.append((y_1, x_1))  # 방향이랑 칸 수 둘 다 갖고 있어야하는데...

    while q:
        y, x = q.popleft()
        # 인덱스 맞추기 위함
        y -= 1
        x -= 1
        for dy, dx in d:
            Y = y + dy
            X = x + dx
            if 0 <= Y < n and 0 <= X < m and arr[Y][X] != "#" and not visited[Y][X]:
                q.append((Y, X))
                #
                # 직전과 방향이 같다면 move+1, 근데 이거 하기 전에 move 범위 내인지 확인하고, 범위 바깥이면 무시(continue)

                # 직전과 방향이 다르다면 move는 0으로 초기화, cnt+=1
                visited[Y][X] = visited[y][x]


bfs()
