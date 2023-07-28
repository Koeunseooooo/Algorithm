k= int(input())
arr = list(map(int,input().split()))

def isPrime(a):
    if a==1 :
        return False
    for i in range(2,a):
        if(a%i==0):
            return False
    return True

result = 0
for a in arr:
    if isPrime(a):
        result +=1
    
print(result)

