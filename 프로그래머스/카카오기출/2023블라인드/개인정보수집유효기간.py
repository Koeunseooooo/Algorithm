"""
2023.11.06
"""


# 계산의 편의를 위해 일수로 변환하기
def time_convert(t):
    year, month, day = map(int, t.split("."))
    return year * 12 * 28 + month * 28 + day


def solution(today, terms, privacies):
    answer = []
    today = time_convert(today)
    term = {}
    for t in terms:
        c, n = t.split()
        term[c] = int(n) * 28
    for idx, p in enumerate(privacies):
        s, n = p.split()
        s = time_convert(s)
        e = s + term[n]
        if today < e:
            continue
        else:
            answer.append(idx + 1)

    return answer
