def count_subarrays_with_avg(A, S):
    n = len(A)
    result = 0
    current_sum = 0
    start = 0
    cnt = 0

    for end in range(n):
        current_sum += A[end]
        cnt += 1

        while current_sum > S:
            if current_sum / cnt == S:
                result += 1
            current_sum -= A[start]
            cnt -= 1
            start += 1

    return result


A = [0, 4, -3, 1]
S = 2
print(count_subarrays_with_avg(A, S))
