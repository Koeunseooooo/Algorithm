T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = []
    for _ in range(n):
        temp = list(input())
        temp = list(map(int, temp))
        arr.append(temp)
    result = 0
    mid = n // 2  # 가운데 인덱스
    for i in range(n // 2):  # 0~2까지 돌아감
        # 위쪽
        tar = arr[i]
        s = mid - i
        e = mid + i
        tar = tar[s : e + 1]
        result += sum(tar)
        # 아래쪽
        tar = arr[n - i - 1]
        s = mid - i
        e = mid + i
        tar = tar[s : e + 1]
        result += sum(tar)
    result += sum(arr[mid])
    print("#{} {}".format(test_case, result))
