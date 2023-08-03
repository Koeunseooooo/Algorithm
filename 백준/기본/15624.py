n = int(input())
fib={0:0,1:1}

def fibonacci(n):
    if n in fib:
        return fib[n]
    fib[n]=fibonacci(n-2)+fibonacci(n-1)
    return fib[n]



print(fibonacci(n))


# n = int(input())
 
# dp= [0,1,1]
 
# for i in range(3,n+1):
#     dp.append((dp[i-1]+dp[i-2])%1000000007)
 
# print(dp[n])