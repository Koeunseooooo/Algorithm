# https://school.programmers.co.kr/questions/42319


import math


def division_search(num_bin):
    global flag
    if len(num_bin) == 1:
        return 1
    mid = len(num_bin) // 2
    if num_bin[mid] == "0":
        for i in range(0, mid):
            if num_bin[i] == "1":
                return 0
        for j in range(mid + 1, len(num_bin)):
            if num_bin[j] == "1":
                return 0
    res1 = division_search(num_bin[:mid])
    res2 = division_search(num_bin[mid + 1 :])
    return res1 & res2


def solution(numbers):
    answer = []
    for n in numbers:
        flag = 1
        num_bin = bin(n).replace("0b", "")
        digit = (
            2 ** (int(math.log(len(num_bin), 2)) + 1) - 1
        )  # 포화 이진트리를 만들기 위해 필요한 총 노드 개수
        num_bin = "0" * (digit - len(num_bin)) + num_bin
        if num_bin[len(num_bin) // 2] == "1":  # 루트노드가 1이라면
            answer.append(division_search(num_bin))
        else:
            answer.append(0)

    return answer
