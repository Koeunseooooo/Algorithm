import sys
from itertools import combinations

n = int(sys.stdin.readline())
answer = []

# 반복문을 통해 감소하는 수를 조합
# 최대 감소하는 수는 9876543210
for i in range(1, 11):
    for j in combinations(range(10), i):
        num = sorted(list(j), reverse=True)
        answer.append(int("".join(map(str, num))))

answer.sort()  # 감소하는 수 정렬
print(answer[n] if len(answer) > n else -1)  # 감소하는 수가 있을 때와 없는 경우
