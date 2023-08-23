from collections import deque
import sys

input = sys.stdin.readline
s, b = map(int, input().strip().split())

visited = [0] * 200001  # 시간 갱신


def bfs():
    ans_sec = 100001  # 최종 빠른 시간 저장하는 변수

    q = deque()
    ans_cnt = 0  # 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수
    q.append(s)
    visited[s] = 0

    while q:
        x = q.popleft()
        if visited[x] > ans_sec:
            break
        if x == b:
            if ans_sec == 100001:
                ans_sec = visited[x]

            if visited[x] == ans_sec:
                ans_cnt += 1
            continue
        arr = [x - 1, x + 1, x * 2]

        for a in arr:
            if 0 <= a <= 200000 and (visited[a] == 0 or visited[a] == visited[x] + 1):
                visited[a] = visited[x] + 1
                q.append(a)
    return ans_sec, ans_cnt


ans_sec, ans_cnt = bfs()

print(ans_sec)
print(ans_cnt)

"""
이왜틀
from collections import deque
import sys

input = sys.stdin.readline
s, b = map(int, input().strip().split())

visited = []  # 중복 계산 방지


def bfs():
    global s
    q = deque()
    sec = 0  # 시간 갱신 변수
    sec_final = 100001  # 최종 빠른 시간 저장하는 변수
    cnt = 0  # 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수
    q.append((s, cnt))
    visited.append(s)

    while q:
        # print(q)
        s, sec = q.popleft()
        if s == b:
            sec_final = sec
            cnt += 1
            continue
        if sec > sec_final:
            break
        sec += 1
        if s < b:
            cur_1 = s - 1
            cur_2 = s + 1
            cur_3 = s * 2
            if cur_1 not in visited and cur_1 > 0:
                q.append((cur_1, sec))
                visited.append(cur_1)
            if cur_2 not in visited:
                q.append((cur_2, sec))
                visited.append(cur_2)
            if cur_3 not in visited:
                q.append((cur_3, sec))
                visited.append(cur_3)
        elif s > b:
            cur_1 = s - 1
            if cur_1 not in visited:
                q.append((cur_1, sec))
                visited.append(cur_1)
            if cur_1 == b:  # b값인 경우엔 방문 여러번 해두 됨 (예외처리)
                q.append((cur_1, sec))
                visited.append(cur_1)
    return sec_final, cnt


sec, cnt = bfs()

print(sec)
print(cnt)
"""
