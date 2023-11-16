# unsolve .. (시간초과)


def backtracking(count):
    global n, answer
    if not count:
        temp = int("".join(value))  # swap을 모두 끝내고 최종 완성된 숫자
        if answer < temp:
            answer = temp
        return
    for i in range(n):
        for j in range(i + 1, n):
            value[i], value[j] = value[j], value[i]
            # temp = "".join(value)
            backtracking(count - 1)
            value[i], value[j] = value[j], value[i]


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    value, cnt = input().split()
    cnt = int(cnt)
    value = list(value)
    n = len(value)
    answer = int("".join(value))
    backtracking(cnt)
    print("#{} {}".format(test_case, answer))
