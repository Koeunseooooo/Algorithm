import sys
from collections import deque
from pprint import pprint

input = sys.stdin.readline

s = int(input().strip())
visited = [[0] * 1001 for _ in range(1001)]  # 카운트 세는 리스트


def bfs():
    q = deque()
    ans = 0
    q.append((1, 0))  # (화면에 존재하는 이모티콘 개수,현재 클립보드에 저장된 이모티콘 개수)
    # visited[1][0] = 1  # 초기화
    while q:
        # print(visited[:5][:5])
        x_screen, x_clip = q.popleft()
        if x_screen == s:
            # print(x_screen, x_clip, visited[x_screen][x_clip])
            ans = visited[x_screen][x_clip]
            # ans = visited[screen][clip]
            break

        arr = [
            (x_screen, x_screen),
            (x_screen + x_clip, x_clip),
            (x_screen - 1, x_clip),
        ]

        for screen, clip in arr:
            if 0 <= screen < 1001 and 0 <= clip < 1001 and not visited[screen][clip]:
                # 첫 번째 경우
                q.append((screen, clip))  # 현재 화면에 존재하는 이모티콘 개수 만큼 클립보드에 저장
                visited[screen][clip] = visited[x_screen][x_clip] + 1
                # print(q)
                # print(visited[screen][clip], "?")
    return ans


print(bfs())
