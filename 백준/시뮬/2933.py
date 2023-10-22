import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().strip().split())

dong = [list(input().strip()) for _ in range(r)]

n = int(input())
heights = list(map(int, input().strip().split()))
d = [(0, -1), (0, 1), (1, 0), (-1, 0)]


# bfs를 돌려서 클러스트가 떠있는지 확인 -> 동일한 bfs를 여러번 수행하여 비효율 초래함
# -> 없어진 미네랄의 상하좌우만 검사해보면 된다.
def bfs(y, x, visited):
    q = deque()
    q.append((y, x))
    visited[y][x] = 1
    while q:
        y, x = q.popleft()
        if y == r - 1:
            return True
        for dy, dx in d:
            Y = dy + y
            X = dx + x
            if 0 <= Y < c and 0 <= X < r and dong[Y][X] != "." and not visited[Y][X]:
                q.append((Y, X))
                visited[Y][X] = 1
    return False


def down():
    # dong 배열 업데이트 하는 부분
    # 바닥 또는 다른 클러스터 위에 떨어질 수 있도록 합친다.
    for i in range(c):
        for j in range(r - 2, -1, -1):
            if dong[j][i] != ".":
                visited = [[0] * c for _ in range(r)]
                flag = bfs(j, i, visited)
                if not flag:
                    print(j, i, "start")
                    for k in range(r - 1, j, -1):
                        print(k, i, dong[k][i])
                        if dong[k][i] == ".":
                            dong[k][i] = "x"
                            dong[j][i] = "."
                            for i in range(r):
                                print(dong[i])
                            break


for h in heights:
    h = r - h  # idx로 높이 조정
    left = 1  # 순서 : 왼쪽 먼저
    if left:
        for i in range(c):
            if dong[h][i] != ".":
                dong[h][i] = "."
    else:
        for i in range(c, -1, -1):
            if dong[h][i] != ".":
                dong[h][i] = "."
    print("fight")
    for i in range(r):
        print(dong[i])
    down()


def print_dong():
    for i in range(r):
        print(dong[i])
