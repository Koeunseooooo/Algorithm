# import heapq
# import sys

# input = sys.stdin.readline
# s, b = map(int, input().strip().split())
# visited = [0] * 200001


# def bfs():
#     sec = 0
#     ans_sec = 100001

#     hq = []
#     heapq.heappush(hq, (sec, s))
#     visited[s] = sec

#     while hq:
#         sec, x = heapq.heappop(hq)  # sec가 작은 순으로 pop 하기
#         if ans_sec != 100001:
#             break

#         arr = [x - 1, x + 1, x * 2]

#         for i in range(len(arr)):
#             if 0 <= arr[i] <= 200000 and (
#                 visited[arr[i]] == 0 or visited[arr[i]] >= sec  # depth가 같거나 미방문일 경우
#             ):
#                 if i == 2:
#                     if arr[i] == b:
#                         ans_sec = sec
#                         break
#                     if arr[i] != x:  # x가 0인경우는 무한 0으로 빠지기 때문에 예외처리
#                         visited[arr[i]] = sec
#                         heapq.heappush(hq, (sec, arr[i]))
#                 else:
#                     if arr[i] == b:
#                         ans_sec = sec + 1
#                         break
#                     visited[arr[i]] = sec + 1
#                     heapq.heappush(hq, (sec + 1, arr[i]))
#     return ans_sec


# ans = bfs()
# print(ans)
from collections import deque

n, k = map(int, input().split())  # n: 수빈이가 있는 위치, k: 동생이 있는 위치
q = deque()
q.append(n)
visited = [-1 for _ in range(100001)]
visited[n] = 0

while q:
    s = q.popleft()

    if s == k:
        print(visited[s])
        break
    if 0 <= s - 1 < 100001 and visited[s - 1] == -1:
        visited[s - 1] = visited[s] + 1
        q.append(s - 1)
    if 0 < s * 2 < 100001 and visited[s * 2] == -1:
        visited[s * 2] = visited[s]
        q.appendleft(s * 2)  # 2*s 가 다른 연산보다 더 높은 우선순위를 가지기 위함
    if 0 <= s + 1 < 100001 and visited[s + 1] == -1:
        visited[s + 1] = visited[s] + 1
        q.append(s + 1)
