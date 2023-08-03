import math
n=[]
while True:
    a= int(input())
    if a!=0:
        n.append(a)
    else:
        break

def getPrimeNum(n):
    if n==1:
        return 1
    arr=[True]*((2*n)+1)
    arr[0]=False
    arr[1]=False

    
    for i in range(2,int(math.sqrt(2*n))+1):
        if arr[i]==True:
            j=2
            while i*j<=2*n:
                arr[i*j]=False
                j+=1
    result =0
    for i in range(n+1,2*n+1):
        if arr[i]==True:
            result+=1
    
    return result

for i in range(len(n)):
    print(getPrimeNum(n[i]))



def fib(n):
    a,b = 1,1
    if n==1 or n==2:
        return 1
        
    for i in range(1,n):
        a,b = b, a+b

    return a

print(fib(5))