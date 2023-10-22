arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

## zip
# 시계 방향 90 (= 반시계 방향 270)
arr_90 = list(map(list, zip(*arr[::-1])))
print(arr_90)

# 시계 방향 180 (= 반시계 방향 180)
arr_180 = [a[::-1] for a in arr[::-1]]
print(arr_180)

# 시계 방향 270 (= 반시계 방향 90)
arr_270 = [x[::-1] for x in list(map(list, zip(*arr[::-1])))[::-1]]
print(arr_270)

## 인덱싱
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = 3
### 시계 방향 90 (= 반시계 방향 270)
new_90 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_90[j][n - i - 1] = arr[i][j]
print(new_90)

### 시계 180 & 반시계 180
new_180 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_180[n - i - 1][n - j - 1] = arr[i][j]
print(new_180)

### 시계 270 & 반시계 90
new_270 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_270[n - 1 - j][i] = arr[i][j]
print(new_270)
