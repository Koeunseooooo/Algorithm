X = "ABCDEF"
Y = "GBCDFE"


def longest_common_string(X, Y):  # 최장 공통 문자열
    dp = [[0] * (len(Y) + 1) for _ in range(len(X) + 1)]
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if Y[i - 1] == X[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = 0
    mx = 0  # dp 최댓값 찾기
    for i in range(1, len(dp)):
        tmp_mx = max(dp[i])
        mx = max(mx, tmp_mx)
    return mx


def longest_common_subSeqeunse(X, Y):  # 최장 공통 부분수열
    dp = [[0] * (len(Y) + 1) for _ in range(len(X) + 1)]
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if Y[i - 1] == X[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


print(longest_common_string(X, Y))
print(longest_common_subSeqeunse(X, Y))
