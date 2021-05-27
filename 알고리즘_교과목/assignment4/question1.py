def memoization_fibo(n):
    memo[0]=1
    memo[1]=1

    if n<2:
        return memo[n]

    for i in range(2,n+1):
        memo[i] = memo[i-2] + memo[i-1]

    return memo[n]

if __name__ == '__main__':
    n=int(input("숫자를 입력하세용"))
    memo =[ 0 for i in range(n+2)]
    print(memoization_fibo(n))
