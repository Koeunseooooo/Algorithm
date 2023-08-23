import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())


def bfs():
    q = deque()
    depth = 1
    result = 0
    q.append((a, depth))
    while q:
        n, depth = q.popleft()
        if n == b:
            result = depth
            break
        depth += 1
        # 2를 곱하는 경우
        cur_1 = n * 2
        if cur_1 < b:
            q.append((cur_1, depth))
        elif cur_1 == b:
            result = depth
            break
        # 1의 수를 가장 오른쪽에 추가하는 경우
        cur_2 = n * 10 + 1
        if cur_2 < b:
            q.append((cur_2, depth))
        elif cur_2 == b:
            result = depth
            break
    return result


result = bfs()
if not result:
    print(-1)
else:
    print(result)
