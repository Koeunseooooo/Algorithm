import sys
from collections import deque

input = sys.stdin.readline


N, s, m = map(int, input().strip().split())
n = list(map(int, input().strip().split()))
q = deque()
dp = [0] * (m + 1)
dp[s] = 1

for i in range(len(n)):
    for j in range(len(dp)):
        cnt = i + 1
        if dp[j] == cnt:
            if 0 <= j - n[i] <= m:
                q.append((j, 0))  # 0은 뺄셈을 의미
            if 0 <= j + n[i] <= m:
                q.append((j, 1))  # 1은 덧셈을 의미
    while q:
        j, cal = q.popleft()
        if cal == 0:
            dp[j - n[i]] = cnt + 1
        else:
            dp[j + n[i]] = cnt + 1

for i in range(len(dp) - 1, -1, -1):
    if dp[i] == N + 1:
        print(i)
        exit()
print(-1)
