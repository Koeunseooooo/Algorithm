parent=[]

def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)
    parent[b]=a # a가 무조건  작게 들어가니까 b가 a를 바라봐야함

    def input():
        return stdin.readline().rstrip()

    global parents

    g = int(input())
    p = int(input())
    planes = [int(input()) for _ in range(p)]

    parents = list(i for i in range(g + 1))
    cnt = 0
    for plane in planes:
        plane = find(plane)
        # 도킹 가능한 게이트가 없는 경우
        if plane == 0:
            break
        union(plane - 1, plane)
        cnt += 1

    print(cnt)