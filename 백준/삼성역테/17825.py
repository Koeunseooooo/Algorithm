import sys

input = sys.stdin.readline

score = [
    0,
    2,
    4,
    6,
    8,
    10,
    12,
    14,
    16,
    18,
    20,
    22,
    24,
    26,
    28,
    30,
    32,
    34,
    36,
    38,
    40,
    13,
    16,
    19,
    25,
    22,
    24,
    28,
    27,
    26,
    30,
    35,
    0,
]

graph = [
    [1],
    [2],
    [3],
    [4],
    [5],
    [6, 21],
    [7],
    [8],
    [9],
    [10],
    [11, 25],
    [12],
    [13],
    [14],
    [15],
    [16, 27],
    [17],
    [18],
    [19],
    [20],
    [32],
    [22],
    [23],
    [24],
    [30],
    [26],
    [24],
    [28],
    [29],
    [24],
    [31],
    [20],
    [32],  # 자기 자신?
]

dices = list(map(int, input().strip().split()))
horse = [0, 0, 0, 0]  # 처음에는 시작 칸에 말 4개가 있다

MIN = -1e9
ans = MIN


def dfs(turn, horse, result):
    global ans
    if turn == 10:
        ans = max(result, ans)
        return
    for i in range(4):
        cur = horse[i]
        if len(graph[cur]) > 1:
            cur = graph[cur][1]
        else:
            cur = graph[cur][0]
        cnt = dices[turn]
        for _ in range(1, cnt):  # 이미 위에서 말이 이동하는 칸의 색깔을 확인하기 위해 한 번 움직였으므로 1부터 시작함
            cur = graph[cur][0]
        if cur == 32 or (cur < 32 and cur not in horse):
            before = horse[i]
            horse[i] = cur
            dfs(turn + 1, horse, result + score[cur])
            horse[i] = before


dfs(0, horse, 0)
print(ans)
