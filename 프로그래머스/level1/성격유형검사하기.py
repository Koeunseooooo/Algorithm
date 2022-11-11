def solution(survey, choices):
    answer = ''
    result=[0,0,0,0] #경우의 수가 8개인데 4개로 줄이고 +-로 조정하려니까 좀 헷갈리긴함..
    # RT/CF/JM/AN
    
    for i in range(len(survey)):
        sur=survey[i][0]
        if sur=='R':
            result[0]+=choices[i]-4
        elif sur=='T':
            result[0]-=choices[i]-4
        elif sur=='C':
            result[1]+=choices[i]-4
        elif sur=='F':
            result[1]-=choices[i]-4
        elif sur=='J':
            result[2]+=choices[i]-4
        elif sur=='M':
            result[2]-=choices[i]-4
        elif sur=='A':
            result[3]+=choices[i]-4
        elif sur=='N':
            result[3]-=choices[i]-4
    
    if result[0]>0:
        answer+='T'
    else:
        answer+='R'
        
    if result[1]>0:
        answer+='F'
    else:
        answer+='C'
    
    if result[2]>0:
        answer+='M'
    else:
        answer+='J'
    
    if result[3]>0:
        answer+='N'
    else:
        answer+='A'
        
            
            
    return answer