# solve (완전탐색에서 가지치기까지 해야 시간초과 피할 수 있음)
def backtracking(count):
    global n, answer
    if count == cnt:
        temp = int("".join(value))  # swap을 모두 끝내고 최종 완성된 숫자
        if answer < temp:
            answer = temp
        return
    for i in range(n):
        for j in range(i + 1, n):
            value[i], value[j] = value[j], value[i]
            temp = "".join(value)
            if [temp, count] not in v:
                backtracking(count + 1)  # 순서주의.. 먼저 백트래킹으로 다 돌고 방문 여부 표시해야함
                v.append([temp, count])

            value[i], value[j] = value[j], value[i]


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    value, cnt = input().split()
    cnt = int(cnt)
    value = list(value)
    n = len(value)
    v = []  # 동일한 교환횟수 시점에서 동일한 값이 등장한다면 이는 이미 지나간 길이므로 또 연산해줄 필요가 없다.
    answer = 0
    backtracking(0)
    print("#{} {}".format(test_case, answer))
