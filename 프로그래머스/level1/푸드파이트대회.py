def solution(food):
    food=food[1:]
    answer = ''
    count=0
    for f in food:
        count=count+1
        if f//2:
            for i in range(f//2):
                answer+=str(count)
            # print(f,f//2)
    opp=answer[::-1]
    answer+='0'
    answer+=opp
                
    return answer