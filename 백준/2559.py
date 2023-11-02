import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

sum = 0


for i in range(k):
    sum += arr[i]

answer = sum

for i in range(k, n):
    sum += arr[i] - arr[i - k]
    answer = max(answer, sum)
print(answer)
