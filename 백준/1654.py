# 4 11
# 802
# 743
# 457
# 539

n, k = map(int, input().split())

lans = []
for i in range(n):
    lans.append(int(input()))

start = 1
end = max(lans)
answer = 0
while start <= end:
    pointer = (start + end) // 2
    cnt = 0
    for lan in lans:
        cnt += lan // pointer
    if cnt >= k:
        start = pointer + 1
    else:
        end = pointer - 1
print(end)
