import sys

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0] * n for i in range(n)]

homeNum = 0  # 하나의 단지에 집이 몇개 있는 지 셈


def dfs(x, y):
    global homeNum

    if x < 0 or y < 0 or x >= n or y >= n:  # 범위를 벗어나면 fasle
        return False
    if arr[x][y] == 1 and visited[x][y] != 1:  # 방문하지 않았으며 집일 경우
        visited[x][y] = 1
        homeNum += 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


result = []
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            result.append(homeNum)
            homeNum = 0

print(len(result))
result.sort()
for i in range(len(result)):
    print(result[i])
