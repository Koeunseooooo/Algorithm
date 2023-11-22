# unsolve(현재 정확도 85.7)
#


def dfs(arr, cnt, idx, info):  # 현재 과녁판 배열, 남은 화살, 과녁한 배열 가리키는 인덱스
    global maxDiff, answer
    if idx == 11 or cnt == 0:
        # print(arr, 1)
        # 남은 화살은 모두 0점 과녁에 몰빵
        arr[10] += cnt
        # 비교 파트
        ryan_score = 0
        appeach_score = 0
        for i in range(len(info)):
            if arr[i] > info[i]:
                ryan_score += 10 - i
            else:
                if info[i] == 0:
                    continue
                else:
                    appeach_score += 10 - i
        diff = ryan_score - appeach_score
        if diff > 0 and diff >= maxDiff:
            # print(diff)
            flag = 0
            if diff == maxDiff:
                for i in range(10, -1, -1):
                    if answer[i] == arr[i]:
                        continue
                    elif answer[i] > arr[i]:
                        continue
                    else:
                        flag = 1
                if flag:
                    answer = arr[:]
            else:
                maxDiff = diff
                answer = arr[:]
                # print(answer, 1)
        arr[10] -= cnt  # 엥 이거 왜 해줘야하는데 도대체? -> 얻지 않기로 결정할 때 필요..?
        return
    # 점수를 얻기로 결정
    if info[idx] < cnt:
        arr[idx] = info[idx] + 1
        dfs(arr, cnt - (arr[idx]), idx + 1, info)
        arr[idx] = 0
    # 얻지 않기로 결정
    dfs(arr, cnt, idx + 1, info)


maxDiff = 0
answer = []


def solution(n, info):
    global answer
    arr = [0] * 11

    dfs(arr, n, 0, info)
    if len(answer) == 0 or maxDiff == 0:
        answer = [-1]

    return answer


# print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
# print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
# print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
# [1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0]
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
# [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2]
