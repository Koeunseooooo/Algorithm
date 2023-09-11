import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

parent = [i for i in range(n)]


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


answer = 0
for c in range(m):
    a, b = map(int, input().split())
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)
    if parent_a == parent_b:
        if answer == 0:
            answer = c + 1
    else:
        # union작업
        if parent_a < parent_b:
            parent[parent_b] = parent_a
        else:
            parent[parent_a] = parent_b

print(answer)
