import math

N = int(input())

# 왼쪽에서부터 1자리 숫자는 p 나올 수 있음
# 그 외 2자리, 3자리, n자리는 모두 나올 수 있음
p = [2, 3, 5, 7]


def isPrime(a):
    for i in range(2, int(math.sqrt(a)) + 1):  # a의 제곱근을 정수화 한 후 +1
        if a % i == 0:
            return False
    return True


def backtracking(n, num):
    if num == N - 1:
        if isPrime(n):
            print(n)
    tar = n * 10
    for i in range(10):
        tar = tar + 1
        if isPrime(tar):
            backtracking(tar, num + 1)


for i in p:
    backtracking(i, 0)
