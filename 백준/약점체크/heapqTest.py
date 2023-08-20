import heapq


def heapsort(iterable):  # 오름차순
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result


def heapsort_des(iterable):  # 내림차순
    h = []
    result = []  # 내림차순 정렬하여 받을 리스트
    for value in iterable:
        heapq.heappush(h, -value)
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


print(heapsort([2, 5, 7, 2, 8, 4, 6, 8, 9]))
print(heapsort_des([2, 5, 7, 2, 8, 4, 6, 8, 9]))
