import sys

input = sys.stdin.readline

s = int(input())

cur = 0

i = 1
while True:
    cur += i
    if cur > s:
        i = i - 1
        break
    elif cur == s:
        break
    i += 1


print(i)
