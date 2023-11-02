# 그냥 set을 쓰면 왜 안되는 지 살펴보자 -> 사실 된다 (;) set도 해시셋이라 O(1) 안에 다 끝난다.
# 마지막 비트는 범위 안에 해당하지 않으므로 무시하면 됨

import sys

input = sys.stdin.readline
m = int(input())
_set = 0
for _ in range(m):
    raw_data = input().strip().split()
    if len(raw_data) > 1:
        com, num = raw_data
        num = int(num)
    else:
        com = raw_data[0]

    if com == "add":
        _set = _set | (1 << num)
    elif com == "check":
        if _set & (1 << num):
            print(1)
        else:
            print(0)
    elif com == "remove":
        _set = _set & ~(1 << num)
    elif com == "toggle":
        _set = _set ^ (1 << num)
    elif com == "all":
        _set = (1 << 21) - 1
    elif com == "empty":
        _set = 0


# def bitcount(x):
#     if x == 0:
#         return 0
#     return (x % 2) + bitcount(x // 2)


# # 101000 -> 집합의 크기 2라고 함

# print(bitcount(40))
