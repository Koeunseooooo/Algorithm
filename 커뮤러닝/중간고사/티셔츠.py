def solution(people, tshirts):
    people.sort()
    tshirts.sort()
    p, t, ans = 0, 0, 0
    while p < len(people) and t < len(tshirts):
        if tshirts[t] >= people[p]:
            ans += 1
            p += 1
        t += 1
    return ans