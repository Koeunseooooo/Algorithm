from collections import deque
import sys

input = sys.stdin.readline
s, b = map(int, input().strip().split())

move = [0] * 200001  # 부모 노드 저장
visited = [0] * 200001  # 방문 여부 파악 및 sec 갱신
ans_sec = 100001  # 최종 빠른 시간 저장하는 변수
way = []


def bfs():
    global ans_sec
    global way
    q = deque()
    q.append(s)
    move[s] = 0  # 이전 방문 노드를 채울거임. 근데 s는 초기 노드니까 이전 방문 노드 자체가 없으므로 0으로 초기화
    while q:
        x = q.popleft()
        if x == b:
            ans_sec = visited[x]
            # 경로 찾는 파트
            cur_node = x
            way.append(x)
            while True:
                if cur_node == s:
                    break
                way.append(move[cur_node])
                cur_node = move[cur_node]
            print(ans_sec)
            for w in way[::-1]:
                print(w, end=" ")
            break

        arr = [x - 1, x + 1, x * 2]

        for a in arr:
            if 0 <= a <= 200000 and (visited[a] == 0):
                move[a] = x
                visited[a] = visited[x] + 1
                q.append(a)
    return ans_sec


bfs()
