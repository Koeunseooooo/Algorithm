def solution(s):
    answer = ""
    arr = list(s.split(" "))
    arr2 = list(map(int, arr))
    _max = max(arr2)
    _min = min(arr2)
    answer = str(_min) + " " + str(_max)
    return answer
