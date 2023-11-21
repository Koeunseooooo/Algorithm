from collections import deque

n = int(input())
m = int(input())
arr = []
for _ in range(m):
    arr.append(list(map(int, input())))

visited = [[0] * n for _ in range(m)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
route = []


def bfs(y, x, visited, level, isBoundary=0):
    if visited[y][x]:  # 이미 방문한 곳이라면 바로 return
        return
    global route
    q = deque()
    q.append((y, x))
    visited[y][x] = 1
    target = arr[y][x]
    new = []
    cnt = 1
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            Y = y + dy
            X = x + dx
            if 0 <= Y < m and 0 <= X < n and visited[Y][X] == 0:
                visited[Y][X] = 1
                if arr[Y][X] == target:
                    q.append((Y, X))
                    cnt += 1
                else:
                    new.append((Y, X))

    if len(new) > 0:
        for y, x in new:
            visited[y][x] = 0
        if isBoundary:
            return
        for y, x in new:
            bfs(y, x, visited, level + 1)
    else:
        if isBoundary:
            return
    route.append([cnt, level])
    return


level = 0
bfs(0, 0, visited, level, 1)

answer = []
for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j, visited, 1)
            answer.append(route)
            route = []


# to-do : route를 출력 형식에 맞게 처리해야함
result = []
for a in answer:
    a.sort(key=lambda x: -x[1])
    for i in range(len(a)):
        c, l = a[i]
        for j in range(i, len(a)):
            _, nl = a[j]
            if l - 1 == nl:
                a[j][0] += c
    a.sort(key=lambda x: x[1])
    temp = []
    for i in range(len(a)):
        temp.append("." * (a[i][1] - 1) + str(a[i][0]))
    temp[0] = int(temp[0])
    result.append(temp)

result.sort(key=lambda x: -x[0])

for r in result:
    for i in range(len(r)):
        print(r[i])
