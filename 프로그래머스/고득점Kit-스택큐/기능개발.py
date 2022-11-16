def solution(progresses, speeds):
    answer = []
    # 앞타임보다 내가 더 빠르면 앞타임 애의 숫자로 스택을 넣자
    remains =[]
    stack = []
    
    for p,s in zip(progresses,speeds):
        r=(100-p)//s
        if (100-p)%s !=0:
            r=r+1
        remains.append(r)
    
    for r in remains:
        if stack:
            if stack[-1]<r:
                stack.append(r)
            else:
                stack.append(stack[-1])
        else:
            stack.append(r)

    days=sorted(set(stack)) #sorted를 하면 set이 list로 바뀜
    
    for d in days:
        answer.append(stack.count(d))

    return answer