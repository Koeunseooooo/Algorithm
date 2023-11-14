from collections import deque


def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    mid = (sum1 + sum2) // 2
    limit = len(queue1) * 4
    while True:
        if sum1 > sum2:
            tar = q1.popleft()
            q2.append(tar)
            sum1 -= tar
            sum2 += tar
            answer += 1
        elif sum1 < sum2:
            tar = q2.popleft()
            q1.append(tar)
            sum1 += tar
            sum2 -= tar
            answer += 1
        else:
            break
        if answer == limit:
            answer = -1
            break
    return answer
