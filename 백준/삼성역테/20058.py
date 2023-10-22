import sys
from collections import deque

input = sys.stdin.readline

N, Q = map(int, input().strip().split())
ice = []
for _ in range(2**N):
    ice.append(list(map(int, input().strip().split())))

levels = list(map(int, input().strip().split()))


def rotate_ice(L):
    global ice
    res = [[0] * (2**N) for _ in range(2**N)]
    for y in range(0, 2**N, 2**L):
        for x in range(0, 2**N, 2**L):
            for i in range(2**L):
                for j in range(2**L):
                    # (0,0)에서 시작하지 않아두 이렇게 하면 되어요
                    res[y + j][2**L + x - i - 1] = ice[y + i][x + j]
    return res


d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def remove_ice():
    remove = [
        [0] * (2**N) for _ in range(2**N)
    ]  # 이렇게 계속 배열을 새로 만들어주는 것이 과연 정석 풀이인가? -> 아니다. 그냥 나중에 줄일 좌표만 1차원 리스트에 적어두어도 된다.
    # https://kimjingo.tistory.com/131 참고
    # 인간 디버거의 로그 찍기 블로그 참고하기
    melting_list = []
    for y in range(2**N):
        for x in range(2**N):
            flag = 0
            for dy, dx in d:
                Y = y + dy
                X = x + dx
                if 0 <= Y < (2**N) and 0 <= X < (2**N) and ice[Y][X] > 0:
                    flag += 1

            if flag < 3 and ice[y][x] != 0:
                # remove[y][x] = 1
                melting_list.append((y, x))

    for y, x in melting_list:
        ice[y][x] -= 1
    return ice


MIN = -1e9


def get_chunk_of_ice(ice):
    cnt = 0
    visited = [[0] * (2**N) for _ in range(2**N)]

    for y in range(2**N):
        for x in range(2**N):
            if not visited[y][x] and ice[y][x] != 0:
                q = deque()
                q.append((y, x))
                visited[y][x] = 1
                cur_cnt = 0
                while q:
                    y, x = q.popleft()
                    cur_cnt += 1
                    for dy, dx in d:
                        Y = y + dy
                        X = x + dx
                        if (
                            0 <= Y < 2**N
                            and 0 <= X < 2**N
                            and not visited[Y][X]
                            and ice[Y][X] != 0
                        ):
                            visited[Y][X] = 1
                            q.append((Y, X))
                cnt = max(cnt, cur_cnt)
    return cnt


for l in levels:
    # 격자를 나누어서 모든 부분 격자를 시계방향으로 90도 회전시킨다
    ice = rotate_ice(l)
    # 이후 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다
    ice = remove_ice()

# 파이어스톰 시전 후 , 남은 얼음의 합
total = 0
for i in range(len(ice)):
    total += sum(ice[i])
print(total)
# 가장 큰 덩어리의 개수 찾기
print(get_chunk_of_ice(ice))
