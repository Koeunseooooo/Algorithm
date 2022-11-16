from itertools import permutations
def solution(k, dungeons):
    answer = -1
    result=[]
    n=len(dungeons)
    cases = [n for n in range(len(dungeons))]
    pers = list(permutations(cases,n))
    
    for p in pers:
        tmp=0
        tmp_k=k
        for i in p:
            if tmp_k>=dungeons[i][0]:
                tmp_k-=dungeons[i][1]
                tmp+=1
        result.append(tmp)
        
    answer=max(result)
                
    return answer