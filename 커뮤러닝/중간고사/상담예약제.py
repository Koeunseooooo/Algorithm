def parse_time(t):
    h, m = map(int, t.split(':'))
    return 60*h + m

def solution(booked, unbooked):
    
    booked = [(parse_time(t), name) for t, name in booked] + [(1000000, None)]
    unbooked = [(parse_time(t), name) for t, name in unbooked] + [(1000000, None)]
    booked.sort()
    unbooked.sort()
    b, u, t, answer = 0, 0, 0, []
    
    while b < len(booked) and u < len(unbooked):
        
        t1, t2 = booked[b][0], unbooked[u][0]
        if t1 <= t:
            answer.append(booked[b][1])
            b += 1
            t += 10
        elif t2 <= t:
            answer.append(unbooked[u][1])
            u += 1
            t += 10
        else:
            t = min(t1, t2)
    
    answer.pop()
    return answer