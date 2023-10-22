while True:
    target= input()
    if target=='.':
        break
    target = list(target)
    stack=[]
    isYes=True
    for t in target:
        if t=='(' or t=='[':
            stack.append(t)
        elif t==')':
            if len(stack)==0:
                isYes=False
                break
            tar=stack.pop()
            if tar=='(':
                continue
            elif tar=='[':
                isYes = False
                break
        elif t==']':
            if len(stack)==0:
                isYes=False
                break
            tar = stack.pop()
            if tar == '[':
                continue
            elif tar == '(':
                isYes = False
                break
        else:
            continue

    if isYes:
        if len(stack)!=0:
            print('no')
        else:
            print('yes')
    else:
        print('no')





