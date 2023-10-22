'''
빡구현 문제. 이문제에선 그래프 모양의 변형이 자주 일어나고 리스트의 왼쪽에서 삭제할 일이 많기 때문에
collections의 deque()를 사용하는게 좋았다. 그리고 deque()의 reverse() 기능을 사용해서
시계방향 180도 회전 함수를 쉽게 작성할 수 있었다.
'''
from collections import deque
import sys
input = sys.stdin.readline
N,K = map(int,input().split())
d=[(-1,0),(1,0),(0,-1),(0,1)]
board=[]
board.append(deque(list(map(int,input().split()))))
print(board)

def get_result(board):
    dp=board[0]
    result1=max(dp)-min(dp)
    return result1

def push_fish_to_min_bowl(graph):
    min_bowl_fish_num = min(graph[0])
    for i in range(len(graph[0])):
        if graph[0][i] == min_bowl_fish_num:
            graph[0][i] += 1

def popleft_and_stack(board):
    pop=board[0].popleft()
    board.append(deque([pop]))

def rotate_90_clockwise(bowls):
    # 일단 가로 세로가 바뀌어 엥 지금보니까 그냥 직사각형 회전이다!
    new_bowls = [[0] * len(bowls) for _ in range(len(bowls[0]))]
    for i in range(len(bowls[0])):
        for j in range(len(bowls)):
            new_bowls[i][j] = bowls[j][len(bowls[0]) - 1 - i]

    return new_bowls


def fly_blocks(graph):
    while True:
        will_fly_blocks=[]
        will_fly_blocks_row=len(graph)
        will_fly_lbocks_col=len(graph[-1])
        for i in range(will_fly_blocks_row):
            new_deque=deque()
            for _ in range(will_fly_lbocks_col):
                new_deque.append(graph[i].popleft())
            will_fly_blocks.append(new_deque)
        # 다시 graph를 업데이트 하는거야
        graph=[graph[0]]
        rotated_blocks=rotate_90_clockwise(will_fly_blocks)
        for row in rotated_blocks:
            graph.append(deque(row))

answer =0
while True:
    result = get_result(board)
    if result <=K:
        print(answer)
        break
    push_fish_to_min_bowl(board)
    popleft_and_stack(board)
    print(board)
    board=fly_blocks(board)
    break