import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().strip().split())

belt = deque(list(map(int, input().strip().split())))
robot = deque([0] * n)  # 컨베이어 벨트에 로봇이 있는 지 없는 지를 확인

up = 0  # 올리는 위치
down = n - 1  # 내리는 위치
answer = 0


while 1:
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0  # 로봇이 내려가는 부분이니 0

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
    for i in range(n - 2, -1, -1):
        if robot[i] == 1 and robot[i + 1] == 0 and belt[i + 1] >= 1:
            robot[i + 1] = 1
            robot[i] = 0
            belt[i + 1] -= 1
    robot[-1] = 0

    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if robot[0] == 0 and belt[0] != 0:
        robot[0] = 1
        belt[0] -= 1

    # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    answer += 1
    if belt.count(0) >= k:
        break  # 종료
print(answer)
