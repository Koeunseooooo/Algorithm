from collections import Counter

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc = int(input())
    scores = list(map(int, input().split()))

    _dict = Counter(scores)
    max_value = max(_dict.values())
    cand = []
    for k, v in _dict.items():
        if v == max_value:
            cand.append(k)

    cand.sort(reverse=True)
    print("#{} {}".format(test_case, cand[0]))
