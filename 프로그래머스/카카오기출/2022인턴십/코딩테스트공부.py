def solution(alp, cop, problems):
    answer = 0
    max_alp, max_cop = 0, 0
    INF = 1e9
    for p in problems:
        _alp, _cop, _, _, _ = p
        max_alp = max(max_alp, _alp)
        max_cop = max(max_cop, _cop)

    dp = [[INF] * (max_cop + 1) for _ in range(max_alp + 1)]  # dp 배열 초기화

    alp = min(alp, max_alp)  # 둘중 하나라도 목표값을 넘어가면 안된다.
    cop = min(cop, max_cop)

    dp[alp][cop] = 0  # dp 시작은 초기 알고력, 코딩력에서 부터 시작
    # dp[i][j] : 알고력 i, 코딩력 j일 때의 최단 시간
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            # 기본적으로 공부를 통해서 각각 코딩력, 알고력을 높임
            if i < max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j < max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
            # 비교
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    new_alp = min(
                        i + alp_rwd, max_alp
                    )  # 둘중 하나라도 목표값을 넘어가면 안된다. (반복문 돌 때마다 이렇게 수시로 확인해주어야 한다.)
                    new_cop = min(j + cop_rwd, max_cop)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)

    answer = dp[max_alp][max_cop]
    return answer
