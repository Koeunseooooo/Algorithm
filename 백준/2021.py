import sys
from collections import deque

input = sys.stdin.readline

n, l = map(int, input().split())

rail=[]
for _ in range(l):
    tmp=list(map(int,input().split()))
    rail.append(tmp[:-1])

g = [[] for _ in range(n + 1)]

for i in range(l):
    for j in rail[i]:
        if j == -1:
            break
        g[j].append(i)

st, en = map(int, input().split())


vis = [-2] * (n + 1) # 역 번호와 인덱스 맞추기 위해 n+1로 크기 초기화
rvis = [0] * (l)
q = deque()
q.append(st)
vis[st] = -1
flag = 0
while q:
    cur = q.popleft()

    if cur == en:

        if st == en:
            print(0)


        else:
            print(vis[cur])
        flag = 1
        break

    for i in g[cur]:
        if rvis[i]:
            continue
        rvis[i] = 1
        for j in rail[i]:

            if vis[j]!=-2:
                continue
            vis[j] = vis[cur] + 1
            q.append(j)

if not flag:
    print(-1)
