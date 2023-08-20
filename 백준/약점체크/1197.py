import sys

input = sys.stdin.readline

v, e = map(int, input().split())

edges = []

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))

edges.sort(key=lambda x: x[2])
parent = [i for i in range(v + 1)]


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    x = find_parent(a)
    y = find_parent(b)
    if x < y:
        parent[y] = x

    else:
        parent[x] = y


result = 0

for edge in edges:
    a, b, cost = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost

print(parent)
print(result)
