def solution(s):
    answer = True
    stack=[]
    
    for c in s:
        if c=='(':
            stack.append(c)
        else: # c가 ')'라면
            if not stack:
                return False
            else:
                stack.pop()
    if len(stack)==0:
        return True
    else:
        return False
        