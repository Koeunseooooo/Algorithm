def solution(clothes):
    answer = 1
    result={}
    for i in clothes:
        result[i[1]]=0
        
    for i in clothes:
        result[i[1]]+=1
    
    for v in result.values():
        answer*=v+1
    answer-=1
        
    return answer