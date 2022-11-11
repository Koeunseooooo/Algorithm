def solution(genres, plays):
    answer = []
    result={}
    for i,(x,y) in enumerate(zip(genres,plays)):
        if x not in result:
            result[x]=[]
            result[x].append([y,i])
        else:
            result[x].append([y,i])
    # print(result)
    total={}
    for k,v in result.items():
        result[k].sort(key=lambda x:(-x[0],x[1])) # 내림차, 오름차
        total[sum([i[0] for i in result[k]])]=k
        
    total=sorted(total.items(),key=lambda x:-x[0])
    # print(total)
    
    for t in total:
        if len(result[t[1]])>=2:
            answer.append(result[t[1]][0][1])
            answer.append(result[t[1]][1][1])
        else:
            answer.append(result[t[1]][0][1])
        
    return answer