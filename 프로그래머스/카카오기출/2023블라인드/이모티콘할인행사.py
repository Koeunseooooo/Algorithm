from itertools import product


def solution(users, emoticons):
    candidate = []
    e_rates = [10, 20, 30, 40]
    n = len(emoticons)
    for idx, p in enumerate(product([10, 20, 30, 40], repeat=n)):
        service = 0
        money = 0
        for user in users:
            u_rate, u_price = user
            temp = 0
            for e_rate, e_price in zip(p, emoticons):
                if e_rate >= u_rate:
                    temp += e_price * (100 - e_rate) * 0.01
            if temp >= u_price:
                service += 1
            else:
                money += temp
        candidate.append([service, money])

    candidate.sort(key=lambda x: (-x[0], -x[1]))
    answer = candidate[0]

    return answer
