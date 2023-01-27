def solution(reply):
    
    # 그래프 생성
    remaining = set(range(1, len(reply)))
    forward = [set(l) for l in reply]
    reverse = [set() for _ in range(len(reply))]
    for i, l in enumerate(reply):
        for j in l:
            reverse[j].add(i)
    leafs = [i for i, l in enumerate(reply) if not l]
    
    def remove_cycle():
        
        nonlocal remaining
        
        n = next(iter(remaining))
        nexts = {}
        while n not in nexts:
            nexts[n] = next(iter(forward[n]))
            n = nexts[n]
        
        cycles = [n]
        s_f, s_r = forward[n], reverse[n]
        while 1:
            _n = nexts[cycles[-1]]
            if _n == n:
                break
            s_f.update(forward[_n])
            s_r.update(reverse[_n])          
            cycles.append(_n)
            
        cycles = set(cycles)
        for i in s_r:
            forward[i] -= cycles
            forward[i].add(n)
        for i in s_f:
            reverse[i] -= cycles
            reverse[i].add(n)
        remaining -= set(cycles)
        remaining.add(n)
        s_f -= set(cycles)
        s_r -= set(cycles)      
        
        if s_f:
            return []
        else:
            return [n]
            
    def remove_leafs(leafs):
        nonlocal remaining
        to_remove = set(leafs)
        while leafs:
            leaf = leafs.pop()
            for p in reverse[leaf]:
                if p not in to_remove:
                    leafs.append(p)
                    to_remove.add(p)
        remaining -= to_remove
        return leafs
                  
    ans = len(leafs)
    length = len(remaining)
    while remaining:
        if leafs:
            leafs = remove_leafs(leafs)
        else:
            leafs = remove_cycle()
            ans += len(leafs)
        if len(remaining) >= length:
            raise ValueError
        length = len(remaining)

    return ans