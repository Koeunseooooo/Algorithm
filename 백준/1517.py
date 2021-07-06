#버블 소트..
#시간초과 .. 이유..? 시간복잡도가 n(n-1)/2라서,, 너무 오래걸려서,,

n=int(input())
arr=list(map(int,input().split()))

count=0
for i in range(len(arr)-1,0,-1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            count+=1

print(count)