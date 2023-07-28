k= int(input())
n=3

res=[]
for i in range(k):
    arr=list(map(int,input().split()))
    arr.sort()
    res.append(arr[-3])

for r in res:
    print(r)