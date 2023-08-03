import math
m, n = map(int,input().split())

def isPrime(n):
    arr=[True]*(n+1)
    arr[0]=False
    arr[1]=False
    for i in range(2,int(math.sqrt(n))+1): # 에라토스테네스의 체 + 시간복잡도 반절 줄이기
        if(arr[i]==True):
            j=2
            while(i*j<=n):
                arr[i*j]=False
                j+=1
    return arr

arr = isPrime(n)

# 출력할 때 인덱스 m 이하의 원소들은 무시
for i in range(m,n+1):
    if arr[i]:
        print(i)

