# 4 7
# 20 15 10 17
n, m = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)
answer = 0  # 높이의 최댓값

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for tree in trees:
        if tree - mid > 0:  # tree가 더 작으면 무시
            cnt += tree - mid
    if cnt >= m:
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1
print(answer)
