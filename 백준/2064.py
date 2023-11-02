# 3
# 194.85.160.177
# 194.85.160.183
# 194.85.160.178
import sys

input = sys.stdin.readline

n = int(input())
ips = []
for i in range(n):
    ips.append(list(map(int, input().strip().split("."))))

m = 0
for i in range(4, -1, -1):  # 오른쪽 바이트부터 검사할것임(인덱스 0은 제외)
    max_ip = ips[0][i]
    min_ip = ips[0][i]
    for j in range(1, n):
        temp_max_ip = ips[j][i]
        if temp_max_ip > max_ip:
            max_ip = temp_max_ip
        if temp_max_ip < min_ip:
            min_ip = temp_max_ip
    diff = max_ip ^ min_ip
    if diff:
        diff_len = len(bin(diff)) - 2
        m += diff
    else:
        m += 8
