def solution(candy, positions):
    
    # part1
    n_match, cache = 0, [0]*len(candy)
    for i in range(1, len(candy)):
        while n_match and candy[n_match] != candy[i]:
            n_match = cache[n_match]
        if candy[n_match] == candy[i]:
            n_match += 1
            cache[i] = n_match
    
    # part2
    answer = []
    for pos in positions:
        ans = 0
        while cache[pos-1]:
            pos = cache[pos-1]
            ans += 1
        answer.append(ans)
        
    return answer