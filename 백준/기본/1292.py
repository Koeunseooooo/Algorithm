a,b = map(int,input().split())

arr=[]
for i in range(1,1000):
    for _ in range(i):
        arr.append(i)
    if(len(arr)>1000):
        break

print(sum(arr[a-1:b]))

# memory : 128mb 제한 31256kb