def solution(cost, order):
    
    # part 1    
    order.sort()
    _order = [order[0]]
    for i, (m, n) in enumerate(sorted(order)[1:]):
        _order.append([m - order[i][0], n])
    
    # part 2
    stack = []
    for m, n in _order:
        while stack:
            _m, _n = stack[-1]
            if _m / _n < m / n:
                break
            stack.pop()
            m, n = m + _m, n + _n
        stack.append([m, n])
    
    # part 3
    answer = 0
    for m, n in stack:
        p_prev = 0
        for t, p in cost:
            if m * t >= n:
                break
            answer += (n - m * t) * (p - p_prev) # 넘긴 갯수 * 차액
            p_prev = p
            
    return answer