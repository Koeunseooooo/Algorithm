import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().strip().split()))
b, c = map(int, input().strip().split())
cnt = 0

# 총감독관
for i in range(len(A)):
    if A[i] > b:
        A[i] -= b
    else:
        A[i] = 0
    cnt += 1

# 부감독관
for i in range(len(A)):
    if A[i] != 0:
        if A[i] % c != 0:
            cnt += A[i] // c + 1
        else:
            cnt += A[i] // c

print(cnt)
