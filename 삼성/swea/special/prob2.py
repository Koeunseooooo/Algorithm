T = int(input())
for test_case in range(1, T + 1):
    n, a, b = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    high_idx = 0
    high_sco = arr[0]
    for i in range(1, n):
        if arr[i] == high_sco:
            high_idx = i

    base_idx = n - 1
    base_sco = arr[-1]
    for i in range(n - 2, -1, -1):
        if arr[i] == base_sco:
            base_idx = i

    mid_prob = arr[high_idx + 1 : base_idx]
    answer = 0

    def func():
        global mid_prob, answer, a, b
        if len(mid_prob) == 1:
            answer = 1
            return
        scores = list(set(mid_prob))  # 성적별로 자를 수 있는 집합 개수 (다시 리스트화)
        scores.sort(reverse=True)
        for s in scores:
            limit = s
            cnt = 0
            for mid_p in mid_prob:
                if mid_p >= limit:
                    cnt += 1
            if a <= cnt <= b:
                answer = max(answer, cnt)
        if answer == 0:  # two-pointer로 해결했어야 했다..
            cnt = 0
            mid = (len(scores) - 1) // 2
            tar = scores[mid]
            for mid_p in mid_prob:
                if mid_p == tar:
                    cnt += 1
            answer = cnt

    func()
    print("#{} {}".format(test_case, answer))
