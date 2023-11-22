from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    devil = defaultdict(int)  # 실제 정지 당한 사람 가려내기용
    info = defaultdict(list)
    for r in report:
        a, b = r.split(" ")
        if b not in info[a]:
            info[a].append(b)
            devil[b] += 1
    for id in id_list:
        cnt = 0
        for i in info[id]:
            if devil[i] >= k:
                cnt += 1
        answer.append(cnt)

    return answer
