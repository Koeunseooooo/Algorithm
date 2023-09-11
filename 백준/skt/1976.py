import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [0] * (n + 1)

for i in range(1, len(parent)):
    parent[i] = i


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


for i in range(n):
    link = list(map(int, input().split()))
    for j in range(n):
        if link[j] == 1:
            union(i + 1, j + 1)


path = list(map(int, input().strip().split()))


for i in range(len(path) - 1):
    if find_parent(path[i]) != find_parent(path[i + 1]):
        print("NO")
        exit()
else:
    print("YES")
