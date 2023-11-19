import heapq


# 오름차순 정렬
def heapsort(arr):
    h = []
    result = []
    for value in arr:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


# 내림차순 정렬
def heapsort2(arr):
    h = []
    result = []
    for value in arr:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


def solve(n, arr):
    while n:
        # 현재 시점기준으로 가장 큰 값과 작은 값
        min_value = max(arr)
        max_value = min(arr)
        min_idx = arr.index(min_value)
        max_idx = arr.index(max_value)
        arr[min_idx] += 1
        arr[max_idx] -= 1
        n -= 1
    min_value = max(arr)
    max_value = min(arr)
    diff = max_value - min_value
    return diff


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 10 + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = solve(n, arr)
    print("#{} {}".format(test_case, answer))


for tc in range(1, 11):
    dump = int(input())
    data = list(map(int, input().split()))

    for _ in range(dump):
        # 최댓값을 1 감소
        max_pos = data.index(max(data))
        data[max_pos] -= 1
        # 최솟값을 1 증가
        min_pos = data.index(min(data))
        data[min_pos] += 1

    # 최댓값과 최솟값의 차이
    result = max(data) - min(data)

    print("#%d %d" % (tc, result))
