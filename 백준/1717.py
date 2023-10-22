import sys
sys.setrecursionlimit(1000000) # 재귀 깊이 제한 늘리기
input = sys.stdin.readline

n,m=map(int,input().split())

parent=[0]*(n+1)
for i in range(n+1):
    parent[i] = i

def union_parent(a,b):
    a=find_parent(a)
    b=find_parent(b)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a

def find_parent(x):
    global parent
    if parent[x]!=x:
        parent[x]=find_parent(parent[x])
    return parent[x]

for _ in range(m):
    type,a,b=map(int,input().split())
    if type==0:
        union_parent(a,b)
    else:
        if find_parent(a)==find_parent(b):
            print('YES')
        else:
            print('NO')



