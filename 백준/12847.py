# 5 3
# 10 20 30 20 10

n, m = map(int, input().split())
arr = list(map(int, input().split()))

window = sum(arr[:m])
answer = window

for i in range(m, n):
    window += arr[i] - arr[i - m]
    answer = max(window, answer)
print(answer)
