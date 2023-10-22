tc=int(input())
for _ in range(tc):
    n=int(input())
    parent=[0]*(n+1)
    for _ in range(n-1):
        a,b=map(int,input().split())
        parent[b]=a

    ta,tb=map(int,input().split())
    tracking_ta=[]
    # print(parent)
    while True:
        if ta==0:
            break
        tracking_ta.append(ta)
        ta=parent[ta]

    # print(tracking_ta)
    # tracking_ta=set(tracking_ta)
    while True:
        if tb in tracking_ta:
            print(tb)
            break
        tb=parent[tb]