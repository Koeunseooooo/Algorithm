import math


def solution(n, k):
    k_n = ""
    while n:  # k진수 변환
        k_n = str(n % k) + k_n
        n = n // k

    arr = k_n.split("0")

    def isPrime(n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    cnt = 0
    for a in arr:
        if len(a) == 0:
            continue
        if int(a) == 1:
            continue
        if isPrime(int(a)):
            cnt += 1

    return cnt
