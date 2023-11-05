# 1
def check_credit_rating(score):
    if score > 900:
        return 1
    elif score > 800:
        return 2
    elif score > 700:
        return 3
    elif score > 600:
        return 4
    elif score > 500:
        return 5
    elif score > 400:
        return 6
    elif score > 300:
        return 7
    elif score > 200:
        return 8
    else:
        return 9


def solution(score):
    answer = []
    m = len(score[0])

    for s in score:
        s.sort()
        s = s[1:-1]
        s_s = sum(s) / (m - 2)
        rate = check_credit_rating(s_s)
        answer.append(rate)
    return answer


# 2
from itertools import product, permutations, combinations


def solution(dice):
    n = len(dice)
    # nums 리스트의 값이 0인 경우 해당 인덱스의 수는 나올 수 없는 수,
    # 1인 경우 실제 나온 수를 의미한다.
    nums = [0] * (10**n + 1)
    nums[0] = 1

    # 주사위를 선택할 수 있는 모든 경우의 수(인덱스)를 구한다.
    part_dice = []
    for r in range(1, n + 1):
        for comb in list(combinations(list(range(n)), r)):
            part_dice.append(comb)

    # part_dice를 통해 주사위를 선택할 수 있는 모든 경우의 수(실제 값)에 대한 리스트를 구한다.
    candidate_dice = []
    for part in part_dice:
        temp_dice = []
        for p in part:
            temp_dice.append(dice[p])
        candidate_dice.append(temp_dice)

    for cur_dice in candidate_dice:
        # 각 리스트에 대한 중복순열을 구한다.
        for _product in list(product(*cur_dice)):
            # 조합에 대한 순열을 구한다.
            for _permu in list(permutations(_product)):
                # 0이 맨 앞에 등장할 경우 continue
                if _permu[0] == 0:
                    continue
                # 주사위로 숫자를 만든다
                result = int("".join(map(str, _permu)))
                # 숫자에 해당하는 index에 접근하여 1로 업데이트 해준다. (방문처리)
                nums[result] = 1

    # nums 리스트에서 0이 가장 먼저 등장하는 idx가 결국 만들 수 없는 가장 작은 자연수를 의미한다.
    answer = nums.index(0)
    return answer


# 3
def solution(diet):
    answer = 0
    n = len(diet)
    dp = [[0] * 3 for _ in range(n)]
    dp[0][0] = diet[0][0]
    dp[0][1] = diet[0][1]
    dp[0][2] = diet[0][2]

    for i in range(1, n):
        for j in range(3):
            if j == 0:  # 아침 (전날 아침, 전날 점심, 전날 저녁)
                dp[i][j] = min(
                    diet[i][j] + dp[i - 1][j],
                    diet[i][j] + dp[i - 1][j + 1],
                    diet[i][j] + dp[i - 1][j + 2],
                )
            elif j == 1:  # 점심 (전날 점심, 전날 저녁, 오늘 아침)
                dp[i][j] = min(
                    diet[i][j] + dp[i - 1][j],
                    diet[i][j] + dp[i - 1][j + 1],
                    diet[i][j] + dp[i][j - 1],
                )
            elif j == 2:  # 저녁 (전날 저녁, 오늘 아침, 오늘 점심)
                dp[i][j] = min(
                    diet[i][j] + dp[i - 1][j],
                    diet[i][j] + dp[i][j - 1],
                    diet[i][j] + dp[i][j - 2],
                )
    answer = min(dp[n - 1])
    return answer
