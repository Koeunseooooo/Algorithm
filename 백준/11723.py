# 그냥 set을 쓰면 왜 안되는 지 살펴보자
# 사실 되야한다. set은 해시셋이라 O(1) 안에 연산이 거의 다 되기 때문이다.
import sys

m = int(input())
input = sys.stdin.readline
_set = set()
for _ in range(m):
    raw_data = input().strip().split()
    if len(raw_data) > 1:
        com, num = raw_data
        num = int(num)
    else:
        com = raw_data[0]

    if com == "add":
        _set.add(num)
    elif com == "check":
        if num in _set:
            print(1)
        else:
            print(0)
    elif com == "remove":
        _set.discard(num)
    elif com == "toggle":
        if num in _set:
            _set.remove(num)
        else:
            _set.add(num)
    elif com == "all":
        _set = set([i for i in range(1, 21)])
    elif com == "empty":
        _set = set()
