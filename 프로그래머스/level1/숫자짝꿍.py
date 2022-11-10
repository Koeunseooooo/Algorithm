def solution(X, Y):
    answer=""
    a=[0 for i in range(10)]
    b=[0 for i in range(10)]
    for i in X:
        a[int(i)]+=1
    for i in Y:
        b[int(i)]+=1
    
    for i in range(9,-1,-1): # 애초에 위에서부터 빼면 정렬할 필요가 없다... wow
        while(True):
            if a[i]==0 or b[i]==0:
                break
            answer+=str(i)
            a[i]-=1
            b[i]-=1
    # print(answer)
    if len(answer)==0:
        answer="-1"
    elif answer.count('0')==len(answer):
        answer='0'
        
    
    return answer