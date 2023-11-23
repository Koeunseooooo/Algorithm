import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)  # 이걸 안쓰면 런타임 에러가 뜨다니
# 문자 순서가 d l r u 아래 왼 오 위
d = [(1, 0), (0, -1), (0, 1), (-1, 0)]
d_al = ["d", "l", "r", "u"]
answer = "z"


def dfs(n, m, x, y, r, c, s, cnt, k):
    global answer
    if k < cnt + abs(x - r) + abs(y - c):  # 현재 남은 이동거리보다 맨해튼 거리가 더 크다면
        return
    if x == r and y == c and cnt == k:
        answer = s
        return
    for i in range(4):
        X = x + d[i][0]
        Y = y + d[i][1]
        if 1 <= X <= n and 1 <= Y <= m and s < answer:
            dfs(n, m, X, Y, r, c, s + d_al[i], cnt + 1, k)


def solution(n, m, x, y, r, c, k):
    m_dist = abs(x - r) + abs(y - c)
    if k < m_dist or (k - m_dist) % 2:
        return "impossible"

    dfs(n, m, x, y, r, c, "", 0, k)
    return answer
