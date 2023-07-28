def isPrime(a):
    if a==1:
        return False
    # 이렇게 하면 a가 2일때 true가 나오낭?
    for i in range(2,a):
        if(a%i==0):
            return False
    return True

m = int(input())
n = int(input())


arr=[]
for i in range(m,n+1):
    if isPrime(i):
        arr.append(i)

if(len(arr)==0):
    print(-1)
else:
    print(sum(arr))
    print(arr[0])