def solution(babbling):
    can = ["aya","ye","woo","ma"]
    answer = 0
    
    for b in babbling:
        stack=''
        prev='' # prev가 필요한 이유 : 같은 발음을 하는 것을 어려워 한다는 제한 사항 존재
        for c in b:
            stack+=c
            if stack!=prev and stack in can:
                prev=stack
                stack=''
        if len(stack)==0:
            answer+=1
                
        
    return answer