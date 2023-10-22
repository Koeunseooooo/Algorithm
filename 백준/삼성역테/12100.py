import sys

input = sys.stdin.readline

n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().strip().split())))
print(arr)

MAX = -1e9
ans = MAX


# 너가 직접 풀어보삼
def move_arr(cur_arr, d_idx):
    # 방향의 도착지점에
    pass


def dfs(cnt, cur_arr):
    global ans
    cnt += 1
    if cnt == 5:
        return ans
    for i in range(4):
        move_arr(cur_arr, i)


dfs(0, arr)
