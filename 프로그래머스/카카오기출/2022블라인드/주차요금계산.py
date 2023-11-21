from collections import defaultdict
import math


def solution(fees, records):
    answer = []
    check = defaultdict(bool)
    acc = defaultdict(int)
    time = defaultdict(int)
    for record in records:
        t, num, is_in = record.split()
        h, m = map(int, t.split(":"))
        t = h * 60 + m
        if is_in == "IN":
            acc[num] = t
            check[num] = False
        else:
            time[num] += t - acc[num]
            acc[num] = 0
            check[num] = True

    final = 23 * 60 + 59
    for k, v in acc.items():
        if not check[k]:
            time[k] += final - acc[k]

    for k, v in time.items():
        price = fees[1]
        if v > fees[0]:
            remain = math.ceil((v - fees[0]) / fees[2]) * fees[3]
            price += remain
        time[k] = price

    times = list(time.items())
    times.sort(key=lambda x: x[0])

    for n, v in times:
        answer.append(v)

    return answer
