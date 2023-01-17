def solution1(n, lost, reserve):
    u=[1]*(n+2)
    for i in reserve:
        u[i]+=1
    for j in lost:
        u[j]-=1
    for x in range(1,n+1):
        if u[x-1]==0 and u[x]==2:
            u[x-1],u[x]=1,1
        elif u[x]==2 and u[x+1]==0:
            u[x],u[x+1]=1,1
    return len([i for i in u[1:n+1] if i>0])


def solution2(n, lost, reserve):
    s= set(lost) & set(reserve)
    l= set(lost) - s
    r= set(reserve) -s
    
    for x in sorted(r):
        if x-1 in l:
            l.remove(x-1)
        elif x+1 in l:
            l.remove(x+1)
            
    return n-len(l)