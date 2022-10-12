N = int(input())
ans = 1
B = list(map(int, input().split()))
for n in B:
    ans = ans * n

print(ans)