# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(2, n - 2):
        temp = arr[i - 2 : i + 2 + 1]
        _max = max(temp[0], temp[1], temp[3], temp[4])
        if _max < temp[2]:
            ans += temp[2] - _max

    print("#{} {}".format(test_case, ans))
